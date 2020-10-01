
from flask import Flask, render_template, redirect, url_for, Response, jsonify
from bson import json_util
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import requests
import json
import pandas as pd
import numpy as np


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
app.config["MONGO_URI"] = "mongodb://localhost:27017/fortune3"
mongo = PyMongo(app)



# Home Page Rendering 
@app.route("/")
def index():
    return render_template('index.html')
   

# Geomap Page Rendering 
@app.route('/map')
def map():
   return render_template('map.html')


# API endpoint for geomap data
@app.route("/api/map" , methods=['GET'])
def mapData():
 
    results = mongo.db.company.find({})
    mapData = pd.DataFrame(results)
    mapjson = json.loads(json_util.dumps(mapData))
    return jsonify(mapjson)


if __name__ == "__main__":
    app.run(debug=True)
