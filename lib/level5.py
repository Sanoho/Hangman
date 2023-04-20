import random, os
from db.models import Word, Base, Score
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import level1

white = "\033[1;37;40m"
red = "\033[1;31;40m"
yellow = "\033[1;33;40m"
green = "\033[1;32;40m"
magenta = "\033[1;35;40m"
loser = ["hangman11.txt", "hangman22.txt"]
congrats = ["congrats1.txt", "congrats2.txt"]

engine = create_engine('sqlite:///hangman_app.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
def level5_words():
    word_list = []
    for word in session.query(Word).where(Word.difficulty == 5):
        word_list.append(word.word)
    random_word = random.choice(word_list)
    return random_word.upper()

def play_game(word, user, leaderboard, animator):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    score = 20
    print(f"{magenta}Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input(f"{magenta}Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{yellow}You already guessed the letter", f"{white}{guess}")
            elif guess not in word:
                print(f"{white}{guess}", f"{red}is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"{green}Good job,", f"{white}{guess}", f"{green}is in the word!")
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
                print(f"{yellow}You already guessed the word", f"{white}{guess}")
            elif guess != word:
                print(f"{white}{guess}", f"{red}is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print(f"{red}Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        total_score = tries * score
        level1.highscore.append(total_score)
        points = sum([score for score in level1.highscore])     
        if input(f"{green}CONGRATS YOU WON THE GAME WITH THE SCORE OF {white}{points}{green}!!\n{magenta}Play Again? ({green}Y{magenta}/{red}N{magenta}) ").upper() == "Y":
            level1.main()
        else:
            animator(congrats, delay = 1, repeat = 6)
    else:
        print(f"{red}Sorry, you ran out of tries. The word was " + f"{white}{word}" + f"{red}. Maybe next time!")
        points = sum([score for score in level1.highscore])
        print(points)
        if input(f"{magenta}\nDo you want to play again?").upper() == "Y":
            level1.main()
            level1.highscore = []
        else:
            score = Score(score = points, user_id = user.id, leaderboard_id = leaderboard.id)
            session.add(score)
            session.commit()
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

def main(user, leaderboard, animator):
    word = level5_words()
    play_game(word, user, leaderboard, animator)