"""Item Catalog Project
Displays sports categories and their respective product items.

Created: 2014
Author: Ramiro Trejo
"""

from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home')
def showCategories():
    # page must show most recently added items
    recentItems = session.query(Item).order_by(Item.id.desc()).limit(5)
    categoryList = session.query(Category).order_by(Category.title).all()
    return render_template('index.html', categories=categoryList, items=recentItems)


@app.route('/category/<int:category_id>')
def showCategory(category_id):
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
    #return "Shows category %s and all of its items" % category_id


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/category/<int:category_id>/edit')
def editCategory(category_id):
    return "Edit the Category %s name" % category_id


@app.route('/category/<int:category_id>/delete')
def deleteCategory(category_id):
    return "Delete the Category %s" % category_id


@app.route('/category/new_item')
def newItem():
    categories = session.query(Category).order_by(Category.title).all()
    return render_template('new_item.html', categories=categories)


@app.route('/category/<int:category_id>/item/<int:item_id>')
def showItem(category_id, item_id):
    return "Show item %s page" % item_id


@app.route('/category/<int:category_id>/item/<int:item_id>/edit')
def editItem(category_id, item_id):
    # return "Edit item %s page" % item_id
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('edit_item.html', category=category, item=item)


@app.route('/category/<int:category_id>/item/<int:item_id>/delete')
def deleteItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('deleteItem.html', category=category, item=item)


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
