# from db.score import Score
# from db.user import User
# from db.words import Words
import os, time, sys

class Hangman():
    os.system('clear')
    hangman = ["hangman11.txt", "hangman22.txt"]

    def animator(filenames, delay = 1, repeat = 10):
        frames = []
        for name in filenames:
            with open (name, 'r', encoding = 'utf8') as f:
                frames.append(f.readlines())
        for i in range(repeat):
            for frame in frames:
                print(''.join(frame))
                time.sleep(delay)
                os.system('clear')
    animator(hangman, delay = 1.0, repeat = 4)

    message = """Welcome to Hangman!
Hangman is a classic word game in which you must guess as many secret words as you can before you run out of lives!\n"""
    def title_typewriter(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    title_typewriter(message)

    ask_name = "Please enter your username:\n"
    def prompt_username(ask_name):
        for char in ask_name:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    prompt_username(ask_name)

    username = input()
    def input_username(username):
        welcome_message = f"Welcome, {username}!\nAre you ready to start?\n(yes/no)"
        for char in welcome_message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        if welcome_message == "yes":
            print("plays the game")
        else:
            return prompt_username(ask_name)

    input_username(username)


# GET WORD FUNC

# PLAY FUNC

# DISPLAY STAGES OF HANGMAN FUNC

# def display_hangman(tries):
#     stages = [  # final state: head, torso, both arms, and both legs
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     /|\
#                    |      |
#                    |     / \
#                    -
#                 """,
#                 # head, torso, both arms, and one leg
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     /|\
#                    |      |
#                    |     / 
#                    -
#                 """,
#                 # head, torso, and both arms
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     /|\
#                    |      |
#                    |      
#                    -
#                 """,
#                 # head, torso, and one arm
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     /|
#                    |      |
#                    |     
#                    -
#                 """,
#                 # head and torso
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |      |
#                    |      |
#                    |     
#                    -
#                 """,
#                 # head
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |    
#                    |      
#                    |     
#                    -
#                 """,
#                 # initial empty state
#                 """
#                    --------
#                    |      |
#                    |      
#                    |    
#                    |      
#                    |     
#                    -
#                 """
#     ]
#     return stages[tries]

# MAIN FUNC