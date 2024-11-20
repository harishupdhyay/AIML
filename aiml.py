import aiml

# Initialize chatbot
bot = aiml.Kernel()
bot.learn("chatbot.aiml")

# Chat loop
while True:
    user_input = input("You: ")
    print("Bot:", bot.respond(user_input))
