from flask import Flask, render_template, request, redirect, jsonify, url_for, flash  # NOQA
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Product, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import functions

app = Flask(__name__)

engine = create_engine('sqlite:///productscatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/category/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[r.serialize for r in categories])


# Show all categories
@app.route('/')
@app.route('/category/')
def showCategories():
    categories = session.query(Category).order_by(asc(Category.name))
    if 'username' not in login_session:
        return render_template('publiccategories.html', categories=categories)
    else:
       return render_template('categories.html', categories=categories)


# Show all categories
#@app.route('/')
#@app.route('/category/')
#def showCategories():
#    categories = session.query(Category).all()
# return "This page will show all my restaurants"
#   return render_template('publiccategories.html', categories=categories)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    category = session.query(Category).first()
    items = session.query(Product).filter_by(category_id=category.id)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
    return output


if __name__ == '__main__':
    app.debug = True
app.run(host='0.0.0.0', port=5000)
