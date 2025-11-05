# AutoML Agent with Azure OpenAI

This is an implementation of the [AutoML Agent paper](https://arxiv.org/abs/2410.02958) with support for **Azure OpenAI GPT-4-mini, GPT-5-mini, and o3-mini** models.

AutoML Agent is a multi-agent LLM framework that automates the complete machine learning pipeline, from data exploration to model deployment. The system orchestrates specialized agents to handle distinct phases of AutoML workflows.

## 🌟 Features

- **Multi-Agent Architecture**: Specialized agents for data processing, model selection, and operations
- **Azure OpenAI Integration**: Native support for Azure OpenAI GPT-4-mini, GPT-5-mini, and o3-mini
- **Full Pipeline Automation**: End-to-end ML workflow from data to deployment
- **Multiple Data Modalities**: Support for tabular, image, text, graph, and time-series data
- **Knowledge Retrieval**: Integrated RAG (Retrieval-Augmented Generation) from Kaggle, arXiv, PapersWithCode
- **Code Generation**: Automatic Python code generation for ML pipelines
- **Gradio UI**: Built-in web interface generation

## 🏗️ Architecture

The system consists of four specialized agents:

1. **AgentManager**: Orchestrates the entire workflow using a state machine
2. **DataAgent**: Handles dataset retrieval, preprocessing, and augmentation
3. **ModelAgent**: Performs model selection and hyperparameter optimization
4. **OperationAgent**: Generates and executes Python code for the ML pipeline
5. **PromptAgent**: Parses natural language requirements into structured JSON

## 📋 Prerequisites

- Python 3.11+
- Azure OpenAI account with GPT-4-mini, GPT-5-mini, and/or o3-mini deployments
- (Optional) Kaggle, HuggingFace, and other API keys for dataset/model retrieval

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/alfiansmart/AutoML-Agent.git
cd AutoML-Agent
```

### 2. Create a virtual environment

```bash
conda create --name automl-agent python=3.11
conda activate automl-agent
```

or with venv:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. Set up your API credentials

Edit `configs.py` to add your credentials:

```python
class Configs:
    # Azure OpenAI Configuration
    AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
    AZURE_OPENAI_KEY = "your-azure-api-key"
    AZURE_API_VERSION = "2024-02-15-preview"

    # Optional: Other service keys for enhanced functionality
    HF_KEY = ""  # HuggingFace for dataset/model retrieval
    PWC_KEY = ""  # PapersWithCode for research insights
    SEARCHAPI_API_KEY = ""  # Google search API
    TAVILY_API_KEY = ""  # Tavily search
```

### 2. Update model configurations

The `AVAILABLE_LLMs` dictionary in `configs.py` already includes Azure OpenAI configurations:

```python
AVAILABLE_LLMs = {
    "azure-gpt-4-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "gpt-4-mini",  # Your Azure deployment name
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
    "azure-gpt-5-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "gpt-5-mini",  # Your Azure deployment name
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
    "azure-o3-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "o3-mini",  # Your Azure deployment name
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
}
```

**Important**: Replace `"gpt-4-mini"`, `"gpt-5-mini"`, and `"o3-mini"` with your actual Azure deployment names.

## 📖 Usage

### Basic Example

```python
from agent_manager import AgentManager

# Initialize the AgentManager with Azure OpenAI GPT-5-mini
manager = AgentManager(
    llm='azure-gpt-5-mini',  # Select the Azure GPT-5-mini deployment
    interactive=False,  # Run in non-interactive mode for automated execution
    data_path="path/to/your/dataset.csv"  # Provide the dataset location
)

# Start the AutoML workflow
manager.initiate_chat(  # Launch the AutoML Agent conversation
    prompt="Build a classification model to predict customer churn using this dataset"
)
```

### Using o3-mini for reasoning tasks

```python
from agent_manager import AgentManager

# Use o3-mini for complex reasoning and planning
manager = AgentManager(
    llm='azure-o3-mini',
    interactive=False,
    data_path="data/complex_dataset.csv"
)

manager.initiate_chat(
    prompt="Develop a time-series forecasting model with feature engineering for sales prediction"
)
```

### Advanced Usage

```python
from agent_manager import AgentManager

# Initialize with custom settings
manager = AgentManager(
    llm='azure-gpt-4-mini',  # Use Azure GPT-4-mini for vision-focused workflows
    interactive=True,  # Enable interactive mode for user feedback
    data_path="data/images/",
    n_plan=5,  # Generate 5 different solution plans
    top_k=3,   # Consider top 3 models
    decomp=True  # Enable plan decomposition
)

# Provide a detailed task description
task_description = """
Build a computer vision model for image classification.
Requirements:
- Use transfer learning with pretrained models
- Apply data augmentation
- Optimize for accuracy and inference speed
- Deploy as a Gradio web app
"""

manager.initiate_chat(prompt=task_description)
```

## 📁 Output

Generated code and artifacts are saved in the `agent_workspace/` directory:

- `agent_workspace/exp/{timestamp}.py` - Generated ML pipeline code
- `agent_workspace/logs/` - Execution logs
- `agent_workspace/models/` - Trained models

## 🎯 Supported Tasks

- **Tabular**: Classification, Regression, Clustering
- **Computer Vision**: Image Classification, Object Detection, Segmentation
- **NLP**: Text Classification, NER, Summarization
- **Time Series**: Forecasting, Anomaly Detection
- **Graph**: Node Classification, Link Prediction

## 🔧 Task Metrics

The system automatically selects appropriate metrics based on task type:

```python
TASK_METRICS = {
    "image_classification": "accuracy",
    "text_classification": "accuracy",
    "tabular_classification": "F1",
    "tabular_regression": "RMSLE",
    "tabular_clustering": "RI",
    "node_classification": "accuracy",
    "ts_forecasting": "RMSLE",
}
```

## 🐛 Troubleshooting

### Common Issues

1. **Azure OpenAI Authentication Error**
   - Verify your `AZURE_OPENAI_KEY` and `AZURE_OPENAI_ENDPOINT` in `configs.py`
   - Ensure your Azure subscription has access to the specified models
   - Check that deployment names match your Azure configuration

2. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt --upgrade
   ```

3. **CUDA/GPU Issues**
   - Ensure PyTorch is installed with CUDA support if using GPU
   - Set `CUDA_VISIBLE_DEVICES` environment variable

4. **Kaggle API Authentication**
   - Download kaggle.json from your Kaggle account settings
   - Place it in `~/.kaggle/kaggle.json`
   - Set permissions: `chmod 600 ~/.kaggle/kaggle.json`

## 📚 Documentation

- [AutoML Agent Paper](https://arxiv.org/abs/2410.02958)
- [Original GitHub Implementation](https://github.com/DeepAuto-AI/automl-agent)
- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is based on the original AutoML Agent implementation (CC BY-NC 4.0) and modified to support Azure OpenAI.

## 🙏 Acknowledgments

- Original AutoML Agent paper and implementation by DeepAuto-AI
- Azure OpenAI team for the excellent API and models

## 📧 Contact

For questions or issues, please open an issue on GitHub.

## 🔗 Related Resources

- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [AutoML Resources](https://www.automl.org/)
