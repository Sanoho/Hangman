from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.words import (Base, Word)

if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite:///hangman_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session = Session()

    pas = Word('pass', 1)

    session.add(pas)
    session.commit()