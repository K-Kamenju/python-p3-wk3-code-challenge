#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



from models import Restaurant, Customer, Review, Base

if __name__ == "__main__":
    
    # this creates the database
    engine = create_engine("sqlite:///code_challenge_restaurants.db")
    Base.metadata.create_all(engine)
    # creates a session that will allow us to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Test Suites:
    '''
    Object Relationship Methods
    '''
    print(f"\n Below are the Object Relationship Methods Test Suites: \n")
    # Review Testing
    review_orm_test_case = session.query(Review).first()
    print(f"\n These are tests for the reviews:")
    print(f"\n Review customer test\n This review was made by: {review_orm_test_case.find_customer()}")
    print(f"\n Review restaurant test\n This review was for: {review_orm_test_case.find_restaurant()}")
    
    # Restaurant Testing
    restaurant_orm_test_case = session.query(Restaurant).first()
    print(f"\n These are tests for the restaurants:")
    print(f"\n Restaurant reviews test\n The reviews for this restaurant are: {restaurant_orm_test_case.find_reviews_on_restaurant()}")
    print(f"\n Restaurant customers test\n The customers who reviewed this restaurant are: {restaurant_orm_test_case.find_customers()}")
    
    # Customer Testing
    customer_orm_test_case = session.query(Customer).first()
    print(f"\n These are tests for the customers:")
    print(f"\n Customer reviews test\n The reviews this customer has made are: {customer_orm_test_case.find_reviews_by_customer()}")
    print(f"\n Customer restaurants test\n The restaurants this customer has reviewed are: {customer_orm_test_case.find_restaurants()}")
    
    
    '''
    Aggregate and Relationship Methods
    '''
    print(f"\n \n Below are the Aggregate and Relationship Methods Test Suites: \n")
    # Customer Testing
    customer_arm_test_case = session.query(Customer).first()
    print(f"\n These are tests for the customers:")
    print(f"\n Customer full name test\n This customer's full name is: {customer_arm_test_case.full_name()}")
    print(f"\n Customer's favorite restaurant test\n This customer's favorite restaurant is: {customer_arm_test_case.favorite_restaurant(session)}")
    
    # Review Testing
    review_arm_test_case = session.query(Review).first()
    print(f"\n These are tests for the reviews:")
    print(f"\n Review full review test\n This review is: {review_arm_test_case.full_review()}")
    
    # Restaurant Testing
    restaurant_arm_test_case = session.query(Restaurant).first()
    print(f"\n These are tests for the restaurants:")
    print(f"\n Restaurant all reviews test\n The reviews for this restaurant are: {restaurant_arm_test_case.all_reviews(session)}")
    print(f"\n Restaurant fanciest test\n The fanciest restaurant is: {restaurant_arm_test_case.fanciest(session)}")