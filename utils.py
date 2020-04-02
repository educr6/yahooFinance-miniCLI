import json

def readJsonFile(filePath):

    with open(filePath) as json_file:
        data = json.load(json_file)
        return data

    
def writeJsonFile(filePath, data):

    with open(filePath, 'w') as outfile:
        json.dump(data, outfile)


def getStockDB(stocksDBpath = "./stocks.json"):
    
    stocksDB = readJsonFile(stocksDBpath)
    return stocksDB


def getStocksList(stocksDBpath = "./stocks.json"):

    stocksDB = getStockDB(stocksDBpath)
    stocksList = stocksDB["Stocks"]
    return stocksList


def getTickerList(stocksDBpath = "./stocks.json"):

    stockTickerList = []
    stocksList = getStocksList(stocksDBpath)
    
    for stock in stocksList:
        stockTickerList.append(stock['Ticker'])
    
    return stockTickerList


def getStock(ticker, stocksDBpath = "./stocks.json"):

    stocksList = getStocksList(stocksDBpath)

    for stock in stocksList:
        if stock['Ticker'] == ticker:
            return stock
    
    raise Exception('The stock with the ticker {} is not in the database'.format(ticker))


def isStockOnDB(ticker, stocksDBpath = "./stocks.json"):
    tickerList = getTickerList(stocksDBpath)
    return ticker in tickerList

def writeStockIntoDB(stock):
    
    stocksDB = getStockDB()
    stocksDB["Stocks"].append(stock)

    writeJsonFile("./stocks.json", stocksDB )




#