from factom_api import *
from sign_verify import *
from datetime import datetime
from csv_helper import *

BOT_PUB_KEY = '06436011af1b6b197c57bc700d0b04a3cbdec101735340764025394a14ad8fe8'

analyst_db = 'analyst_ids.csv'
stocks_db = 'stock_ids.csv'

open(analyst_db, 'a').close()
open(stocks_db, 'a').close()

'''
CREATE NEW ACTOR (ANALYST)
'''

def create_new_analyst(username, full_name, employer, email):
    if db_lookup(analyst_db, username) is not None:
        return 0
    public_key = generate_key(username).decode()
    data = sign(username=username,name=full_name,employer=employer,email=email,public_key=public_key,timestamp=str(datetime.now()),
                schema="username,ticker,date,recommendation,horizon,timestamp")
    print(verify(**data))
    chain_id = create_chain(external_ids=[username], content=str(data))['chain_id']
    write_file(analyst_db,username,chain_id)

print(create_new_analyst('anish.bhatnagar1','Anish Bhatnagar','Citi','anish.bhatnagar@citi.com'))

'''
ANALYST CREATES NEW RECOMMENDATION
'''

def add_new_rec(username, ticker, recommendation, horizon):
    chain_id = db_lookup(analyst_db, username)
    if chain_id is None:
        return 0
    data = sign(username=username,ticker=ticker,recommendation=recommendation,horizon=horizon,timestamp=str(datetime.now()))
    print(verify(**data))
    print([username,ticker,horizon])
    return chain_add_entry(chain_id = chain_id,
                               external_ids=[username,ticker,horizon],content=str(data))

print(add_new_rec('anish.bhatnagar1', 'FB', 'Buy', '2018-09-28'))

'''
BOT WRITES ANALYST SCORE FOR IND, STOCK, REGION
'''

def add_score(analyst_username, ticker, industry, score):
    analyst_chain_id = db_lookup(analyst_db, analyst_username)
    stock_chain_id = db_lookup(stocks_db, ticker)
    if analyst_chain_id is None or stock_chain_id is None:
        return 0
    data = sign(username='BOT', analyst_username=analyst_username, ticker=ticker,
                industry=industry, score=score, verify_key=BOT_PUB_KEY,timestamp=str(datetime.now()))
    if verify(**data):
        print(chain_add_entry(chain_id = analyst_chain_id,
                               external_ids=[analyst_username, ticker],content=str(data)))
        print(chain_add_entry(chain_id=analyst_chain_id,
                        external_ids=[analyst_username, industry], content=str(data)))

#add_score('anish.bhatnagar1','FB','Technology',1)

#print(chain_get_entry('d294f6e585874fe640be4ce636e6ef9e3adc27620aa3221fdcf5c0a7c11c6f67','9ae712ba61ea3f9022fcc466a8689b401849c5fed7af3f9e90ee56fe1ecf7771'))

