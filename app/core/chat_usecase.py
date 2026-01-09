class ChatUseCase:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def execute(self, message: str) -> str:
        return self.llm_client.generate(message)
