from llm.ollama_client import OllamaClient
from services.prompt_builder import PromptBuilder
from services.response_parser import ResponseParser
import logging

logger = logging.getLogger(__name__)

class CategorizationAgent:

    def __init__(self):

        self.llm = OllamaClient()
        self.prompt_builder = PromptBuilder()
        self.parser = ResponseParser()

    def categorize(self, transaction, company_context):

        prompt = self.prompt_builder.build(
            transaction,
            company_context
        )

        llm_response = self.llm.generate(prompt)

        print("LLM RAW RESPONSE:")
        print(llm_response)

        result = self.parser.parse(llm_response)

        return result