# imports from sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# create the engine database
engine = create_engine("sqlite:///code_challenge_restaurants.db")

# 
Base = declarative_base()

class Restaurant(Base):
    # this houses the table name 
    __tablename__ = "restaurants"
    
    # These are the columns for that table
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(Integer())
    
class Customer(Base):
    # this houses the table name 
    __tablename__ = "customers"
    
    # These are the columns for that table
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    
class Review(Base):
    # this houses the table name 
    __tablename__ = "reviews"
    
    # These are the columns for that table
    id = Column(Integer, primary_key=True)
    comments = Column(String(300), nullable=False)
    star_rating = Column(Integer())
    
    # foreign keys
    customer_id = Column(Integer, ForeignKey("customers.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))