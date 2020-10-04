
from flask import Flask, render_template, redirect, url_for, Response, jsonify
from bson import json_util
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import requests
import json
import pandas as pd
import load_stock_data


# Create an instance of Flask
app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = '*'
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/fortune500"
mongo = PyMongo(app)

#Getting latest stock data and loading to Mongo DB
@app.before_first_request
def stock_data():
    try:
        print("Data reader reading data from Yahoo finance...")
        load_stock_data.get_stock_info()
        print("Stock data succefully loaded to Mongo.")
    except Exception as e:
        print("Data load to Mongo failed. Please check the logs.")


# Home Page Rendering 
@app.route("/")
def index():
    return render_template('index.html')
   

# Geomap Page Rendering 
@app.route('/map')
def map():
   return render_template('map.html')

# Stock Page Rendering 
@app.route('/stock')
def stock():
   return render_template('stock.html')


# route to get geomap data
@app.route("/api/map" , methods=['GET'])
def mapData():
 
    results = mongo.db.companyList.find({})
    mapData = pd.DataFrame(results)
    mapjson = json.loads(json_util.dumps(mapData))
    return jsonify(mapjson)

# route to get stock data
@app.route("/api/stock" , methods=['GET'])
def stockData():
 
    results = mongo.db.Walmart.find({})
    stockData = pd.DataFrame(results)
    stockjson = json.loads(json_util.dumps(stockData))
    return jsonify(stockjson)


if __name__ == "__main__":
    app.run(debug=True)
