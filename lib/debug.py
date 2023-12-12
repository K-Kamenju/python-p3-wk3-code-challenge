#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import ipdb

from models import Customer, Restaurant, Review

if __name__ == "__main__":
    
    # this creates the database
    engine = create_engine("sqlite:///code_challenge_restaurants.db")
    
    # creates a session that will allow us to interact with the database
    Session = sessionmaker(bind = engine)
    session = Session()
    
    # debug
    ipdb.set_trace()
    
    