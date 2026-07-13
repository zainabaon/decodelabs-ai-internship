# Pybot 🤖

A beginner-friendly Python chatbot that uses dictionary-based intent matching to respond to user input.

## About

Pybot (aka **Nova**) is a **rule-based chatbot** — it does not use machine learning. Instead, it matches sanitized user input against a dictionary of predefined intents (greetings, asking the bot's name, asking how it's doing, asking for help, saying thanks, and saying goodbye) and returns the matching response. This project is a foundational exercise in control flow and dictionary usage in Python.

## Features

- Runs in a continuous loop, prompting the user for input
- Sanitizes input (lowercases and strips whitespace) before matching
- Uses a dictionary (not if-elif chains) to map intents to responses
- Falls back to a default message ("I do not understand.") for unmatched input
- Exits cleanly on commands like `bye` or `exit`
- **Stretch goals implemented:**
  - Gives the bot a personality/name ("Nova")
  - Detects when a user introduces themselves (e.g. "my name is Aisha", "I am Sam", "I'm Alex") and greets them by name
  - Logs the full conversation history with timestamps to `conversation_history.txt`

## How to Run

```bash
python chatbot.py
```

Then type your messages at the `You:` prompt. Type `bye` or `exit` to quit.

## Example

```
Nova: Hello! Type 'help' for options or 'bye' to exit.
You: hi
Nova: Hi there! How can I help?
You: my name is Aisha
Nova: Nice to meet you, Aisha!
You: bye
Nova: Goodbye! Thanks for chatting with me.
```

## Files

- `chatbot.py` — main chatbot program
- `conversation_history.txt` — auto-generated log of conversations (created after first run)

## Notes

This project was built as a foundational AI/control-flow exercise, not a production or ML-based chatbot.
