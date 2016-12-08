from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine

import datetime

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)


    def __repr__(self):
        return "<Category(id='%s', name='%s')>" % (self.id, self.name)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name' : self.name,
        }


class Item(Base):

    __tablename__ = 'item'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    description = Column(String(250))
    price = Column(Integer)
    #image_url = Column(String(500))
    # could give a default image file using 'default='
    cat_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    def __repr__(self):
        return "<Item(id='%s',name='%s',description='%s',price='%s',cat_id='%s')>" % (self.id, self.name, self.description, self.price)

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'categoryId' : self.cat_id
        }


class Image(Base):

    __tablename__ = 'image'

    id = Column(Integer, primary_key = True)
    url = Column(String(500))
    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship(Item)

    def __repr__(self):
        return "<Image(id='%s', url='%s', item_id='%s')>" % (self.id, self.url, self.item_id)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'itemId': self.item_id
        }


class Stock(Base):

    __tablename__ = 'stock'

    id = Column(Integer, primary_key = True)
    color = Column(String(50))
    size = Column(String(10))
    quantity = Column(Integer, nullable = False)
    last_updated = Column(DateTime, onupdate = datetime.datetime.now)
    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship(Item)

    def __repr__(self):
        return "<Stock(id='%s', color='%s', size='%s', quantity='%s', last_updated='%s', item_id='%s')>" % (self.id, self.color, self.size, self.quantity, self.last_updated, self.item_id)

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'color' : self.color,
            'size': self.size,
            'quantity' : self.quantity,
            'itemId' : self.item_id,
        }


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    username = Column(String(200), nullable = False)
    admin = Column(Boolean, nullable = False)

    def __repr__(self):
        return "<User(id='%s',username='%s',admin='%s')>" % (self.id, self.username, self.admin)


class Review(Base):

    __tablename__ = 'review'

    id = Column(Integer, primary_key = True)
    body = Column(String(400), nullable = False)
    rating = Column(Integer, nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    created_at = Column(DateTime, onupdate = datetime.datetime.now)
    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship(Item)

    @property
    def serialize(self):
        return {
        'id' : self.id,
        'body' : self.body,
        'rating' : self.rating,
        'user' : self.user_name,
        'createdAt' : self.created_at,
        'item' : self.item_id,
        }

    def __repr__(self):
        return "<Review(id='%s', body='%s', rating='%s', user='%s', created_at='%s', item='%s')>" % (self.id, self.body, self.rating, self.user, self.created_at, self.item)

engine = create_engine('sqlite:///categoryitem.db')

Base.metadata.create_all(engine)
