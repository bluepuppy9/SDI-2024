from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train('chatterbot.corpus.english')

# Start the conversation loop
print('ChatBot: Hello! How can I help you today?')

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        print('ChatBot: Goodbye!')
        break
    response = chatbot.get_response(user_input)
    print('ChatBot:', response)