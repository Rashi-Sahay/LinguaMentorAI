from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime


from database import Base



class User(Base):

    __tablename__="users"


    id = Column(
        Integer,
        primary_key=True
    )


    target_language = Column(
        String
    )


    native_language = Column(
        String
    )


    level = Column(
        String
    )


    interests = Column(
        Text
    )



class Conversation(Base):

    __tablename__="conversations"


    id = Column(
        Integer,
        primary_key=True
    )


    user_id = Column(
        Integer
    )


    role = Column(
        String
    )


    message = Column(
        Text
    )


    created = Column(
        DateTime,
        default=datetime.utcnow
    )



class Vocabulary(Base):

    __tablename__="vocabulary"


    id = Column(
        Integer,
        primary_key=True
    )


    user_id = Column(
        Integer
    )


    word = Column(
        String
    )


    meaning = Column(
        String
    )


    example = Column(
        Text
    )


    box = Column(
        Integer,
        default=1
    )


    next_review = Column(
        DateTime
    )