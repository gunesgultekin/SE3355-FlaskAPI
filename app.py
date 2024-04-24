from flask import Flask, jsonify
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = "MSSQL DATABASE CONNECTION STRING"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_num = db.Column(db.Integer)
    name = db.Column(db.String)
    description = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)
    rating = db.Column(db.Float)
    comment_count = db.Column(db.Integer)
    dealer = db.Column(db.String)
    dealer_rating = db.Column(db.Float)
    manufacturer = db.Column(db.String)
    stock_count = db.Column(db.Integer)

class Advertisements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)

@app.route("/loadAds")
def loadAds():
    advertisements = Advertisements.query.all()
    ad_list = [
        {
          'title':advertisement.title,
           'image':advertisement.image
        } for advertisement in advertisements
    ]

    return jsonify({"ads":ad_list})


@app.route("/getAll")
def getAll():
    products = Products.query.all()
    return products

@app.route("/api/searchFromName",methods=['GET'])
def searchFromName():
    prod_name = request.args['title']
    product = Products.query.where(Products.name == prod_name).first()
    if not product:
        return jsonify("No such product")

    product_json= {'product_num': product.product_num,
                    'name': product.name,
                    'description': product.description,
                    'category': product.category,
                    'price': product.price,
                    'image': product.image,
                    'rating': product.rating,
                    'comment_count': product.comment_count,
                    'dealer': product.dealer,
                    'dealer_rating': product.dealer_rating,
                    'manufacturer': product.manufacturer,
                    'stock_count': product.stock_count
                    }
    return jsonify(product_json)


@app.route("/api/search",methods=['GET'])
def search():
    key= request.args['key']
    products_by_name = Products.query.filter(Products.name.ilike(f'%{key}%'))
    products_by_category = Products.query.filter(Products.category.ilike(f'%{key}%'))
    if not products_by_name:
        return jsonify('No products found')
    if not products_by_category:
        return jsonify('No products found')

    products = products_by_name.union(products_by_category).all()

    product_list = [{'product_num': product.product_num,
                     'name': product.name,
                     'description': product.description,
                     'category': product.category,
                     'price': product.price,
                     'image': product.image,
                     'rating': product.rating,
                     'comment_count': product.comment_count,
                     'dealer': product.dealer,
                     'dealer_rating': product.dealer_rating,
                     'manufacturer': product.manufacturer,
                     'stock_count': product.stock_count
                     } for product in products]

    return jsonify({'products': product_list})

if __name__ == '__main__':
    app.run()
