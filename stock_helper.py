import requests

def StockDataCollector(symbol):

	url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=compact&apikey=Y2NWKVN6BJYISZ5A' % (symbol)
	r = requests.get(url)
	return r.json()