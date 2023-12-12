# imports from sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

# this is the base class
Base = declarative_base()

if __name__ == "__main__":
    
    engine = create_engine('sqlite:///code_challenge_restaurants.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()



    '''
    Restaurant class
    '''
    class Restaurant(Base):
        # this houses the table name 
        __tablename__ = "restaurants"
        
        # These are the columns for that table
        id = Column(Integer, primary_key=True)
        name = Column(String(250))
        price = Column(Integer())
        
        # relationship link
        reviews = relationship("Review", back_populates="restaurant")
        customers = association_proxy('reviews', 'customer',
            creator=lambda cs: Review(customer = cs))

        # string representation
        def __repr__(self):

            return f'Restaurant(id={self.id}, ' + \
                f'name={self.name}, ' + \
                f'price={self.price})'

        # find the reviews on this restaurant
        def find_reviews_on_restaurant(self):
            return self.reviews
        
        # find the customers who reviewed this restaurant
        def find_customers(self):
            return [review.customer for review in self.reviews]
        
        # find the fanciest restaurant based on the highest price
        @classmethod
        def fanciest(cls, session):
            fanciest_restaurant = (
                session.query(cls)
                .order_by(cls.price.desc())
                .first()
            )
            return fanciest_restaurant

        # find all the reviews for this restaurant
        def all_reviews(self, session):
            reviews = session.query(Review).filter(Review.restaurant_id == self.id).all()
            formatted_reviews = [
                f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars."
                for review in reviews
            ]
            return formatted_reviews




    '''
    Customer class
    '''
    class Customer(Base):
        # this houses the table name 
        __tablename__ = "customers"
        
        # These are the columns for that table
        id = Column(Integer, primary_key=True)
        first_name = Column(String(10))
        last_name = Column(String(10))
        
        # relationship link
        reviews = relationship("Review", back_populates="customer")
        restaurants = association_proxy('reviews', 'restaurant',
            creator=lambda rs: Review(restaurant = rs))

        # string representation
        def __repr__(self):

            return f'Customer(id={self.id}, ' + \
                f'first_name={self.first_name}, ' + \
                f'last_name={self.last_name})'

        # find the reviews associated with the customer
        def find_reviews_by_customer(self):
            return self.reviews
        
        # find the restaurants associated with the customer
        def find_restaurants(self):
            return [review.restaurant for review in self.reviews]

        # return the full name
        def full_name(self):
            return f"{self.first_name} {self.last_name}"

        # find the favorite restaurant based on how high the rating is
        def favorite_restaurant(self, session):
            favorite_restaurant = (
                session.query(Restaurant)
                .join(Review, Restaurant.id == Review.restaurant_id)
                .filter(Review.customer_id == self.id)
                .order_by(Review.star_rating.desc())
                .first()
            )
            return favorite_restaurant

        # add a review
        def add_review(self, session, restaurant, rating, comments=""):
            new_review = Review(
                customer=self,
                restaurant=restaurant,
                star_rating=rating,
                comments=comments
            )
            session.add(new_review)
            session.commit()

        # delete all the reviews by a customer
        def delete_reviews(self, session, restaurant):
            reviews_to_delete = session.query(Review).filter(
                Review.customer_id == self.id,
                Review.restaurant_id == restaurant.id
            ).all()

            for review in reviews_to_delete:
                session.delete(review)

            session.commit()


    '''
    Review class
    '''
    class Review(Base):
        # this houses the table name 
        __tablename__ = "reviews"
        
        # These are the columns for that table
        id = Column(Integer, primary_key=True)
        comments = Column(String())
        star_rating = Column(Integer())
        
        # foreign keys
        customer_id = Column(Integer, ForeignKey("customers.id"))
        restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
        
        # relationship links
        customer = relationship("Customer", back_populates="reviews")
        restaurant = relationship("Restaurant", back_populates="reviews")

        # string representation
        def __repr__(self):

            return f'Review(id={self.id}, ' + \
                f'comments={self.comments}, ' + \
                f'star_rating={self.star_rating})'
        
        # find the customer associated with the review
        def find_customer(self):
            return self.customer
        
        # find the restaurant associated with the review
        def find_restaurant(self):
            return self.restaurant
        
        # Output a full review
        def full_review(self):
            return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."
    

