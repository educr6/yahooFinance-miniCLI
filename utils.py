import json

def readJsonFile(filePath):

    with open(filePath) as json_file:
        data = json.load(json_file)
        return data



def getStockDB():
    stocksDBpath = "./stocks.json"
    stocksDB = readJsonFile(stocksDBpath)
    return stocksDB

def getStocksList():

    stocksDB = getStockDB()
    stocksList = stocksDB["Stocks"]
    return stocksList

def getTickerList():

    stockTickerList = []
    stocksList = getStocksList()
    
    for stock in stocksList:
        stockTickerList.append(stock['Ticker'])
    
    return stockTickerList




def getStock(ticker):

    stocksList = getStocksList()

    for stock in stocksList:
        if stock['Ticker'] == ticker:
            return stock
    
    raise Exception('The stock with the ticker {} is not in the database'.format(ticker))




#