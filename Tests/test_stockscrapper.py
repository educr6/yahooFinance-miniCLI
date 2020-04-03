import pytest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import utils
import stockscrapper

dummyDB = "./stocksdummy.json"
urlJsonPath  = "./yahooFinanceURLs.json"


def test_getYahooFinanceStockUrlWithoutTicker():
    assert "https://finance.yahoo.com/quote/" == stockscrapper.getYahooFinanceStockUrlWithoutTicker(urlJsonPath)

def test_getYahooFinanceStockUrl():
    assert "https://finance.yahoo.com/quote/AAPL/" == stockscrapper.getYahooFinanceStockUrl("AAPL",urlJsonPath)


