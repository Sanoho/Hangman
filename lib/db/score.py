from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, ForeignKey)
from sqlalchemy.ext.declarative import (declarative_base)

Base = declarative_base()

class Score(Base):
    __tablename__ = 'scores'

    id = Column('id', Integer, primary_key = True)
    score = Column('score', Integer)
    user = Column(Integer, ForeignKey('user.id'))

    def __init__(self, score, user) -> None:
        self.score = score
        self.user = user

    def __repr__(self):
        return f'Id: {self.id}, ' \
            f'Score {self.score}, ' \
            f'User {self.user}'