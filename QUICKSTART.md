# QuickStart Guide - AutoML Agent with Azure OpenAI

This guide will help you get started with AutoML Agent using Azure OpenAI in under 5 minutes.

## Step 1: Install Dependencies

```bash
# Create virtual environment
conda create --name automl-agent python=3.11
conda activate automl-agent

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Configure Azure OpenAI

1. **Get your Azure OpenAI credentials:**
   - Go to [Azure Portal](https://portal.azure.com)
   - Navigate to your Azure OpenAI resource
   - Copy the endpoint URL and API key

2. **Edit `configs.py`:**

```python
class Configs:
    # Replace with your actual values
    AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
    AZURE_OPENAI_KEY = "your-api-key-here"
    AZURE_API_VERSION = "2024-02-15-preview"
```

3. **Update deployment names in `AVAILABLE_LLMs`:**

```python
AVAILABLE_LLMs = {
    "azure-gpt-4-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "your-gpt4-mini-deployment-name",  # ← Change this
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
    "azure-o3-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "your-o3-mini-deployment-name",  # ← Change this
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
}
```

## Step 3: Run Your First AutoML Task

Create a file `my_first_automl.py`:

```python
from agent_manager import AgentManager

# Initialize with Azure GPT-4-mini
manager = AgentManager(
    llm='azure-gpt-4-mini',
    interactive=False,
    data_path="path/to/your/data.csv"
)

# Start AutoML
manager.initiate_chat(
    prompt="Build a classification model for this dataset"
)
```

Run it:

```bash
python my_first_automl.py
```

## Step 4: Check Results

Your generated code will be in:
- `agent_workspace/exp/` - Generated Python code
- `agent_workspace/logs/` - Execution logs

## 🎯 What Just Happened?

The AutoML Agent:
1. ✅ Analyzed your dataset
2. ✅ Retrieved relevant knowledge from Kaggle, arXiv, PapersWithCode
3. ✅ Generated multiple ML solution plans
4. ✅ Selected the best models
5. ✅ Created executable Python code
6. ✅ Validated the solution

## 🚀 Next Steps

### Try Different Tasks

**Image Classification:**
```python
manager = AgentManager(llm='azure-o3-mini', data_path="images/")
manager.initiate_chat("Build an image classifier with transfer learning")
```

**Time Series Forecasting:**
```python
manager = AgentManager(llm='azure-gpt-4-mini', data_path="sales.csv")
manager.initiate_chat("Forecast sales for the next 30 days")
```

**Text Classification:**
```python
manager = AgentManager(llm='azure-o3-mini', data_path="reviews.csv")
manager.initiate_chat("Build a sentiment analysis model")
```

### Advanced Features

**Generate Multiple Plans:**
```python
manager = AgentManager(
    llm='azure-gpt-4-mini',
    n_plan=5,  # Generate 5 different solution approaches
    top_k=3    # Consider top 3 models
)
```

**Interactive Mode:**
```python
manager = AgentManager(
    llm='azure-gpt-4-mini',
    interactive=True  # Ask for user feedback during process
)
```

**Detailed Planning:**
```python
manager = AgentManager(
    llm='azure-o3-mini',
    decomp=True  # Enable detailed plan decomposition
)
```

## 🔧 Optional: Set Up Additional Services

For enhanced functionality, configure these optional services:

### Kaggle (for dataset retrieval)
```bash
# Download kaggle.json from https://www.kaggle.com/settings
mkdir ~/.kaggle
mv kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### HuggingFace (for models/datasets)
```python
# In configs.py
HF_KEY = "your_huggingface_token"
```

## 💡 Tips

1. **Start Simple**: Begin with small datasets to test the system
2. **Clear Prompts**: Be specific about what you want (e.g., "optimize for accuracy" vs "optimize for speed")
3. **Monitor Costs**: Azure OpenAI charges per token - use GPT-4-mini for cost efficiency
4. **Use o3-mini**: For complex reasoning tasks requiring multi-step planning
5. **Check Logs**: Review `agent_workspace/logs/` if something goes wrong

## 🐛 Common Issues

**"Authentication failed"**
- Double-check your Azure credentials in `configs.py`
- Verify your deployment names match Azure

**"Model not found"**
- Ensure deployment names in `configs.py` match your Azure deployments
- Check that your Azure subscription has access to the models

**"No module named..."**
- Run: `pip install -r requirements.txt --upgrade`

## 📚 Learn More

- See `README.md` for comprehensive documentation
- Check `example_usage.py` for more examples
- Read the [AutoML Agent paper](https://arxiv.org/abs/2410.02958)

## 🎉 You're Ready!

Start automating your ML workflows with AutoML Agent and Azure OpenAI! 🚀
