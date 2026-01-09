from openai import OpenAI

class OpenAILLM:
    def __init__(self):
        self.client = OpenAI()

    def generate(self, message: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",   # ✅ VALID MODEL
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
