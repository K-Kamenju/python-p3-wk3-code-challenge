from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///code_challenge_restaurants.db")

Base = declarative_base()

class Restaurant(Base):
    pass