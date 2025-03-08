from langchain_ollama import ChatOllama


class Chatbot:
    def __init__(self, model='gemma2:27b', temperature=0.7, personality='Friendly'):
        self.model = model
        self.temperature = temperature
        self.personality = personality
        self._chatbot = ChatOllama(model=self.model, temperature=self.temperature)
    
    def set_temperature(self, temperature):
        self.temperature = temperature
        self._chatbot = ChatOllama(model=self.model, temperature=self.temperature)
    
    def set_personality(self, personality):
        self.personality = personality
    
    def get_personality_prompt(self):
        prompts = {
            "Friendly": "Respond in a warm, helpful, and engaging manner.",
            "Professional": "Provide clear, concise, and formal responses.",
            "Sarcastic": "Respond with a witty, humorous, and slightly sarcastic tone.",
            "Encouraging": "Be positive, motivational, and supportive in responses.",
            "Direct": "Give straightforward, no-nonsense responses."
        }
        return prompts.get(self.personality, "Respond normally.")
    
    def invoke(self, messages):
        system_message = {"role": "system", "content": self.get_personality_prompt()}
        messages.insert(0, system_message)  # Ensure the system message is included
        return self._chatbot.invoke(messages).content
