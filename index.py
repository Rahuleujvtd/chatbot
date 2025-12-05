

responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hello there! What can I do for you?",
    "how are you": "I am fine, thank you! How are you?",
    "what is your name": "I am RahulBot, your friendly chatbot.",
    "bye": "Bye! Have a nice day!"
}

print("==== Welcome to RahulBot ====")
print("Type 'bye' to exit\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in responses:
        print(f"Bot: {responses[user_input]}")
        if user_input == "bye":
            break
    else:
        print("Bot: Sorry, I didn't understand that. Try another question.")
