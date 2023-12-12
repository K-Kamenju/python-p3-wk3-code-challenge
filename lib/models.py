# imports from sqlalchemy
from sqlalchemy import func
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

# this is the base class
Base = declarative_base()



'''
Restaurant class
'''
class Restaurant(Base):
    # this houses the table name 
    __tablename__ = "restaurants"
    
    # These are the columns for that table
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
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



'''
Customer class
'''
class Customer(Base):
    # this houses the table name 
    __tablename__ = "customers"
    
    # These are the columns for that table
    id = Column(Integer, primary_key=True)
    first_name = Column(String(10), nullable=False)
    last_name = Column(String(10), nullable=False)
    
    # relationship link
    reviews = relationship("Review", back_populates="customer")
    restaurants = association_proxy('reviews', 'restaurant',
        creator=lambda rs: Review(restaurant = rs))

    # string representation
    def __repr__(self):

        return f'Customer(id={self.id}, ' + \
            f'first_name={self.first_name}, ' + \
            f'last_name={self.last_name})'



'''
Review class
'''
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
    
    # relationship links
    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")

    # string representation
    def __repr__(self):

        return f'Review(id={self.id}, ' + \
            f'comments={self.comments}, ' + \
            f'star_rating={self.star_rating})'