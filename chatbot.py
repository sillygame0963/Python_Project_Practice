# Import the regular expression module to handle matching
import re
from http.client import responses

# A dictionary that map keywords to predefined responses
responses = {
    "hello": "Hi! I'm a noob chatbot! How can I help you?",
    "hi": "Hi Son! How can I help you today?",
    "How are you?": "I'm fine thank you, and you?",
    "What is your name?": "I don't have a name. I'm just a noob chatbot for real.",
    "help": "I'm here! What do you need?",
    "bye": "See yaaa!",
    "thank you": "You're welcome!",
    "default": "What are you talking about? Say it again!"
}

# Function to find appropriate response based on user's input
def chatbot_res(user_input):
    # Convert user's input to lowercase to match case-insensitive
    user_input = user_input.lower()

    for keywords in responses:
        if re.search(keywords, user_input):
            return responses[keywords]
        else:
            return responses["default"]

# Main function to run the chatbot
def chatbot():
    print("Hi! I'm a noob Chatbot! How can I help you\n (Type 'bye' to exit the conversation)")

    while True:
        # Get user's input
        user_input = input("You: ")

        # If user type 'bye'
        if user_input.lower() == 'bye':
            print("Chatbot: See yaaa!")
            break

        # Chatbot response based on user's input
        responses = chatbot_res(user_input)

        # Print chatbot response
        print(f"Chatbot: {responses}")

chatbot()