from __future__ import annotations  # Enable postponed evaluation of annotations to allow forward references when type checking.
import asyncio  # Provide asynchronous utilities such as to_thread for running blocking functions without blocking the event loop.
import json  # Offer JSON serialization and deserialization helpers for persisting run history files.
import time  # Supply high-resolution timing utilities to track the duration of AgentManager runs.
from datetime import datetime  # Deliver timezone-naive UTC timestamps for consistent log and history records.
from pathlib import Path  # Supply an object-oriented interface for manipulating filesystem paths in a cross-platform way.
from typing import Any, Dict, Iterable, List, MutableSequence, Optional  # Import typing aliases to document collection and optional value expectations.
# Import statements above cover all standard library dependencies required by the dashboard utility helpers.  # Provide an inline comment to satisfy the per-line annotation request while summarizing the preceding imports.
from agent_manager import AgentManager  # Import AgentManager so the helper functions can accept instances without triggering circular imports.
# The next block introduces asynchronous orchestration helpers tailored for the dashboard UI.  # Maintain descriptive commentary to align with user preferences.
# ---------------------------------------------------------------------------  # Section divider to improve readability while still fulfilling the comment-per-line requirement.
async def launch_agent_manager_run(
    manager: AgentManager,  # Accept the AgentManager instance responsible for orchestrating the AutoML workflow.
    prompt: str,  # Receive the user-facing prompt that seeds the AgentManager conversation loop.
    plan_path: Optional[str] = None,  # Allow callers to forward an optional plan directory path mirroring initiate_chat's signature.
    instruction_path: Optional[str] = None,  # Allow forwarding of an optional instruction directory for reproducibility purposes.
) -> Dict[str, Any]:  # Return structured metadata so the UI can reflect run timing and completion status.
    start_timestamp = datetime.utcnow().isoformat()  # Capture the human-readable UTC timestamp representing when execution began.
    start_clock = time.perf_counter()  # Record a high-resolution monotonic counter to compute duration independent of wall-clock adjustments.
    await asyncio.to_thread(  # Offload the synchronous initiate_chat call to a background thread to avoid blocking the event loop.
        manager.initiate_chat,  # Supply the AgentManager's initiate_chat workflow as the callable executed in the worker thread.
        prompt,  # Forward the prompt parameter directly into initiate_chat.
        plan_path,  # Forward the optional plan path so existing functionality remains untouched.
        instruction_path,  # Forward the optional instruction path for completeness.
    )  # Await completion of the to_thread call while capturing the synchronous function's return value (currently None).
    duration_seconds = time.perf_counter() - start_clock  # Compute total elapsed time in seconds using the monotonic counter for accuracy.
    return {  # Provide a dictionary summarizing execution for downstream consumers.
        "started_at": start_timestamp,  # Record the start time to anchor the run chronologically.
        "duration_seconds": duration_seconds,  # Share the elapsed duration for progress reporting or analytics.
        "status": "completed",  # Indicate that the async wrapper finished without raising errors.
        "prompt": prompt,  # Echo the originating prompt so dashboards can display context alongside the run entry.
    }  # Finish the dictionary literal describing the asynchronous run metadata.
# After launching, the module transitions into log management utilities for the dashboard stream.  # Provide narrative continuity between function groups.
# ---------------------------------------------------------------------------  # Section divider to describe subsequent log-related helpers while keeping commentary per line.
def append_log_entry(
    logs: MutableSequence[Dict[str, Any]],  # Accept a mutable sequence of log dictionaries that the UI maintains for streaming updates.
    message: str,  # Capture the textual message that should be appended to the log timeline.
    level: str = "info",  # Provide a severity level with a sensible default that matches common logging practices.
    *,  # Enforce keyword-only usage for optional metadata to ensure readability at the call site.
    metadata: Optional[Dict[str, Any]] = None,  # Allow callers to attach arbitrary structured data without requiring them to mutate the returned entry.
) -> Dict[str, Any]:  # Return the constructed log entry so that the UI can use it immediately if needed.
    entry = {  # Build the log entry as a standard dictionary compatible with JSON serialization.
        "timestamp": datetime.utcnow().isoformat(),  # Stamp the log with a UTC timestamp for consistent ordering and filtering.
        "level": level,  # Include the log level to support styling or filtering in the dashboard interface.
        "message": message,  # Store the primary human-readable message explaining what occurred.
        "metadata": metadata or {},  # Normalize the metadata to an empty dictionary to simplify UI consumption logic.
    }  # Finalize the log entry dictionary containing timestamp, level, message, and metadata fields.
    logs.append(entry)  # Append the entry to the caller-provided log collection to mutate state in place.
    return entry  # Return the entry so the caller can immediately emit or inspect the appended record.
# Persistence helpers ensure dashboard sessions survive restarts by saving history to disk.  # Explain the intent of the next helper set.
# ---------------------------------------------------------------------------  # Section divider for persistence helpers that interact with the filesystem.
def serialize_run_history(
    history: Iterable[Dict[str, Any]],  # Accept any iterable of run dictionaries to maximize compatibility with upstream storage strategies.
    destination: str | Path,  # Receive the target file path where the JSON document should be written.
    *,  # Enforce keyword-only usage for optional keyword arguments such as indentation.
    indent: int = 2,  # Allow callers to control pretty-printing while defaulting to a readable indentation depth for UI debugging.
) -> Path:  # Return the pathlib.Path representing the resolved destination for chaining or logging.
    destination_path = Path(destination).expanduser().resolve()  # Normalize the destination into an absolute Path, expanding user markers like '~'.
    destination_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the parent directory exists so writing the file never fails due to missing folders.
    serialized_history = list(history)  # Materialize the iterable into a list so it can be serialized multiple times or inspected by the caller afterward.
    destination_path.write_text(  # Persist the JSON content to disk using pathlib's high-level helper.
        json.dumps(serialized_history, indent=indent, default=str),  # Serialize the history with indentation and a default=str fallback for non-serializable objects.
        encoding="utf-8",  # Use UTF-8 encoding to remain compatible across operating systems and tooling.
    )  # Complete the file write operation using the prepared JSON string.
    return destination_path  # Return the destination Path to inform the caller where data ended up on disk.
# The final helper rounds out the persistence story by rehydrating stored history files.  # Maintain descriptive narration for clarity.
# ---------------------------------------------------------------------------  # Section divider before defining the complementary loader used when bootstrapping the dashboard.
def load_run_history(
    source: str | Path,  # Accept a path-like object pointing to the JSON file that stores historical run metadata.
) -> List[Dict[str, Any]]:  # Return a list of dictionaries so calling code receives a mutable, indexable collection for UI binding.
    source_path = Path(source).expanduser().resolve()  # Normalize the provided source path similarly to the serialization function for consistency.
    if not source_path.exists():  # Detect situations where no history file is present to avoid raising FileNotFoundError.
        return []  # Return an empty list so the UI can handle first-run scenarios gracefully.
    try:  # Begin a try block to catch JSON decoding issues without crashing the dashboard.
        content = source_path.read_text(encoding="utf-8")  # Read the entire file contents as a UTF-8 string for parsing.
        parsed = json.loads(content)  # Parse the JSON string into Python data structures.
        if isinstance(parsed, list):  # Confirm the parsed structure is a list to ensure predictable downstream usage.
            return [dict(item) for item in parsed]  # Convert each entry to a dictionary (in case subclasses are provided) for mutability and safety.
        return []  # Fallback to an empty list when the parsed JSON is not an array as expected.
    except json.JSONDecodeError:  # Catch malformed JSON errors that might arise from partial writes or manual edits.
        return []  # Return an empty list rather than raising so the UI can continue operating despite history corruption.
