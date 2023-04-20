import level1
import os, time, sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, User

engine = create_engine('sqlite:///hangman_app.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

white = "\033[1;37;40m"
red = "\033[1;31;40m"
yellow = "\033[1;33;40m"
green = "\033[1;32;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"

os.system('clear')
hangman = ["hangman11.txt", "hangman22.txt"]


def animator(filenames, delay = 1, repeat = 4):
    frames = []
    for name in filenames:
        with open (name, 'r', encoding = 'utf8') as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print(''.join(frame))
            time.sleep(delay)
            os.system('clear')

animator(hangman, delay = 1.0, repeat = 3)

message = f"""\t\t\t\t\t\t\t\t {green}WELCOME {magenta}TO {green}H{red}A{yellow}N{cyan}G{white}M{magenta}A{green}N{red}!\n
\t\t{white}Hangman is a classic word game in which you must guess as many secret words as you can before you run out of lives!\n"""

def title_typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
title_typewriter(message)

ask_name = f"\n{magenta}Please enter your username:\n"
def prompt_username(ask_name):
    for char in ask_name:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
prompt_username(ask_name)

username = input(f"{white}")

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
    welcome_message = f"\n{magenta}Welcome," + f"{white} {username}" + f"{magenta}!" + f"{magenta}\n\nAre you ready to start?" + f" {magenta}(" + f"{green}y" + f"{magenta}/" + f"{red}n" + f"{magenta})\n"
    for char in welcome_message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
input_username(username) 

decision = input(f"{white}")

def yes_or_no(decision):
    if decision == "y":
        print(f"{green}Let's start the game!")

while decision != "y":
    prompt_username(ask_name)
    username = input()
    find_or_create_user(username)
    input_username(username)
    decision = input()
    yes_or_no(decision)

level1.main(user)


