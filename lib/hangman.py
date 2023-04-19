import level1
import os, time, sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, User

engine = create_engine('sqlite:///hangman_app.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

os.system('clear')
hangman = ["hangman11.txt", "hangman22.txt"]

# def animator(filenames, delay = 1, repeat = 4):
#     frames = []
#     for name in filenames:
#         with open (name, 'r', encoding = 'utf8') as f:
#             frames.append(f.readlines())
#     for i in range(repeat):
#         for frame in frames:
#             print(''.join(frame))
#             time.sleep(delay)
#             os.system('clear')

# animator(hangman, delay = 1.0, repeat = 3)

# message = """Welcome to Hangman!
# Hangman is a classic word game in which you must guess as many secret words as you can before you run out of lives!\n"""
# def title_typewriter(message):
#     for char in message:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(0.1)
# title_typewriter(message)

ask_name = "Please enter your username:\n"
def prompt_username(ask_name):
    for char in ask_name:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
prompt_username(ask_name)

username = input()
# user = User(username = username)
# session.add(user)
# session.commit()

def find_or_create_user(username):
    user = session.query(User).filter(User.username == username).first()
    if user:
        return user
    else:
        user = User(username = username)
        session.add(user)
        session.commit()
        return user
user = find_or_create_user(username)


def input_username(username):
    welcome_message = f"Welcome, {username}!\nAre you ready to start?\n(y/n)\n"
    for char in welcome_message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    
input_username(username) 

decision = input()

def yes_or_no(decision):
    if decision == "y":
        print("Let's start the game!")

while decision != "y":
    prompt_username(ask_name)
    username = input()
    find_or_create_user(username)
    input_username(username)
    decision = input()
    yes_or_no(decision)

level1.main()


