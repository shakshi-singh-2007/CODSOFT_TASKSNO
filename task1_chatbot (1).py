# Task 1: Rule-based Chatbot

import re
import random
from datetime import datetime

# Each rule: (pattern to look for, list of possible replies)
RULES = [
    (r"\b(hi|hello|hey)\b",
     ["Hello! I am a chatbot. How can I help you?", "Hi there! How are you?"]),
    (r"\bhow are you\b",
     ["I am doing great, thanks! How about you?"]),
    (r"\b(your name|who are you)\b",
     ["My name is CodBot. I was built for the CodSoft internship."]),
    (r"\btime\b",
     ["__TIME__"]),
    (r"\b(date|today)\b",
     ["__DATE__"]),
    (r"\bpython\b",
     ["Python is an easy and powerful programming language, great for AI!"]),
    (r"\b(ai|artificial intelligence)\b",
     ["AI is about teaching machines to think and learn like humans."]),
    (r"\bhelp\b",
     ["You can ask me about the time, date, Python or AI. Type 'bye' to exit."]),
    (r"\b(thanks|thank you)\b",
     ["You are welcome! Anything else?"]),
    (r"\b(bye|goodbye|exit|quit)\b",
     ["__EXIT__"]),
]

def get_reply(user_text):
    text = user_text.lower().strip()
    for pattern, replies in RULES:
        if re.search(pattern, text):
            reply = random.choice(replies)
            if reply == "__TIME__":
                return "The time is " + datetime.now().strftime("%I:%M %p")
            if reply == "__DATE__":
                return "Today's date is " + datetime.now().strftime("%d %B %Y")
            return reply
    return "Sorry, I did not understand that. Type 'help' to see what I can do."

def main():
    print("CodBot: Hello! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        reply = get_reply(user)
        if reply == "__EXIT__":
            print("CodBot: Goodbye! See you soon.")
            break
        print("CodBot:", reply)

if __name__ == "__main__":
    main()
