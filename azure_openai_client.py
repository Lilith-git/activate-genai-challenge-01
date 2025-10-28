import os
import logging
from typing import List
from dotenv import load_dotenv
from openai import AzureOpenAI
from openai.types.chat import ChatCompletion
from openai.types.embedding import Embedding

# Load .env variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GenTechAI")

# Initialize client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# Get deployment names
CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")


def test_chat(prompt: str) -> ChatCompletion:
    try:
        response = client.chat.completions.create(
            model=CHAT_DEPLOYMENT,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200,
        )
        logger.info("Chat response received.")
        return response
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise


def test_embedding(text: str) -> Embedding:
    try:
        response = client.embeddings.create(
            model=EMBEDDING_DEPLOYMENT,
            input=text,
        )
        logger.info("Embedding generated.")
        return response
    except Exception as e:
        logger.error(f"Embedding error: {e}")
        raise
