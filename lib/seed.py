#!/usr/bin/env python3

# import faker
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Customer, Review, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///code_challenge_restaurants.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Review).delete()
    session.query(Customer).delete()
    session.query(Restaurant).delete()

    fake = Faker()

    # Generate Restaurants
    restaurants = []
    for i in range(20):
        restaurant = Restaurant(
            name=fake.company(),
            price=random.randint(1, 50)
        )
        session.add(restaurant)
        
        restaurants.append(restaurant)
        
    session.commit()
    
    # Print statement to check the number of restaurants generated
    print("Number of Restaurants:", session.query(Restaurant).count())

    # Generate Customers
    customers = []
    for i in range(20):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        
        customers.append(customer)

    session.commit()
    # Print statement to check the number of customers generated
    print("Number of Customers:", session.query(Customer).count())
    
    # Generate Reviews
    reviews = []
    for i in range(50):
        restaurant = random.choice(restaurants)
        customer = random.choice(customers)

        review = Review(
            comments=fake.sentence(),
            star_rating=random.randint(1, 5),
            customer_id=customer.id,
            restaurant_id=restaurant.id
        )
        session.add(review)
        
        reviews.append(review)
    
    session.commit()
    
    # Print statement to check the number of reviews generated
    print("Number of Reviews:", session.query(Review).count())
    
    session.close()
