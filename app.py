
from flask import Flask, render_template, redirect, url_for, Response, jsonify
from bson import json_util
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import requests
import json
import pandas as pd
import load_stock_data
import pymongo
from pymongo import MongoClient
import locale


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

# Sector Page Rendering
@app.route("/sector" , methods=['GET'])
def Sector():

    myclient = pymongo.MongoClient("mongodb://localhost:27017/fortune500")
    db = myclient.fortune500
    col = db["companyList"]

    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

    Sectors = ['Retailing', 'Energy', 'Technology', 'Health Care', 'Financials',
        'Wholesalers', 'Telecommunications', 'Motor Vehicles &  Parts',
        'Food &  Drug Stores', 'Industrials', 'Aerospace &  Defense',
        'Transportation', 'Household Products',
        'Food, Beverages &  Tobacco', 'Apparel',
        'Hotels, Restaurants &  Leisure', 'Business Services', 'Materials',
        'Engineering &  Construction', 'Chemicals', 'Media']

    SectorSpread = []
    Employees = []
    Revenue = []
    Profits = []
    ProfitChangeAVG = []
    Assets = []
    MarketValue = []

    sectorCount = 0
    employeeCount = 0
    revenueCount = 0
    profitsCount = 0
    assetsCount = 0
    marketValueCount = 0
    AssetsTotal = 0
    MVTotal = 0

    for sector in Sectors:
        myquery = { "Sector": sector }
        mydoc = col.find(myquery)
        
        ProfitChangePos = []
        ProfitChangeNeg = []
        
        for x in mydoc:
            sectorCount += 1
            employeeCount = employeeCount + locale.atoi(x['Number of Employees'])
            revenueCount = revenueCount + locale.atof(x['Revenues ($millions)'].replace("$",""))
            if x['Profits ($millions)'].startswith('($'):
                profitsCount = profitsCount - locale.atof(x['Profits ($millions)'].replace("($","").replace(")",""))
            else:
                profitsCount = profitsCount + locale.atof(x['Profits ($millions)'].replace("$","").replace("-", "0"))
            
            if x['Profit Change'] == '-':
                ProfitChangeNeg.append(locale.atof(x['Profit Change'].replace('-', '0')))
            elif x['Profit Change'].startswith('-'):
                ProfitChangeNeg.append(locale.atof(x['Profit Change'].replace("%","").replace("-", "")))
            else:
                ProfitChangePos.append(locale.atof(x['Profit Change'].replace("%","")))
                
            assetsCount = assetsCount + locale.atof(x['Assets ($millions)'].replace("$",""))
            AssetsTotal = AssetsTotal + locale.atof(x['Assets ($millions)'].replace("$",""))
            marketValueCount = marketValueCount + (locale.atof(((x['Market Value As of 3/31/20 ($m)']).replace("$","").replace("-", "0"))))
            MVTotal = MVTotal + (locale.atof(((x['Market Value As of 3/31/20 ($m)']).replace("$","").replace("-", "0"))))

        SectorSpread.append(sectorCount)
        Employees.append(employeeCount)
        Revenue.append(revenueCount)
        Profits.append(profitsCount)
        ProfitChangeAVG.append(((sum(ProfitChangePos))/(len(ProfitChangePos)))-((sum(ProfitChangeNeg))/(len(ProfitChangeNeg))))
        Assets.append(assetsCount)
        MarketValue.append(marketValueCount)
        
        sectorCount = 0
        employeeCount = 0
        revenueCount = 0
        profitsCount = 0
        assetsCount = 0
        marketValueCount = 0
    
    SectorTotals = []
    for i in range(len(Sectors)):
        SectorTotalsDict = {'label': Sectors[i], 'value': SectorSpread[i]}
        SectorTotals.append(SectorTotalsDict)

    SectorEmployees = []
    for i in range(len(Sectors)):
        SectorEmpDict = {'label': Sectors[i], 'value': Employees[i]}
        SectorEmployees.append(SectorEmpDict)

    SectorRevenue = []
    for i in range(len(Sectors)):
        SectorRevDict = {'label': Sectors[i], 'value': Revenue[i]}
        SectorRevenue.append(SectorRevDict)
    
    SectorLabels = []
    for i in range(len(Sectors)):
        SectorLabelDict = {'label': Sectors[i]}
        SectorLabels.append(SectorLabelDict)
        
    SectorProfits = []
    for i in range(len(Sectors)):
        SectorProfDict = {'value': Profits[i]}
        SectorProfits.append(SectorProfDict)
        
    SectorProfitChange = []
    for i in range(len(Sectors)):
        if ProfitChangeAVG[i] < 0:
            SectorPCDict = {'label': Sectors[i], 'value': ProfitChangeAVG[i], 'color': '#D18E8F'}
        else:
            SectorPCDict = {'label': Sectors[i], 'value': ProfitChangeAVG[i], 'color': '#BACE98'}
        SectorProfitChange.append(SectorPCDict)

    SectorAssets = []
    for i in range(len(Sectors)):
        SectorAssetsDict = {'label': Sectors[i], 'value': Assets[i]}
        SectorAssets.append(SectorAssetsDict)

    SectorMarketValue = []
    for i in range(len(Sectors)):
        SectorMKDict = {'label': Sectors[i], 'value': MarketValue[i]}
        SectorMarketValue.append(SectorMKDict)
        
    SectorData = [SectorTotals, SectorEmployees, SectorRevenue, SectorLabels, SectorProfits, SectorProfitChange, SectorAssets, AssetsTotal, SectorMarketValue, MVTotal]

    return jsonify(SectorData)


if __name__ == "__main__":
    app.run(debug=True)
