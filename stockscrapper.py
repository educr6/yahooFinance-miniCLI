from bs4 import BeautifulSoup
import requests
import utils


def getYahooFinanceStockUrlWithoutTicker():
    yahooFinanceURLsPath = "./yahooFinanceURLs.json"
    yahooFinanceURLJson = utils.readJsonFile(yahooFinanceURLsPath)
    return yahooFinanceURLJson['stockURL']

def getYahooFinanceStockUrl(ticker):
    url = getYahooFinanceStockUrlWithoutTicker() + ticker + "/"
    return url



def getYahooFinanceStockPage(ticker):

    HTTPOKSTATUS = 200
    url = getYahooFinanceStockUrl(ticker)
    page = requests.get(url)

    if page.status_code == 200:
        return page.content
    
    raise Exception("The ticker {} could not be found in Yahoo Finance".format(ticker))



def getMarketCap(SoupObject):
     
    marketCapHtml = SoupObject.find('td', {'data-test': 'MARKET_CAP-value'})
    marketCap = marketCapHtml.span.string
    return marketCap

def getCompanyName(SoupObject):

    soup = SoupObject.find("div", {"class":"D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)" })
    companyName = soup.div.string
    companyName = removeTickerFromCompanyName(companyName)
    return companyName

def getCompanyNameWithTicker(SoupObject):
    soup = SoupObject.find("div", {"class":"D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)" })
    companyNameWithTicker = soup.div.string
    return companyNameWithTicker


def removeTickerFromCompanyName(nameWithTicker):
    NAME_INDEX = 1
    nameWithoutTicker = nameWithTicker.split('-')[NAME_INDEX][1:]
    return nameWithoutTicker

def extractTickerFromCompanyName(nameWithTicker):
    TICKER_IDEX = 0
    ticker = nameWithTicker.split('-')[TICKER_IDEX][:-1]
    return ticker


def getBeautifulSoupObject(page):
    return BeautifulSoup(page, 'html.parser')
     

def getStockTableInfo(SoupObject):

    leftTable = SoupObject.find('table', {'class': "W(100%)"})
    leftTableBody = leftTable.tbody
    allTrs = leftTableBody.find_all('tr')

    stock = {}

    for row in allTrs:
        
        content = row.find_all('td')
        info = content[0].string
        value = content[1].string

        stock[info] = value 
    
    return stock

def getAllStockInfo(SoupObject):

    companyName = getCompanyName(SoupObject)
    ticker = extractTickerFromCompanyName(getCompanyNameWithTicker(SoupObject))
    stockTableInfo = getStockTableInfo(SoupObject)

    stock = {}
    stock["Name"] = companyName
    stock["Ticker"] = ticker
    stock.update(stockTableInfo)
    return stock



def writeStockIntoDB(stock):
    
    stocksDB = utils.getStockDB()
    stocksDB["Stocks"].append(stock)

    utils.writeJsonFile("./stocks.json", stocksDB )

    return 1

def getStockFromYahooFinance(ticker):
    page = getYahooFinanceStockPage(ticker)
    soup = getBeautifulSoupObject(page)
    stock = getAllStockInfo(soup)
    return stock









