def chatbot():
    responses = {
        "hello": "Hi, welcome! How can I help you?",
        "how are you": "I'm doing great! Thanks for asking!",
        "who are you": "I’m a simple chatbot created  with Python.",
        "motivate me": "Keep pushing! You're doing amazing 👌",
        "happy": "Love to hear that!",
        "functions kya hote hai": "Functions ek reusable block of code hote hain 😄",
    }

    print("Chatbot ready! Type 'exit' or 'bye' to stop.\n")

    while True:
        userInput = input("YOU: ").lower().strip()

        # Exit condition
        if userInput in ["bye", "exit"]:
            print("BOT: Bye! Take care 👋")
            break

        print("\n------------------")

        if userInput in responses:
            print("BOT:", responses[userInput])
        else:
            print("BOT: Sorry, I don't understand:", userInput)

        print("------------------\n")


# Run chatbot
chatbot()
