
# Import dependencies
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

# Getting latest stock data and loading to Mongo DB
@app.before_first_request
def stock_data():
    try:
        print("Data reader reading data from Yahoo finance...")
        load_stock_data.get_stock_info()
        print("Stock data successfully loaded to Mongo.")
    except:
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
 
    # Set up Mongodb connection
    myclient = pymongo.MongoClient("mongodb://localhost:27017/fortune500")
    db = myclient.fortune500

    # Walmart data reformatting for fusion chart

    #Connect to Walmart collection
    colWMT = db["WMT"]

    # Count number of documents in collections
    WMTcount = colWMT.find().count()
    # Create list for xaxis labels
    WMTLabels = []
    # Create list for dictionaries of Walmart data
    WMT = []
    # Set initial x tick counter to zero
    WMTx = 0

    # Loop through documents to collect and reformat data for fusioncharts
    for i in colWMT.find():
        # Add one to the x tick for each loop to set up xaxis alignment for data
        WMTx += 1
        # Collect and reformat document data to the fusioncharts format
        WMTdict = {'tooltext': (f"{(str(i['Date'])[:-9])} Open: ${round(i['Open'], 2)} Close: ${round (i['Close'], 2)}"), 'open': i['Open'], 'high': i['High'], 'low': i['Low'], 'close': i['Close'], 'volume': i['Volume'], 'x': WMTx}
        # Append each document's data to the WMT list
        WMT.append(WMTdict)
        # Conditionals to grab the 5 xaxis labels using the x ticks and document count variable
        if WMTx == 1:
            WMTL1 = {'label': i['Date'].strftime("%B %Y"), 'x': WMTx}
            WMTLabels.append(WMTL1)
        elif WMTx == round((WMTcount * 0.25), 0):
            WMTL2 = {'label': i['Date'].strftime("%B %Y"), 'x': WMTx}
            WMTLabels.append(WMTL2)
        elif WMTx == round((WMTcount * 0.50), 0):
            WMTL3 = {'label': i['Date'].strftime("%B %Y"), 'x': WMTx}
            WMTLabels.append(WMTL3)
        elif WMTx == round((WMTcount * 0.75), 0):
            WMTL4 = {'label': i['Date'].strftime("%B %Y"), 'x': WMTx}
            WMTLabels.append(WMTL4)
        elif WMTx == WMTcount:
            WMTL5 = {'label': i['Date'].strftime("%B %Y"), 'x': WMTx}
            WMTLabels.append(WMTL5)
    
    # Amazon data reformatting for fusion chart
    # For explanation of code chunk, see code for Walmart starting on line 74

    colAMZN = db["AMZN"]

    AMZNcount = colAMZN.find().count()
    AMZNLabels = []
    AMZN = []
    AMZNx = 0

    for i in colAMZN.find():
        AMZNx += 1
        AMZNdict = {'tooltext': (f"{(str(i['Date'])[:-9])} Open: ${round(i['Open'], 2)} Close: ${round (i['Close'], 2)}"), 'open': i['Open'], 'high': i['High'], 'low': i['Low'], 'close': i['Close'], 'volume': i['Volume'], 'x': AMZNx}
        AMZN.append(AMZNdict)
        if AMZNx == 1:
            AMZNL1 = {'label': i['Date'].strftime("%B %Y"), 'x': AMZNx}
            AMZNLabels.append(AMZNL1)
        elif AMZNx == round((AMZNcount * 0.25), 0):
            AMZNL2 = {'label': i['Date'].strftime("%B %Y"), 'x': AMZNx}
            AMZNLabels.append(AMZNL2)
        elif AMZNx == round((AMZNcount * 0.50), 0):
            AMZNL3 = {'label': i['Date'].strftime("%B %Y"), 'x': AMZNx}
            AMZNLabels.append(AMZNL3)
        elif AMZNx == round((AMZNcount * 0.75), 0):
            AMZNL4 = {'label': i['Date'].strftime("%B %Y"), 'x': AMZNx}
            AMZNLabels.append(AMZNL4)
        elif AMZNx == AMZNcount:
            AMZNL5 = {'label': i['Date'].strftime("%B %Y"), 'x': AMZNx}
            AMZNLabels.append(AMZNL5)

    # Exxon Mobil data reformatting for fusion chart
    # For explanation of code chunk, see code for Walmart starting on line 74

    colXOM = db["XOM"]

    XOMcount = colXOM.find().count()
    XOMLabels = []
    XOM = []
    XOMx = 0

    for i in colXOM.find():
        XOMx += 1
        XOMdict = {'tooltext': (f"{(str(i['Date'])[:-9])} Open: ${round(i['Open'], 2)} Close: ${round (i['Close'], 2)}"), 'open': i['Open'], 'high': i['High'], 'low': i['Low'], 'close': i['Close'], 'volume': i['Volume'], 'x': XOMx}
        XOM.append(XOMdict)
        if XOMx == 1:
            XOML1 = {'label': i['Date'].strftime("%B %Y"), 'x': XOMx}
            XOMLabels.append(XOML1)
        elif XOMx == round((XOMcount * 0.25), 0):
            XOML2 = {'label': i['Date'].strftime("%B %Y"), 'x': XOMx}
            XOMLabels.append(XOML2)
        elif XOMx == round((XOMcount * 0.50), 0):
            XOML3 = {'label': i['Date'].strftime("%B %Y"), 'x': XOMx}
            XOMLabels.append(XOML3)
        elif XOMx == round((XOMcount * 0.75), 0):
            XOML4 = {'label': i['Date'].strftime("%B %Y"), 'x': XOMx}
            XOMLabels.append(XOML4)
        elif XOMx == XOMcount:
            XOML5 = {'label': i['Date'].strftime("%B %Y"), 'x': XOMx}
            XOMLabels.append(XOML5)

    # Apple data reformatting for fusion chart
    # For explanation of code chunk, see code for Walmart starting on line 74

    colAAPL = db["AAPL"]

    AAPLcount = colAAPL.find().count()
    AAPLLabels = []
    AAPL = []
    AAPLx = 0

    for i in colAAPL.find():
        AAPLx += 1
        AAPLdict = {'tooltext': (f"{(str(i['Date'])[:-9])} Open: ${round(i['Open'], 2)} Close: ${round (i['Close'], 2)}"), 'open': i['Open'], 'high': i['High'], 'low': i['Low'], 'close': i['Close'], 'volume': i['Volume'], 'x': AAPLx}
        AAPL.append(AAPLdict)
        if AAPLx == 1:
            AAPLL5 = {'label': i['Date'].strftime("%B %Y"), 'x': AAPLx}
            AAPLLabels.append(AAPLL5)
        elif AAPLx == round((AAPLcount * 0.25), 0):
            AAPLL5 = {'label': i['Date'].strftime("%B %Y"), 'x': AAPLx}
            AAPLLabels.append(AAPLL5)
        elif AAPLx == round((AAPLcount * 0.50), 0):
            AAPLL5 = {'label': i['Date'].strftime("%B %Y"), 'x': AAPLx}
            AAPLLabels.append(AAPLL5)
        elif AAPLx == round((AAPLcount * 0.75), 0):
            AAPLL5 = {'label': i['Date'].strftime("%B %Y"), 'x': AAPLx}
            AAPLLabels.append(AAPLL5)
        elif AAPLx == AAPLcount:
            AAPLL5 = {'label': i['Date'].strftime("%B %Y"), 'x': AAPLx}
            AAPLLabels.append(AAPLL5)

    # CVS data reformatting for fusion chart
    # For explanation of code chunk, see code for Walmart starting on line 74

    colCVS = db["CVS"]

    CVScount = colCVS.find().count()
    CVSLabels = []
    CVS = []
    CVSx = 0

    for i in colCVS.find():
        CVSx += 1
        CVSdict = {'tooltext': (f"{(str(i['Date'])[:-9])} Open: ${round(i['Open'], 2)} Close: ${round (i['Close'], 2)}"), 'open': i['Open'], 'high': i['High'], 'low': i['Low'], 'close': i['Close'], 'volume': i['Volume'], 'x': CVSx}
        CVS.append(CVSdict)
        if CVSx == 1:
            CVSL1 = {'label': i['Date'].strftime("%B %Y"), 'x': CVSx}
            CVSLabels.append(CVSL1)
        elif CVSx == round((CVScount * 0.25), 0):
            CVSL2 = {'label': i['Date'].strftime("%B %Y"), 'x': CVSx}
            CVSLabels.append(CVSL2)
        elif CVSx == round((CVScount * 0.50), 0):
            CVSL3 = {'label': i['Date'].strftime("%B %Y"), 'x': CVSx}
            CVSLabels.append(CVSL3)
        elif CVSx == round((CVScount * 0.75), 0):
            CVSL4 = {'label': i['Date'].strftime("%B %Y"), 'x': CVSx}
            CVSLabels.append(CVSL4)
        elif CVSx == CVScount:
            CVSL5 = {'label': i['Date'].strftime("%B %Y"), 'x': CVSx}
            CVSLabels.append(CVSL5)

    # Put xaxis labels for each stock into one dictionary
    LabelPackage = {'WalMart': WMTLabels, 'Amazon': AMZNLabels, 'ExxonMobil': XOMLabels, 'Apple': AAPLLabels, 'CVS': CVSLabels}
    # Create list of company names to populate drop down in StockLogic.js
    stockNames = ['WalMart', 'Amazon', 'ExxonMobil', 'Apple', 'CVS']
    # Combine stockNames, stock data, and LabelPackage into one dictionary to be jsonified and returned
    stockData = {'stockName': stockNames, 'WalMart': WMT, 'Amazon': AMZN, 'ExxonMobil': XOM, 'Apple': AAPL, 'CVS': CVS,
        'LabelPackage': LabelPackage}

    return jsonify(stockData)

# Sector Page Rendering
@app.route("/sector" , methods=['GET'])
def Sector():

    # Set up Mongodb connection
    myclient = pymongo.MongoClient("mongodb://localhost:27017/fortune500")
    db = myclient.fortune500
    col = db["companyList"]

    # Set up locale for use in lines 308-332, which will remove commas from strings to create integers/floats
    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

    # Create list of sectors used to loop through documents in query
    Sectors = ['Retailing', 'Energy', 'Technology', 'Health Care', 'Financials',
        'Wholesalers', 'Telecommunications', 'Motor Vehicles &  Parts',
        'Food &  Drug Stores', 'Industrials', 'Aerospace &  Defense',
        'Transportation', 'Household Products',
        'Food, Beverages &  Tobacco', 'Apparel',
        'Hotels, Restaurants &  Leisure', 'Business Services', 'Materials',
        'Engineering &  Construction', 'Chemicals', 'Media']

    # The following commented out code can be used to find what companies have unlisted sectors and
    # are therefore excluded from the analyses:
    # ------
    # myquery = { "Sector": "" }
    # mydoc = col.find(myquery)
    # for x in mydoc:
         #print(x['Company Name'])

    # Create lists to hold dictionaries of the totals for each sector
    SectorSpread = []
    Employees = []
    Revenue = []
    Profits = []
    ProfitChangeAVG = []
    Assets = []
    MarketValue = []

    # Set initial counters to zero for the loop
    sectorCount = 0
    employeeCount = 0
    revenueCount = 0
    profitsCount = 0
    assetsCount = 0
    marketValueCount = 0
    AssetsTotal = 0
    MVTotal = 0

    # Using list of sectors, loop through collection documents to filter data 
    # into the corresponding lists above
    for sector in Sectors:

        # Set up query
        myquery = { "Sector": sector }
        mydoc = col.find(myquery)
        
        # Set up profit change lists for positive and negative values
        ProfitChangePos = []
        ProfitChangeNeg = []
        
        # Loop through each document to grab specific values while in greater sector loop
        for x in mydoc:
            # Add one to sector counter
            sectorCount += 1
            # Add company's employee total to employee counter
            employeeCount = employeeCount + locale.atoi(x['Number of Employees'])
            # Add company's revenue total to revenue counter
            revenueCount = revenueCount + locale.atof(x['Revenues ($millions)'].replace("$",""))
            # Conditional to remove special characters, add or subtract profit value based on whether
            # it is a positive or negative value ( negative values represented with () around value ),
            # and replace "-" values with 0
            if x['Profits ($millions)'].startswith('($'):
                profitsCount = profitsCount - locale.atof(x['Profits ($millions)'].replace("($","").replace(")",""))
            else:
                profitsCount = profitsCount + locale.atof(x['Profits ($millions)'].replace("$","").replace("-", "0"))
            # Conditional change "-" values to 0 and filter negative and positive values to corresponding lists
            if x['Profit Change'] == '-':
                ProfitChangeNeg.append(locale.atof(x['Profit Change'].replace('-', '0')))
            elif x['Profit Change'].startswith('-'):
                ProfitChangeNeg.append(locale.atof(x['Profit Change'].replace("%","").replace("-", "")))
            else:
                ProfitChangePos.append(locale.atof(x['Profit Change'].replace("%","")))
            # Add company's asset total to asset counter    
            assetsCount = assetsCount + locale.atof(x['Assets ($millions)'].replace("$",""))
            # Add company's asset total to the counter tracking total assets across all sectors for donut chart
            AssetsTotal = AssetsTotal + locale.atof(x['Assets ($millions)'].replace("$",""))
            # Add company's market value to market value counter
            marketValueCount = marketValueCount + (locale.atof(((x['Market Value As of 3/31/20 ($m)']).replace("$","").replace("-", "0"))))
            # Add company's market value to the counter tracking total market value across all sectors for donut chart
            MVTotal = MVTotal + (locale.atof(((x['Market Value As of 3/31/20 ($m)']).replace("$","").replace("-", "0"))))

        # Add sector totals to each corresponding list
        SectorSpread.append(sectorCount)
        Employees.append(employeeCount)
        Revenue.append(revenueCount)
        Profits.append(profitsCount)
        # Calculate profit change average across sector
        ProfitChangeAVG.append(((sum(ProfitChangePos))/(len(ProfitChangePos)))-((sum(ProfitChangeNeg))/(len(ProfitChangeNeg))))
        Assets.append(assetsCount)
        MarketValue.append(marketValueCount)
        
        # Reset counters for next sector loop
        sectorCount = 0
        employeeCount = 0
        revenueCount = 0
        profitsCount = 0
        assetsCount = 0
        marketValueCount = 0

    # Zip lists together into dictionaries that fit fusionchart format
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
        # Assign color codes to positive and negative profit change values
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
        
    # Combine all sector lists together in one list to be jsonified and returned    
    SectorData = [SectorTotals, SectorEmployees, SectorRevenue, SectorLabels, SectorProfits, SectorProfitChange, SectorAssets, AssetsTotal, SectorMarketValue, MVTotal]

    return jsonify(SectorData)


if __name__ == "__main__":
    app.run(debug=True)