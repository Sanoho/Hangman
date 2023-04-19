from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import (Base, Word)
# from db.words import level_three_words

if __name__ == '__main__':
    engine = create_engine('sqlite:///hangman_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session = Session()

    # pas = Word(word = 'pass', difficulty = 1)

    # for word in level_one_words:
    #     word = Word(word = word, difficulty = 1)
    #     session.add(word)
    #     session.commit()
    # for word in level_two_words:
    #     word = Word(word = word, difficulty = 2)
    #     session.add(word)
    #     session.commit()
    # for word in level_three_words:
    #     word = Word(word = word, difficulty = 3)
    #     session.add(word)
    #     session.commit()
    # for word in level_four_words:
    #     word = Word(word = word, difficulty = 4)
    #     session.add(word)
    #     session.commit()
    # for word in level_five_words:
    #     word = Word(word = word, difficulty = 5)
    #     session.add(word)
    #     session.commit()
        
    # deleted_words = session.query(Word).filter(Word.difficulty == 3)
    # session.delete(deleted_words)
    # session.commit()