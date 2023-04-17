from sqlalchemy import (Column, String, Integer)
from sqlalchemy.ext.declarative import (declarative_base)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key = True)
    username = Column('username', String)

    def __init__(self, username) -> None:
        self.username = username

    def __repr__(self):
        return f'Id: {self.id}, ' \
            f'Username {self.username}, ' \
            