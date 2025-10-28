import time
import logging
from azure_openai_client import test_chat, test_embedding

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ModelTester")

def run_chat_tests():
    prompts = [
        "What is the capital of France?",
        "Explain quantum computing in simple terms.",
        "Write a poem about GenTech Inc. using AI."
    ]

    for prompt in prompts:
        logger.info(f"\nTesting prompt: {prompt}")
        start = time.time()
        response = test_chat(prompt)
        end = time.time()

        content = response.choices[0].message.content
        usage = response.usage

        print("\n--- Chat Output ---")
        print(content)
        print("\n--- Stats ---")
        print(f"Prompt Tokens: {usage.prompt_tokens}")
        print(f"Completion Tokens: {usage.completion_tokens}")
        print(f"Total Tokens: {usage.total_tokens}")
        print(f"Response Time: {round(end - start, 2)} seconds\n")


def run_embedding_test():
    sample_texts = [
        "AI is transforming every industry.",
        "GenTech is building intelligent systems.",
    ]

    for text in sample_texts:
        logger.info(f"Generating embedding for: '{text}'")
        start = time.time()
        response = test_embedding(text)
        end = time.time()

        vector = response.data[0].embedding[:5]  # Print first 5 dimensions
        print("\n--- Embedding Sample ---")
        print(vector)
        print(f"Response Time: {round(end - start, 2)} seconds\n")


if __name__ == "__main__":
    print("🔍 Running Chat Model Tests")
    run_chat_tests()
    print("📊 Running Embedding Tests")
    run_embedding_test()
