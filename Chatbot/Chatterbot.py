#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import nltk
import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()

#Create a chatbot
bot = ChatBot('Friend')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

#chat feature
def main():
    while True:
        message = input('\t\t\tYou:')
        if message.strip() != 'Bye':
            reply = bot.get_response(message)
            print('Friend:',reply)
        if message.strip() ==' Bye':
            print('Friend: Bye')
            break
main()