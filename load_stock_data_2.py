import pandas as pd
import pandas_datareader.data as pdr
import datetime as dt
import time
import json
from dateutil.relativedelta import relativedelta
import pymongo
from pymongo import MongoClient

def get_stock_info():
    #Get stock info from yahoo finance using datareader
    start_date = dt.datetime.today() - relativedelta(years=1)
    end_date = dt.datetime.today()


    stock_data_1 = pdr.DataReader("WMT", 'yahoo', start_date, end_date)
    stock_data_2 = pdr.DataReader("AMZN", 'yahoo', start_date, end_date)
    stock_data_3 = pdr.DataReader("XOM", 'yahoo', start_date, end_date)
    stock_data_4 = pdr.DataReader("AAPL", 'yahoo', start_date, end_date)
    stock_data_5 = pdr.DataReader("CVS", 'yahoo', start_date, end_date)
    
    #sleep for 1 minute
    time.sleep(60)

    stock_data_1.reset_index(inplace=True)
    stock_data_2.reset_index(inplace=True)
    stock_data_3.reset_index(inplace=True)
    stock_data_4.reset_index(inplace=True)
    stock_data_5.reset_index(inplace=True)

    # Making Connection 
    myclient = MongoClient("mongodb://localhost:27017/")  
    # database  
    db = myclient["fortune500"] 

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


    