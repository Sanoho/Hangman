import random
from db.models import Word, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import level3

def level2_words():
    engine = create_engine('sqlite:///hangman_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session = Session()
    word_list = []
    for word in session.query(Word).where(Word.difficulty == 2):
        word_list.append(word.word)
    random_word = random.choice(word_list)
    return random_word.upper()

def play_game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
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
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                --------
                |      |
                |      O
                |     \|/
                |      |
                |     d b
                -
                """,
                # head, torso, both arms, and one leg
                """
                --------
                |      |
                |      O
                |     \|/
                |      |
                |     d 
                -
                """,
                # head, torso, and both arms
                """
                --------
                |      |
                |      O
                |     \|/
                |      |
                |      
                -
                """,
                # head, torso, and one arm
                """
                --------
                |      |
                |      O
                |     /|
                |      |
                |     
                -
                """,
                # head and torso
                """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
                """,
                # head
                """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                """,
                # initial empty state
                """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
                """
    ]
    return stages[tries]

def main():
    word = level2_words()
    play_game(word)
    while input("Are you ready for the next level? ").upper() == "Y":
        level3.main()


if __name__ == "__main__":
    main()