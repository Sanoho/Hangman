# from db.score import Score
# from db.user import User
# from db.words import Words
import os, time
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

animator(hangman, delay = 1.0, repeat = 10)

# ANIMATION


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