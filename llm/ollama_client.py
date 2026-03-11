import requests
from llm.base_client import LLMClient


class OllamaClient(LLMClient):

    def generate(self, prompt: str):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data["response"]