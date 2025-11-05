import requests

from bs4 import BeautifulSoup
from urllib.parse import unquote
from serpapi import GoogleSearch
from kaggle.api.kaggle_api_extended import KaggleApi

from openai import OpenAI, AzureOpenAI
from configs import AVAILABLE_LLMs


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def get_kaggle():
    api = KaggleApi()
    api.authenticate()
    return api


def search_web(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": "your api key",
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results["organic_results"]


def print_message(sender, msg, pid=None):
    pid = f"-{pid}" if pid else ""
    sender_color = {
        "user": color.PURPLE,
        "system": color.RED,
        "manager": color.GREEN,
        "model": color.BLUE,
        "data": color.DARKCYAN,
        "prompt": color.CYAN,
        "operation": color.YELLOW,
    }
    sender_label = {
        "user": "💬 You:",
        "system": "⚠️ SYSTEM NOTICE ⚠️\n",
        "manager": "🕴🏻 Agent Manager:",
        "model": f"🦙 Model Agent{pid}:",
        "data": f"🦙 Data Agent{pid}:",
        "prompt": "🦙 Prompt Agent:",
        "operation": f"🦙 Operation Agent{pid}:",
    }

    msg = f"{color.BOLD}{sender_color[sender]}{sender_label[sender]}{color.END}{color.END} {msg}"
    print(msg)
    print()


def get_client(llm: str = "qwen"):
    """
    Get an OpenAI or Azure OpenAI client based on the LLM configuration.

    Args:
        llm: The LLM identifier from AVAILABLE_LLMs

    Returns:
        OpenAI or AzureOpenAI client instance
    """
    llm_config = AVAILABLE_LLMs.get(llm, AVAILABLE_LLMs.get("gpt-3.5"))
    provider = llm_config.get("provider", "openai")

    if provider == "azure":
        # Azure OpenAI client
        return AzureOpenAI(
            api_key=llm_config["api_key"],
            api_version=llm_config["api_version"],
            azure_endpoint=llm_config["endpoint"]
        )
    elif provider == "openai" or llm.startswith("gpt"):
        # Standard OpenAI client
        return OpenAI(api_key=llm_config["api_key"])
    else:
        # Local or custom endpoint
        return OpenAI(
            base_url=llm_config["base_url"],
            api_key=llm_config["api_key"],
        )
