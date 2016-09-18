"""Items Catalog
Displays sports categories and their respective products.

Created: 2015-2016
Author: Ramiro Trejo
"""

from flask import Flask, render_template, redirect, request, url_for, flash, jsonify, make_response
from flask import session as login_session
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, Stock, Image, Review, User

from oauth2client.client import flow_from_clientsecrets, FlowExchangeError

import httplib2, json, requests, random, string

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/categories')
def index():
    # Displays most recent items.
    recentItems = session.query(Item).order_by(Item.id.desc()).limit(5)
    categoryList = session.query(Category).order_by(Category.name).all()
    return render_template('index.html', categories=categoryList, items=recentItems)


@app.route('/categories/new')
def new():
    #categories = session.query(Category).order_by(Category.title).all()
    return render_template('new.html')


@app.route('/categories', methods=['POST'])
def create():
    #create a new item
    newItem = Item(
        name = name,
        description = description,
        cat_id =category,
        price = price,
        image_url = image_url,
     )
    session.add(newItem)
    session.commit()
    redirect('/categories/item/<int:item_id>')


@app.route('/categories/item/<int:item_id>')
def showItem(item_id):
    item = session.query(Item).filter_by(id=item_id)
    return render_template('show_item.html', item=item)


@app.route('/categories/<int:category_id>')
def show(category_id):
    # Displays only one item
    #if there are no items to show then have the html flash a message
    categories = session.query(Category).order_by(Category.title).all()
    category = session.query(Category).filter_by(id=category_id).one()
    # will probably need to have a try to see whether the query function returns something
    # if the query function returns an exception then notify the user
    print category
    print category.id
    # Baseball - 3
    # Basketball - 2
    # Foosball - 7
    # Frisbee - 4
    # Hockey - 9
    # Rock Climbing - 6
    # Skating - 8
    # Snowboarding - 5
    # Soccer - 1
    items = session.query(Item).filter_by(cat_id=category_id).all()
    if not items:
        string = "No items found under " + category.title
        flash(string)
        return render_template('show_category.html', category=category, items=items, categories=categories)
    else:
        return render_template('show_category.html', category=category, items=items, categories=categories)


@app.route('/categories/<int:category_id>/item/<int:item_id>/edit')
def edit(category_id, item_id):
    # return "Edit item %s page" % item_id
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('edit_item.html', category=category, item=item)


@app.route('/categories/<int:category_id>/item/<int:item_id>', methods=['PATCH'])
def update(category_id, item_id):
    return render_template('update.html', item=item)


@app.route('/items/<int:category_id>/item/<int:item_id>', methods=['DELETE'])
def destroy(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('delete_item.html', category=category, item=item)


@app.route('/login')
def login():
    return render_template('login.html')


# @app.route('/catalog.json')
# def json():
    # return the data in json form


@app.errorhandler(404)
def notFoundError(error):
    # render_template('404.html'), 404
    return "Error 404. Found no path named '%s'" % request.path


@app.errorhandler(500)
def internalError(error):
    # render_template('500.html'), 500
    return "Error %s" % 500


if __name__ == '__main__':
    # why does flash() need for an app.secret_key; what is its role?
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0', port = 8000)
