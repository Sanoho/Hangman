import random, os
from db.models import Word, Base, Score
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import level2

white = "\033[1;37;49m"
red = "\033[1;31;49m"
yellow = "\033[1;33;49m"
green = "\033[1;32;49m"
magenta = "\033[1;35;49m"
loser = ["hangman11.txt", "hangman22.txt"]
congrats = ["congrats1.txt", "congrats2.txt"]
troll = ["hangman22.txt"]

engine = create_engine('sqlite:///hangman_app.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

def impossible():
    word_list = []
    for word in session.query(Word).where(Word.difficulty == 99):
        word_list.append(word.word)
    random_word = random.choice(word_list)
    return random_word.upper()

def play_game(word, user, animator):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    score = 15
    print(f"{magenta}\nAre you ready word-master (LOL)?!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input(f"{magenta}Make your guess boy: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{yellow}What? Is your memory that bad? You already guessed", f"{white}{guess}.")
            elif guess not in word:
                print(f"{red}C'mon... Why would you guess {white}{guess}?!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"{green}What luck,", f"{white}{guess}", f"{green}is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"{yellow}C'mon old man, you already guessed that word", f"{white}{guess}.")
            elif guess != word:
                print("HAHAHA",f"{white}{guess}", f"{red}is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print(f"{red}Seriously?!?! Follow the rules and guess a letter or word.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print(f"{green}What?!?! You must have cheated!")
        points = tries * score
        print(f"{magenta}Your score was {green}{points}")
        if input(f"{magenta}\nCan you do it again?... I doubt it. ").upper() == "Y":
            os.system('clear')
            main(user, animator)
        else:
            score = Score(score = points, user_id = user.id, leaderboard_id = level2.leaderboard.id)
            session.add(score)
            session.commit()
            animator(congrats, delay = 1, repeat = 3)
            animator(troll, delay = 1, repeat = 2)
    else:
        print(f"{red}I thought you were the word-master, the word was " + f"{white}{word}" + f"{red}. Horrible!")
        if input(f"{magenta}\nWant to try again loser??").upper() == "Y":
            os.system('clear')
            main(user, animator)
        else:
            os.system("clear")
            animator(loser, delay = 2, repeat = 1)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                f"""{red}
                --------    
                |      |    
                |      O    
                |     \|/   
                |      |    
                |     d b   
                -           """
     f"""{white}            """,        
                # head, torso, both arms, and one leg
                f"""{red}
                --------    
                |      |    
                |      O    
                |     \|/   
                |      |    
                |     d     
                -           """
     f"""{white}            """,       
                # head, torso, and both arms
                f"""{yellow}
                --------    
                |      |    
                |      O    
                |     \|/   
                |      |    
                |           
                -           """
     f"""{white}            """,        
                # head, torso, and one arm
                f"""{yellow}
                --------    
                |      |    
                |      O    
                |     /|    
                |      |    
                |           
                -           """
     f"""{white}            """,     
                # head and torso
                f"""{yellow}
                --------    
                |      |    
                |      O    
                |      |    
                |      |    
                |           
                -           """
     f"""{white}            """,    
                # head
                f"""{green}
                --------    
                |      |    
                |      O    
                |           
                |           
                |           
                -           """
     f"""{white}            """,    
                # initial empty state
                f""" {green}
                --------    
                |      |    
                |           
                |           
                |           
                |           
                -           
                            """
     f"""{white}            """,
    ]
    return stages[tries]

def main(user, animator):
    word = impossible()
    play_game(word, user, animator)