import random
from datetime import datetime


class AdvancedChatbot:
    def __init__(self):
        self.name = "ChatBot Pro"
        self.responses = {
            'greetings': {
                'patterns': ['hello', 'hi', 'hey', 'hola', 'good morning', 'good afternoon'],
                'responses': [
                    "Hello there! 👋",
                    "Hi! How can I help you today?",
                    "Hey! Nice to see you!",
                    "Hello! What can I do for you?"
                ]
            },
            'how_are_you': {
                'patterns': ['how are you', 'how do you do', 'how are things'],
                'responses': [
                    "I'm functioning perfectly! How about you?",
                    "I'm just a program, but I'm doing great! How are you?",
                    "All systems operational! How can I assist you?"
                ]
            },
            'name': {
                'patterns': ['what is your name', 'who are you', 'your name'],
                'responses': [
                    f"I'm {self.name}, your friendly chatbot assistant!",
                    "You can call me ChatBot Pro! 🤖",
                    f"My name is {self.name}! Nice to meet you!"
                ]
            },
            'joke': {
                'patterns': ['tell me a joke', 'joke', 'make me laugh'],
                'responses': [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "Why did the scarecrow win an award? He was outstanding in his field!",
                    "What do you call a fake noodle? An impasta! 😄"
                ]
            },
            'time': {
                'patterns': ['what time is it', 'time', 'current time'],
                'responses': ["The current time is {time}"]
            }
        }

    def get_response(self, user_input):
        """Get an appropriate response based on user input"""
        user_input = user_input.lower().strip()

        # Check each category
        for category, data in self.responses.items():
            for pattern in data['patterns']:
                if pattern in user_input:
                    if category == 'time':
                        current_time = datetime.now().strftime("%H:%M:%S")
                        return data['responses'][0].format(time=current_time)
                    return random.choice(data['responses'])

        # Default response
        return "I'm not sure how to respond to that. Try asking me something else!"

    def chat(self):
        """Main chat loop"""
        print(f"🤖 {self.name}: Hello! I'm an advanced chatbot. Type 'quit' to exit.")
        print("Type 'help' to see what I can do!")

        while True:
            user_input = input("👤 You: ")

            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"🤖 {self.name}: Goodbye! Have a wonderful day! 👋")
                break

            if user_input.lower() == 'help':
                self.show_help()
                continue

            response = self.get_response(user_input)
            print(f"🤖 {self.name}: {response}")

    def show_help(self):
        """Show available commands"""
        print(f"\n🤖 {self.name}: I can respond to:")
        print("-" * 30)
        for category, data in self.responses.items():
            print(f"• {', '.join(data['patterns'][:2])}...")
        print("• help - Show this help message")
        print("• quit - Exit the chat")
        print()


# Run the advanced chatbot
if __name__ == "__main__":
    bot = AdvancedChatbot()
    bot.chat()