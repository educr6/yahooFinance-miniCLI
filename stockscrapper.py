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


""" def getCompanyName(ticker):


def getStockTableInfo(ticker):


def writeStockIntoDB(stock):  """

ticker = "AAPL"

url = getYahooFinanceStockUrl(ticker)
page = getYahooFinanceStockPage(ticker)

soup = BeautifulSoup(page, 'html.parser')
print (getMarketCap(soup))
 





