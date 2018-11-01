from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Write your functions to interact with the database here :

def create_product(name, used, price, description):
    """
    Add a product to the database, given
    their name, used , price and description . 
    """
    product_object = Product(
        name=name,
        used=used,
        price=price,
        description=description)
    session.add(product_object)
    session.commit()

def update_product(name,used,price):

   product_object = session.query(
       Product).filter_by(
       name=name).first()
   product_object.used = used
   if price > 299:
   	print("too exbensive bro")
   else:
   	product_object.price = price
   	session.commit()

def delete_product(id):

   session.query(Product).filter_by(
       id=id).delete()
   session.commit()

def query_all():
   products = session.query(
      Product).all()
   return products

def query_by_id(id):
   product = session.query(
       Product).filter_by(
       id=id).first()
   name = product.name
   return name
