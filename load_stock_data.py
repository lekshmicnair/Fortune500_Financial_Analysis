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

    # Making Connection 
    myclient = MongoClient("mongodb://localhost:27017/")  
    # database  
    db = myclient["fortune500"] 

    ###Rank1- Insert stock data into Mongo DB
    # Created or Switched to collection  
    Collection = db["Walmart"]
    #Drop last collection
    Collection.drop()
    #Insert to Mongo
    stock_data_1.reset_index(inplace=True)
    data_dict = stock_data_1.to_dict("records")
    Collection.insert_one({"index":"Date","data":data_dict})

    ###Rank2- Insert stock data into Mongo DB
    # Created or Switched to collection  
    Collection = db["Amazon"] 
    #Drop last collection
    Collection.drop()
    #Insert to Mongo
    stock_data_2.reset_index(inplace=True)
    data_dict = stock_data_2.to_dict("records")
    Collection.insert_one({"index":"Date","data":data_dict})

    ###Rank3- Insert stock data into Mongo DB
    # Created or Switched to collection  
    Collection = db["ExxonMobil"] 
    #Drop last collection
    Collection.drop()
    #Insert to Mongo
    stock_data_3.reset_index(inplace=True)
    data_dict = stock_data_3.to_dict("records")
    Collection.insert_one({"index":"Date","data":data_dict})

    ###Rank4- Insert stock data into Mongo DB
    # Created or Switched to collection  
    Collection = db["Apple"] 
    #Drop last collection
    Collection.drop()
    #Insert to Mongo
    stock_data_4.reset_index(inplace=True)
    data_dict = stock_data_4.to_dict("records")
    Collection.insert_one({"index":"Date","data":data_dict})

    ###Rank5- Insert stock data into Mongo DB
    # Created or Switched to collection  
    Collection = db["CVS"] 
    #Drop last collection
    Collection.drop()
    #Insert to Mongo
    stock_data_5.reset_index(inplace=True)
    data_dict = stock_data_5.to_dict("records")
    Collection.insert_one({"index":"Date","data":data_dict})