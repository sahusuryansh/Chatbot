import re

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    # Rule 1: Greetings
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I help you today?"
    
    # Rule 2: Asking for name
    elif re.search(r"(your name|who are you)", user_input):
        return "I'm a simple rule-based chatbot."
    
    # Rule 3: Asking about weather
    elif "weather" in user_input:
        return "I'm not connected to the internet, but I hope the weather is nice!"
    
    # Rule 4: Saying goodbye
    elif re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return "Goodbye! Have a great day!"
    
    # Rule 5: Asking for help
    elif "help" in user_input:
        return "Sure, I'm here to help! What do you need assistance with?"
    
    # Default response
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if re.search(r"\b(bye|goodbye|see you)\b", user_input.lower()):
            break