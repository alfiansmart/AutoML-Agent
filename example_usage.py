"""
AutoML Agent Example Usage with Azure OpenAI

This script demonstrates how to use the AutoML Agent with Azure OpenAI GPT-4-mini and o3-mini.
"""

from agent_manager import AgentManager

def example_tabular_classification():
    """
    Example: Tabular data classification task
    """
    print("\n" + "="*80)
    print("Example 1: Tabular Classification with Azure GPT-4-mini")
    print("="*80 + "\n")

    manager = AgentManager(
        llm='azure-gpt-4-mini',  # Use Azure GPT-4-mini
        interactive=False,
        data_path="data/tabular/customer_churn.csv"  # Replace with your data path
    )

    prompt = """
    Build a classification model to predict customer churn.
    Requirements:
    - Use the best performing gradient boosting models
    - Apply feature engineering and selection
    - Optimize for F1 score
    - Include model evaluation metrics
    """

    manager.initiate_chat(prompt=prompt)


def example_image_classification():
    """
    Example: Image classification with transfer learning
    """
    print("\n" + "="*80)
    print("Example 2: Image Classification with Azure o3-mini")
    print("="*80 + "\n")

    manager = AgentManager(
        llm='azure-o3-mini',  # Use Azure o3-mini for complex reasoning
        interactive=False,
        data_path="data/images/"
    )

    prompt = """
    Build a computer vision model for image classification.
    Requirements:
    - Use transfer learning with pretrained models (ResNet, EfficientNet)
    - Apply data augmentation techniques
    - Optimize for both accuracy and inference speed
    - Create a Gradio web app for deployment
    """

    manager.initiate_chat(prompt=prompt)


def example_time_series_forecasting():
    """
    Example: Time series forecasting
    """
    print("\n" + "="*80)
    print("Example 3: Time Series Forecasting with Azure GPT-4-mini")
    print("="*80 + "\n")

    manager = AgentManager(
        llm='azure-gpt-4-mini',
        interactive=False,
        data_path="data/timeseries/sales_data.csv",
        n_plan=3,  # Generate 3 different solution plans
        top_k=2    # Consider top 2 models
    )

    prompt = """
    Develop a time-series forecasting model for sales prediction.
    Requirements:
    - Feature engineering with lag features and rolling statistics
    - Consider both traditional (ARIMA, Prophet) and ML approaches
    - Optimize for RMSLE metric
    - Handle seasonality and trends
    """

    manager.initiate_chat(prompt=prompt)


def example_nlp_text_classification():
    """
    Example: NLP text classification
    """
    print("\n" + "="*80)
    print("Example 4: Text Classification with Azure o3-mini")
    print("="*80 + "\n")

    manager = AgentManager(
        llm='azure-o3-mini',
        interactive=False,
        data_path="data/text/reviews.csv"
    )

    prompt = """
    Build a text classification model for sentiment analysis.
    Requirements:
    - Use pretrained transformers (BERT, RoBERTa)
    - Apply text preprocessing and tokenization
    - Fine-tune on the provided dataset
    - Optimize for accuracy
    - Create visualization of model predictions
    """

    manager.initiate_chat(prompt=prompt)


def example_with_custom_dataset():
    """
    Example: Using AutoML Agent with custom dataset from URL
    """
    print("\n" + "="*80)
    print("Example 5: Custom Dataset from URL")
    print("="*80 + "\n")

    manager = AgentManager(
        llm='azure-gpt-4-mini',
        interactive=False,
        data_path="https://example.com/dataset.csv"
    )

    prompt = """
    Analyze this dataset and build the most appropriate ML model.
    Let the AutoML Agent determine:
    - The type of problem (classification, regression, clustering)
    - Best preprocessing steps
    - Most suitable models
    - Optimal hyperparameters
    """

    manager.initiate_chat(prompt=prompt)


def example_interactive_mode():
    """
    Example: Interactive mode for iterative development
    """
    print("\n" + "="*80)
    print("Example 6: Interactive Mode")
    print("="*80 + "\n")

    manager = AgentManager(
        llm='azure-gpt-4-mini',
        interactive=True,  # Enable interactive mode
        data_path="data/my_dataset.csv",
        n_plan=5,     # Generate more plans for selection
        top_k=3,      # Consider top 3 models
        decomp=True   # Enable detailed plan decomposition
    )

    prompt = """
    Build a comprehensive ML solution for my dataset.
    I want to:
    1. Explore the data thoroughly
    2. Try multiple modeling approaches
    3. Get explanations for model decisions
    4. Deploy the best model
    """

    manager.initiate_chat(prompt=prompt)


def main():
    """
    Main function to run examples

    Uncomment the example you want to run
    """
    print("\n" + "="*80)
    print("AutoML Agent Examples with Azure OpenAI")
    print("="*80)

    # Run examples (uncomment the one you want to try)

    # Example 1: Tabular Classification
    example_tabular_classification()

    # Example 2: Image Classification
    # example_image_classification()

    # Example 3: Time Series Forecasting
    # example_time_series_forecasting()

    # Example 4: NLP Text Classification
    # example_nlp_text_classification()

    # Example 5: Custom Dataset from URL
    # example_with_custom_dataset()

    # Example 6: Interactive Mode
    # example_interactive_mode()


if __name__ == "__main__":
    main()
