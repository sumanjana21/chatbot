# Responses for the chatbot
responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm just a program, but I'm functioning perfectly! How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand that. Can you try rephrasing?",
}

def chatbot():
    print("Chatbot: Hello! Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()  # Convert user input to lowercase for consistency
        if user_input in responses:
            print("Chatbot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Chatbot:", responses["default"])
if __name__ == "__main__":
    chatbot()
