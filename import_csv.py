import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('Data/fortune1000-final.csv', encoding = 'ISO-8859-1')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient('mongodb://localhost:27017/fortune1000') 
db=mongo_client.fortune1000
db.companyList.drop()
header= [ "rank", "title", "Previous Rank", "Revenues ($M)", "Revenue Change", "Profits ($M)", "Profit Change", "Assets ($M)", "Mkt Value as of 3/29/18 ($M)", "Employees", "CEO", "CEO Title", "Sector", "Industry" ,"Years on Fortune 500 List", "City", "State", "Latitude", "Longitude"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.companyList.insert(row)