def get_reply(message):
    """Takes the user's message and returns the bot's reply."""
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm PyBot, a simple chatbot."
    elif message == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can answer."


def main():
    print("=== SIMPLE CHATBOT ===")
    print("Type 'bye' to exit. Type 'help' to see what I can answer.\n")

    while True:
        user_message = input("You: ")

        if user_message.strip() == "":
            print("Bot: Please type something.")
            continue

        reply = get_reply(user_message)
        print("Bot:", reply)

        if user_message.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()