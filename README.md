EXPLORE THE FORTUNE500

The Fortune 500 list is like an ultimate business scorecard for the companies. The 500 that made the 2020 list represent two-thirds of the U.S. economy, with $14 trillion in revenue.

Why care about Fortune 500 analysis? 
Simple.
You could be an investor doing a research on the stock prices or sector analysis. You might be searching for a sales lead. You could be a future entrepreneur. Or better yet you might be looking for a new job like us.

Visualizations  
With the map, you can find the U.S. headquarters for each company on the list. 
With stock analysis, you can analyze the top five fortune 500.
With the sector analysis, you  can do in-depth financial analysis at a sector level.

DATA SOURCES:
https://www.someka.net/excel-template/fortune-500-excel-list/#reviews
https://www.kaggle.com/Eruditepanda/fortune-1000-2018 
https://finance.yahoo.com

DATABASE: MONGO DB

DATA LOAD AND CLEANSING:
The  two CSV files with fortune 500 company information is loaded to Mongo DB using pandas. The data is cleaned to include only relevant information. The two dataframes were merged on the company name.

For stock data- We are reading the latest daily stock data using pandas datareader  from yahoo finance. The stock data is dynamically loaded to the mongo DB using before_first_request route in app.py .

Coding approach
Python flask and pymongo to set up mongo connection and get the data from the mongo DB. And app routes to get the json response to render the web pages.
HTML/CSS and JavaScript for the frontend  and visualization logics.
Java script libraries used 
D3							
Leaflet
Marker cluster
jquery
Fusion charts
