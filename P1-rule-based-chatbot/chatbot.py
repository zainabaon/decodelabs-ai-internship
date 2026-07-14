"""A beginner-friendly rule-based chatbot.

This chatbot is a foundational AI/control-flow exercise. It does not use
machine learning. Instead, it uses a dictionary to match user input to
pre-written responses.
"""

from datetime import datetime


BOT_NAME = "Nova"
LOG_FILE = "conversation_history.txt"


responses = {
    "hello": "Hello! Nice to meet you.",
    "hi": "Hi there! How can I help?",
    "hey": "Hey! What would you like to talk about?",
    "what is your name": f"My name is {BOT_NAME}.",
    "who are you": f"I am {BOT_NAME}, a friendly rule-based chatbot.",
    "how are you": "I am running smoothly, thanks for asking!",
    "help": "You can say hello, ask my name, ask how I am, or type bye to exit.",
    "thanks": "You are welcome!",
    "thank you": "You are very welcome!",
    "bye": "Goodbye! Thanks for chatting with me.",
    "exit": "Goodbye! Thanks for chatting with me.",
}


def log_message(speaker, message):
    """Save each message to a simple text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {speaker}: {message}\n")


def get_name_reply(user_input):
    """Detect simple name introductions like 'my name is Aisha'."""
    name_starters = ["my name is ", "i am ", "i'm "]

    for starter in name_starters:
        if user_input.startswith(starter):
            name = user_input.replace(starter, "", 1).strip().title()

            if name:
                return f"Nice to meet you, {name}!"

    return None


def main():
    """Run the chatbot until the user chooses to exit."""
    print(f"{BOT_NAME}: Hello! Type 'help' for options or 'bye' to exit.")

    while True:
        user_input = input("You: ")

        # Sanitize the input before matching it to dictionary keys.
        user_input = user_input.lower().strip()
        log_message("You", user_input)

        # Stretch goal: detect a user's name before using the dictionary.
        name_reply = get_name_reply(user_input)

        if name_reply:
            bot_response = name_reply
        else:
            bot_response = responses.get(user_input, "I do not understand.")

        print(f"{BOT_NAME}: {bot_response}")
        log_message(BOT_NAME, bot_response)

        # Exit after printing the goodbye message.
        if user_input in ["bye", "exit"]:
            break


if __name__ == "__main__":
    main()
