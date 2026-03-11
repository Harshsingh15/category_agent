class LLMClient:

    def generate(self, prompt: str):
        raise NotImplementedError("Subclasses must implement generate()")