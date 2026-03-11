import json
import re


class ResponseParser:

    def parse(self, response_text):

        try:

            cleaned = response_text.replace("```json", "").replace("```", "")

            match = re.search(r'\{[\s\S]*\}', cleaned)

            if match:
                json_str = match.group()
                return json.loads(json_str)

        except Exception:
            pass

        return {
            "category": "Unknown",
            "confidence": 0,
            "reasoning": "LLM response parsing failed"
        }