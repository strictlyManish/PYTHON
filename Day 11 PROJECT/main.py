responses = {
        "hello": "Hi, welcome! How can I help you?",
        "how are you": "I'm doing great! Thanks for asking!",
        "who are you": "I’m a simple chatbot created  with Python.",
        "motivate me": "Keep pushing! You're doing amazing 👌",
        "happy": "Love to hear that!",
        "functions kya hote hai": "Functions ek reusable block of code hote hain 😄",
}



while True:
    userInput = input('Ask : - ').lower().strip()

    print('YOU : - ',userInput)

    if userInput in ['bye','bas kar']:
        print('Good by')
        break

    if userInput in responses:
        print('BOT: - ',responses[userInput])
    else:
        print('BOT not able to answer')    


