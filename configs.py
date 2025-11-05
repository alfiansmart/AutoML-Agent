class Configs:
    OPENAI_KEY = ""  # your openai's account api key
    HF_KEY = ""
    PWC_KEY = ""
    SEARCHAPI_API_KEY = ""
    TAVILY_API_KEY = ""

    # Azure OpenAI Configuration
    AZURE_OPENAI_ENDPOINT = ""  # e.g., "https://your-resource.openai.azure.com/"
    AZURE_OPENAI_KEY = ""  # your Azure OpenAI API key
    AZURE_API_VERSION = "2024-02-15-preview"  # Azure API version

AVAILABLE_LLMs = {
    "prompt-llm": {
        "api_key": "empty",
        "model": "prompt-llama",
        "base_url": "http://localhost:8000/v1",
        "provider": "local",
    },
    "gpt-4.1": {
        "api_key": Configs.OPENAI_KEY,
        "model": "gpt-4.1",
        "provider": "openai",
    },
    "gpt-4": {
        "api_key": Configs.OPENAI_KEY,
        "model": "gpt-4o",
        "provider": "openai",
    },
    "gpt-3.5": {
        "api_key": Configs.OPENAI_KEY,
        "model": "gpt-3.5-turbo",
        "provider": "openai",
    },
    # Azure OpenAI models
    "azure-gpt-4-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "gpt-4-mini",  # Azure deployment name
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
    "azure-gpt-5-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "gpt-5-mini",  # Azure deployment name
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
    "azure-o3-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "o3-mini",  # Azure deployment name
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
}

TASK_METRICS = {
    "image_classification": "accuracy",
    "text_classification": "accuracy",
    "tabular_classification": "F1",
    "tabular_regression": "RMSLE",
    "tabular_clustering": "RI",
    "node_classification": "accuracy",
    "ts_forecasting": "RMSLE",
}
