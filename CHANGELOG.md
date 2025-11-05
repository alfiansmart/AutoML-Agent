# Changelog

All notable changes to the AutoML Agent Azure implementation will be documented in this file.

## [0.1.0] - 2024-11-05

### Added

#### Azure OpenAI Integration
- ✨ Native support for Azure OpenAI GPT-4-mini, GPT-5-mini, and o3-mini models
- 🔧 Updated `configs.py` with Azure OpenAI configuration parameters
- 🔧 Modified `utils/get_client()` to support AzureOpenAI client initialization
- 📝 Added provider field to LLM configurations for multi-provider support

#### Core Implementation
- 📦 Implemented complete AutoML Agent framework based on arXiv:2410.02958
- 🤖 AgentManager - State machine for workflow orchestration
- 📊 DataAgent - Dataset retrieval and preprocessing
- 🧠 ModelAgent - Model selection and hyperparameter optimization
- ⚙️ OperationAgent - Code generation and execution
- 💬 PromptAgent - Natural language requirement parsing
- 🔍 Knowledge retrieval from Kaggle, arXiv, PapersWithCode

#### Documentation
- 📚 Comprehensive README.md with usage examples
- 🚀 QUICKSTART.md for fast onboarding
- 📝 example_usage.py with 6 different use cases
- 🔐 .env.example for easy configuration
- 📄 LICENSE file (CC BY-NC 4.0)

#### Dependencies
- 📦 Complete requirements.txt with all necessary packages
- 🎯 Organized dependencies by category (ML, Vision, NLP, etc.)
- 🔗 Added google-search-results, kaggle, num2words utilities

#### Project Structure
- 📁 Created agent_workspace/ for outputs and artifacts
- 📁 Created proper directory structure for all agents
- 🔧 setup.py for package installation
- 🙈 .gitignore for Python, data, and model files

#### Features
- 🎯 Multi-modal support (tabular, image, text, time-series, graph)
- 🔄 Multiple solution plan generation
- 🎨 Gradio UI generation for model deployment
- 📊 Automatic metric selection based on task type
- 🔁 Iterative code refinement with error handling
- 💰 Cost tracking for LLM API calls

### Changed
- 🔄 Modified `get_client()` function to detect and route to Azure OpenAI
- 🔄 Extended `AVAILABLE_LLMs` dictionary structure with provider field

### Technical Details

#### Model Configuration
```python
AVAILABLE_LLMs = {
    "azure-gpt-4-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "gpt-4-mini",  # Azure GPT-4-mini deployment name
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
    "azure-gpt-5-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "gpt-5-mini",  # Azure GPT-5-mini deployment name
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
    "azure-o3-mini": {
        "api_key": Configs.AZURE_OPENAI_KEY,
        "model": "o3-mini",  # Azure o3-mini deployment name
        "endpoint": Configs.AZURE_OPENAI_ENDPOINT,
        "api_version": Configs.AZURE_API_VERSION,
        "provider": "azure",
    },
}
```

#### Client Initialization
- Automatic detection of provider type (Azure, OpenAI, Local)
- Backward compatible with original OpenAI implementation
- Support for custom endpoints via base_url parameter

### Known Issues
- ⚠️ Requires Python 3.11+
- ⚠️ Some features require additional API keys (Kaggle, HuggingFace)
- ⚠️ GPU recommended for image/NLP tasks

### Dependencies
Core dependencies:
- openai>=1.30.2 (includes Azure OpenAI support)
- torch>=2.2.1
- transformers>=4.40.1
- langchain>=0.2.1
- pandas>=2.2.2
- scikit-learn>=1.4.1

See requirements.txt for complete list.

### References
- Paper: [AutoML Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://arxiv.org/abs/2410.02958)
- Original Implementation: [DeepAuto-AI/automl-agent](https://github.com/DeepAuto-AI/automl-agent)

---

## Future Roadmap

### Planned Features (v0.2.0)
- [ ] Support for GPT-4o and other Azure OpenAI models
- [ ] Enhanced error recovery and retry logic
- [ ] Model performance comparison dashboard
- [ ] Export to MLflow for experiment tracking
- [ ] Docker containerization
- [ ] CI/CD pipeline setup
- [ ] Unit tests and integration tests
- [ ] Jupyter notebook examples

### Under Consideration
- [ ] Support for other cloud providers (AWS Bedrock, Google Vertex AI)
- [ ] Web UI for non-programmers
- [ ] AutoML benchmarking suite
- [ ] Model explainability features (SHAP, LIME)
- [ ] Automated dataset quality assessment
- [ ] Multi-objective optimization
- [ ] Federated learning support

---

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Acknowledgments

Thanks to the DeepAuto-AI team for the original AutoML Agent implementation and research.
