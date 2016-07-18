from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    title = Column(String(250), nullable = False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title' : self.title,
        }


class Item(Base):

    __tablename__ = 'item'

    id = Column(Integer, primary_key = True)
    title = Column(String(250), nullable = False)
    description = Column(String(250))
    cat_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    # add an image url category of string type

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'description' : self.description,
            'cat_id' : self.cat_id,
        }


engine = create_engine('sqlite:///categoryitem.db')

Base.metadata.create_all(engine)
