from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import (Base, Word)

if __name__ == '__main__':
    engine = create_engine('sqlite:///hangman_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session = Session()

    # pas = Word(word = 'pass', difficulty = 1)

    session.add()
    session.commit()