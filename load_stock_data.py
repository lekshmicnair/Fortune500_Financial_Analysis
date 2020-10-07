import pandas as pd
import pandas_datareader.data as pdr
import datetime as dt
import time
import json
from dateutil.relativedelta import relativedelta
import pymongo
from pymongo import MongoClient

def get_stock_info():
    # Get stock info from yahoo finance for a year using datareader
    start_date = dt.datetime.today() - relativedelta(years=1)
    end_date = dt.datetime.today()

    stock_data_1 = pdr.DataReader("WMT", 'yahoo', start_date, end_date)
    stock_data_2 = pdr.DataReader("AMZN", 'yahoo', start_date, end_date)
    stock_data_3 = pdr.DataReader("XOM", 'yahoo', start_date, end_date)
    stock_data_4 = pdr.DataReader("AAPL", 'yahoo', start_date, end_date)
    stock_data_5 = pdr.DataReader("CVS", 'yahoo', start_date, end_date)
    
    # Sleep for 1 minute to allow data reader to finish before continuing
    time.sleep(60)

    # Reset stock data indexes
    stock_data_1.reset_index(inplace=True)
    stock_data_2.reset_index(inplace=True)
    stock_data_3.reset_index(inplace=True)
    stock_data_4.reset_index(inplace=True)
    stock_data_5.reset_index(inplace=True)

    # Connect to mongodb
    myclient = MongoClient("mongodb://localhost:27017/")   
    db = myclient["fortune500"] 

    #Create collection for each stock, one document for each row

    Collection = db["WMT"]
    #Drop last collection
    Collection.drop()
    Collection.insert_many(stock_data_1.to_dict('records'))

    Collection = db["AMZN"]
    #Drop last collection
    Collection.drop()
    Collection.insert_many(stock_data_2.to_dict('records'))

    Collection = db["XOM"]
    #Drop last collection
    Collection.drop()
    Collection.insert_many(stock_data_3.to_dict('records'))

    Collection = db["AAPL"]
    #Drop last collection
    Collection.drop()
    Collection.insert_many(stock_data_4.to_dict('records'))

    Collection = db["CVS"]
    #Drop last collection
    Collection.drop()
    Collection.insert_many(stock_data_5.to_dict('records'))