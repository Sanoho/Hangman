from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Word, Leaderboard, Score
import ipdb
# from db.words import impossible

if __name__ == '__main__':
    engine = create_engine('sqlite:///hangman_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session = Session()

    # pas = Word(word = 'pass', difficulty = 1)

    # for word in level_one_words:
    #     word = Word(word = word, difficulty = 99)
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
    # for word in impossible:
    #     word = Word(word = word, difficulty = 99)
    #     session.add(word)
    #     session.commit()    

    # deleted_words = session.query(Word).filter(Word.difficulty == 3)
    # session.delete(deleted_words)
    # session.commit()

    # l = Leaderboard()
    # session.add(l)
    # session.commit()

    # ------ below is for leaderboard -----
    # pulls up the scores --- uncomment below
    # leaderboard = session.query(Leaderboard).first()

    # orders the leaderboard by highest  --- don't uncomment this
    # scores = session.query(Score).order_by(Score.score.desc()).limit(3)
    # ------ above is for the leaderboard ------- uncomment above

ipdb.set_trace()