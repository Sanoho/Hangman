from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True)
    username = Column(String())
    score = relationship('Score', backref = 'user')
    def __repr__(self):
        return f'Id: {self.id}, ' \
            f'Username {self.username}' 
    
    
class Word(Base):
    __tablename__ = 'words'
    id = Column('id', Integer, primary_key= True)
    word = Column(String())
    difficulty = Column(Integer())
    def __repr__(self):
        return f'Id: {self.id}, ' \
            f'Word {self.word}, ' \
            f'Difficulty {self.difficulty}'
    
    
class Score(Base):
    __tablename__ = 'scores'
    id = Column('id', Integer, primary_key = True)
    score = Column(Integer())
    user_id = Column(Integer, ForeignKey('users.id'))
    leaderboard_id = Column(Integer, ForeignKey('leaderboard.id'))
    def __repr__(self):
        return f'Id: {self.id}, ' \
            f'Score {self.score}, ' \
            f'User {self.user}'
    
    
class Leaderboard(Base):     
    __tablename__ = 'leaderboard'
    id = Column('id', Integer, primary_key = True)
    scores = relationship('Score', backref = 'leaderboard')
    def __repr__(self):
        return f'Id: {self.id}, ' 