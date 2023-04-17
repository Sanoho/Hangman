from sqlalchemy import (Column, String, Integer)
from sqlalchemy.ext.declarative import (declarative_base)

Base = declarative_base()

class Leaderboard(Base):     
    __tablename__ = 'leaderboard'

    id = Column('id', Integer, primary_key = True)
    username = Column('username', String)
    score = Column('score', Integer)

    def __init__(self, username, score) -> None:
        self.username = username
        self.score = score

    def __repr__(self):
        return f'Id: {self.id}, ' \
            f'Username {self.username}, ' \
            f'Score {self.score}, ' \
            