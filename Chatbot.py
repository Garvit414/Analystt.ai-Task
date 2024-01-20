from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("SimpleBot")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

def get_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

print("SimpleBot: Hi there! I'm SimpleBot. You can start chatting with me. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("SimpleBot: Goodbye!")
        break

    response = get_response(user_input)
    print("SimpleBot:", response)
