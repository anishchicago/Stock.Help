
'''
INVESTOR LOOKS UP SCORES BY STOCK, ANALYST, INDUSTRY
'''

from factom_api import *
from csv_helper import *

analyst_db = 'analyst_ids.csv'
stocks_db = 'stock_ids.csv'

def _lookup_by_analyst(analyst_username, ticker, industry):
    result = []
    analyst_chain_id = db_lookup(analyst_db, analyst_username)
    if analyst_chain_id is None:
        return None
    if ticker is None or ticker == "":
        if industry is None or industry == "":
            all_tickers = get_keys(stocks_db)
            for ticker in all_tickers:
                result.append([chain_entry_search(analyst_chain_id,
                                      [ticker])])
            return result
        else:
            return chain_entry_search(analyst_chain_id,
                                      [industry])
    else:
        if industry is None or industry == "":
            return chain_entry_search(analyst_chain_id,
                                  [ticker])
        else:
            return chain_entry_search(analyst_chain_id,
                                      [ticker,industry])


def lookup(analyst_username=None, ticker=None, industry=None):
    assert ((analyst_username is not None) or \
            (ticker is not None) or \
            (industry is not None))
    if ticker != "":
        myTicker =  None
    else:
        myTicker = ticker
    if industry != "":
        myIndustry = None
    else:
        myIndustry = industry
    if analyst_username is not None and analyst_username != "":
        return _lookup_by_analyst(analyst_username=analyst_username,ticker=myTicker, industry=myIndustry)
    else:
        if myTicker is None or myTicker == "":
            result = []
            if myIndustry is None or myIndustry == "":
                all_tickers = get_keys(stocks_db)
                for myTicker in all_tickers:
                    result.append([chain_search([myTicker])])
                return result
            else:
                return chain_search([myIndustry])
        else:
            if myIndustry is None or myIndustry == "":
                return chain_search([myTicker])
            else:
                return chain_search([myTicker,myIndustry])



#print(lookup(analyst_username='anish.bhatnagar1',ticker=None,industry=None))

#print(chain_search(["test", "AAPL", "2019-09-01"]))

#print(chain_entry_search("95dc284cf654bc99a9314a780a8fbf8cf99eecdb6d0c739ec5d8c7746c672784", ["anishb","AAPL",]))

#print(chain_info('95dc284cf654bc99a9314a780a8fbf8cf99eecdb6d0c739ec5d8c7746c672784'))

