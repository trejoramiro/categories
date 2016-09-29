from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

engine = create_engine('sqlite:///categoryitem.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Baseball

# Basketball
category = session.query(Category).filter_by(id=2).one()
title = ['Basketball', 'Basketball Hoop', 'Shooter Sleeves']
descriptions = ['Get into the game with our basketball and achieve greatness on the court. Durable composite leather offers an incredible feel and grip that will withstand both indoor and outdoor play, letting your rule the court of your choice.',
                'Enhance your game with the our amazing basketball hoop. This basketball system features a steel-framed, shatter-proof backboard with a blow-molded frame pad for maximum durability. Our construction allows for effortless height adjustments, while the XL heavy-duty portable base and straight round extension arms provide extra stability.',
                'Speed up muscle recovery and optimize your performance with our Shooter Sleeves. This sleeve improves blood flow circulation to your bicep and tricep while protecting your skin from abrasions. Constructed with advance moisture management technology, the Shooter Sleeves will keep you cool and dry as you train.']
# category.id
for i in range(3):
    newItem = Item(name = title[i], description=descriptions[i], cat_id = category.id)
    session.add(newItem)
    session.commit()


# Foosball

# Frisbee

# Hockey

# Rock Climbing

# Skating

# Snowboarding

# Soccer
