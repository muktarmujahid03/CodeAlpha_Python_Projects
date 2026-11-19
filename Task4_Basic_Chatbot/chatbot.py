def get_reply(message):
    message = message.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi! Nice to meet you."

    elif "how are you" in message:
        return "I'm fine, thanks! How can I help you?"

    elif "your name" in message:
        return "I'm a simple Python rule-based chatbot."

    elif "help" in message:
        return "You can greet me, ask how I am, or say bye."

    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day."

    else:
        return "I don't understand that yet. Try saying hello or asking how I am."


def main():
    print("\n=== BASIC PYTHON CHATBOT ===")
    print("Type 'bye' to end the conversation.")

    while True:
        user_message = input("\nYou: ")
        reply = get_reply(user_message)

        print("Bot:", reply)

        if user_message.strip().lower() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    main()
