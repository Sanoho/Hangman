from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True)
    username = Column('username', String)
    def __init__(self, username) -> None:
        self.username = username
    def __repr__(self):
        return f'Id: {self.id}, ' \
            f'Username {self.username}' 
    
    
class Word(Base):
    __tablename__ = 'words'
    id = Column('id', Integer, primary_key= True)
    word = Column('word', String)
    difficulty = Column('difficulty', Integer)
    def __init__(self, word, difficulty) -> None:
        self.word = word
        self.difficulty = difficulty
    @property
    def difficulty(self):
        return self._difficulty
    @difficulty.setter
    def difficulty(self, difficulty):
        if isinstance(difficulty, int) and 1 <= difficulty <= 5:
            self._difficulty = difficulty
    def __repr__(self) -> str:
        return f'Id: {self.id}, ' \
            f'Word {self.word}, ' \
            f'Difficulty {self.difficulty}'
    
    
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
            f'Score {self.score},' 