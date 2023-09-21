## Step-1 : Install all the required packages using pip command
#        - requests, pandas, bs4, openpyxl


## Step-2: Importing libraries
import os
import time 
from datetime import datetime
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl


## Step-3: Creating variable for all urls we have to scrape

urls = ['https://in.tradingview.com/markets/stocks-india/market-movers-large-cap/',
        'https://in.tradingview.com/markets/stocks-india/market-movers-gainers/', 
        'https://in.tradingview.com/markets/stocks-india/market-movers-losers/',
        'https://in.tradingview.com/markets/stocks-india/market-movers-best-performing/',
        'https://in.tradingview.com/markets/stocks-india/market-movers-most-volatile/',
        'https://in.tradingview.com/markets/stocks-india/market-movers-highest-revenue/']


## Step-4: Initialize the ExcelWriter object
xl_writer = pd.ExcelWriter('TradingView.xlsx', engine='openpyxl')



## Step-5: Creating a function for automating the scraping process

def Scrape_stocks(url):
        try: 
                now = datetime.now()

                # This is to get the time at the time of web scraping
                current_time = now.strftime("%H:%M:%S")

                print(f"At time : {current_time} IST")


                print(f"Scraping {url}...")

                # Create variable to get url
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "lxml")


                # Create a DataFrame to read the webpages
                df = pd.read_html(url)[0]


                # Replace hyphens with an empty string in the DataFrame
                df.replace('-', '', inplace=True)


                # Save the DataFrame to the Excel file
                df.to_excel(xl_writer, sheet_name=(url.split('/')[-2]).split('-')[-1], index=False)
                

        except Exception as e:
                print(f"Error scraping {url}: {str(e)}")


## Steo-6: Loop through the URLs and scrape & save data
for url in urls:
        Scrape_stocks(url)

## Step-7: Save and Close Excel file
xl_writer.close()







