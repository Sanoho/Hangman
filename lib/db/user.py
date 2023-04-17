from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import (declarative_base)

Base = declarative_base()

class User(Base):
    def __init__(self, username) -> None:
        self.username = username