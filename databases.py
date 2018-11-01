from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, in_stock, rank):
  #TODO: complete the functions (you will need to change the function's inputs)
  product_object = Product(
      name=name,
      price=price,
      in_stock=in_stock,
      rank= rank)
  session.add(product_object)
  session.commit()


def update_product(name ,Nname, Nprice):
  #TODO: complete the functions (you will need to change the function's inputs)
  if Nprice<=300:
  	product_object = session.query(Product).filter_by(name = name).first()
  	product_object.name = Nname
  	product_object.price = Nprice
  	session.commit()
  else:
  	print("Too bad!! the price is not in the range")


def delete_product(id):
  session.query(Product).filter_by(
      id=id).delete()
  session.commit()


def get_product(id):
  pass
