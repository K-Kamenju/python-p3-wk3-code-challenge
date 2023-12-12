from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///code_challenge_restaurants.db")

Base = declarative_base()

class Restaurant(Base):
    pass