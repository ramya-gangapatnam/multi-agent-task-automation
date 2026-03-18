from app.config import MODEL_NAME, OPENAI_API_KEY

from autogen_ext.models.openai import OpenAIChatCompletionClient


def get_model_client() -> OpenAIChatCompletionClient:
    """
    Create a reusable OpenAI model client for AutoGen agents.
    """
    return OpenAIChatCompletionClient(
        model=MODEL_NAME,
        api_key=OPENAI_API_KEY,
    )