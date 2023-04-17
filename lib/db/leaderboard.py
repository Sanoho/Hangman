from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.ext.declarative import (declarative_base)

Base = declarative_base()

class Leaderboard(Base):     
    __tablename__ = 'leaderboard'

    id = Column('id', Integer, primary_key = True)
    username = Column(Integer, ForeignKey('user.id'))
    score = Column(Integer, ForeignKey('score.id'))

    def __init__(self, username, score) -> None:
        self.username = username
        self.score = score

    def __repr__(self):
        return f'Id: {self.id}, ' \
            f'Username {self.username}, ' \
            f'Score {self.score}, ' \
