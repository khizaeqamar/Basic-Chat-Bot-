# ========== CHAT BOT ==========
print("=== WELCOME TO CHATBOT ===")
print("You can ask me basic questions. Type 'bye' to exit.\n")

# ---------- Memory Creation ----------
responses = {
    "hello": "Hi! Welcome to the ChatBot. How can I help you?",
    "how are you": "I am very fine, thanks for asking.",
    "who are you": "I am a smart AI chatbot created using Python.",
    "what is your name": "I am an AI ChatBot.",
    "what is python": "Python is a popular programming language used in web development, data science, AI, and more."
}


# ---------- Response Function ----------
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()

    for key in responses:
        if key in userQuestion:
            return responses[key]

    return "I am not able to answer this yet. I am still learning."


# ---------- Main Chat Loop ----------
while True:
    userInput = input("You: ")

    # Exit condition
    if userInput.lower() in ["bye", "exit"]:
        print("Bot: Goodbye! 👋")
        break

    reply = getResponseOfBot(userInput)
    print("Bot:", reply)
