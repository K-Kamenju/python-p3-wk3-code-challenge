#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Restaurant, Review

if __name__ == "__main__":
    
    # this creates the database
    engine = create_engine("sqlite:///code_challenge_restaurants.db")
    
    # creates a session that will allow us to interact with the database
    Session = sessionmaker(bind = engine)
    session = Session()
    
    # delete active sessions when the seed file is called
    session.query(Review).delete()
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    
    # call the fake method
    fake = Faker()
    
    restaurant_names = ["Bwibo", "KFC", "McDonalds", "Panda Express", "Subway", "Java", "Nyama Mama", "Pepper Tree", "Tin Roof", "Cultiva", "Quest Cafe", "The Lounge", "Dan's Sushi", "Joes Pizza", "Cafe Rio"]
    
    # adding data for the restaurant
    restaurants = []
    for i in range(16):
        restaurant = Restaurant(
            name = random.choice(restaurant_names),
            price = random.randint(1,10)
        )
        
        # add and commit individually to get IDs back
        session.add(restaurant)
        session.commit()
        
        # add the restaurant to the list
        restaurants.append(restaurant)
    
    
    # adding data for the customer
    customers = []
    for i in range(10):
        customer = Customer(
            first_name = fake.first_name(),
            last_name = fake.last_name()
        )
        
        # add and commit individually to get IDs back
        session.add(customer)
        session.commit()
        
        # add the customer to the list
        customers.append(customer)
    
    reviews = []
    for restaurant in restaurants:
        for i in range(random.randint(0,5)):
            customer = random.choice(customers)
            # adds the restaurant to the customer if it wasn't already
            if restaurant not in customer.restaurants:
                customer.restaurants.append(restaurant)
                session.add(Customer)
                session.commit()
            
            # add the review   
            review = Review(
                comments = fake.sentence(),
                star_rating = random.randint(1,5),
                customer_id = customer.id,
                restaurant_id = restaurant.id
            )

            reviews.append(review)
    
    # add and commit 
    session.bulk_save_objects(reviews)
    session.commit()
    session.close()
