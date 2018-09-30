from factom_api import *
from sign_verify import *
from datetime import datetime
from csv_helper import *

BOT_PUB_KEY = '06436011af1b6b197c57bc700d0b04a3cbdec101735340764025394a14ad8fe8'

stocks_db = 'stock_ids.csv'

'''
BOT CREATES NEW STOCK
'''

def create_new_stock(ticker):
    data = sign(username='BOT',ticker=ticker, verify_key=BOT_PUB_KEY,timestamp=str(datetime.now()),
                schema="username,ticker,date,industry,verify_key,price,timestamp")
    if verify(**data):
        chain_id = create_chain(external_ids=[ticker], content=str(data))['chain_id']
        write_file(stocks_db, ticker, chain_id)

#create_new_stock('FB')

'''
BOT WRITES STOCK INFO
'''

def write_stock_info(ticker, date, industry, price):
    stock_chain_id = db_lookup(stocks_db, ticker)
    data = sign(username='BOT',ticker=ticker, date=date, industry=industry, price=price, verify_key=BOT_PUB_KEY,timestamp=str(datetime.now()))
    if verify(**data):
        return(chain_add_entry(chain_id = stock_chain_id,
                               external_ids=[ticker,date],content=str(data)))


#print(write_stock_info('FB','09-28-2017','Technology','168.73'))
#print(write_stock_info('FB','09-28-2018','Technology','164.46'))