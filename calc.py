import random

allProjects = [
    "Ruth & Aaron A - rock paper scissors", 
    "Ryan & Susan & Rosaly - tic tac toe", 
    "Victor & Arian & Dyllon - Hangman", 
    "Sonia & Razeen - message encrypter", 
    "Alice & Savitha - Twilio API", 
    "James & Daniel - Covid-19 API", 
    "Samira & Khadijah - magic 8 ball"
]

random.shuffle(allProjects)

for group in allProjects:
    print(group)