

from scraper import *
from schema import *

def scrapeAll200():
    data200 = {}
    symbols = session.query(
        stocks.symbol
    ).all()

    for symbol in symbols:
        url = "https://finance.yahoo.com/quote/"+ str(symbol.symbol).upper() + ".NS/financials"
        data = getAllData(url)
        data200[symbol.symbol] = data

    return data200


allData = scrapeAll200()
# for i, j in allData.items():
#     print(i, j)
for symbol, data in allData.items():
    for title, stock_data in data.items():
        toSQL(symbol=symbol, title=title, data=stock_data)



