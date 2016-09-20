from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

engine = create_engine('sqlite:///categoryitem.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

list_of_categories = [ 'Soccer',
                    'Basketball',
                    'Baseball',
                    'Frisbee',
                    'Snowboarding',
                    'Rock Climbing',
                    'Foosball',
                    'Skating',
                    'Hockey' ]

for item in list_of_categories:

    newCategory = Category(title = item)
    session.add(newCategory)
    session.commit()
