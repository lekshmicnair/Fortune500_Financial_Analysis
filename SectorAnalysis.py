import pymongo
from pymongo import MongoClient
import locale

def SectorAnalysis():

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
            marketValueCount = marketValueCount + locale.atof(x['Market Value As of 3/31/20 ($m)'].replace("$","").replace("-", "0"))
        
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
    