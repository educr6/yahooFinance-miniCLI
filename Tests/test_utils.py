import pytest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import utils

dummyDB = "../stocksdummy.json"


def test_getTickerList():

    stockList = utils.getTickerList(stocksDBpath = dummyDB)
    assert stockList == ['TSLA', 'AAPL', 'BYND', 'GOOGL', 'MA']

def test_getStocksDB():

    stockDB = utils.getStockDB(dummyDB)
    assert stockDB == {'Stocks': [{'Name': 'Tesla, Inc.', 'Ticker': 'TSLA', 'Previos Close': 524.0, 'Open': 504, 'Bid': '497.63 x 800', 'Ask': '498.49 x 900', "Day's Range": '485.70 - 513.9548', '52 Week Range': '176.99 - 968.99', 'Volume': 8948248, 'Avg. Volume': 20987232, 'TimeStamp': '2012-04-23T18:25:43.511Z'}, {'Name': 'Apple, Inc.', 'Ticker': 'AAPL', 'Previos Close': 524.0, 'Open': 504, 'Bid': '497.63 x 800', 'Ask': '498.49 x 900', "Day's Range": '485.70 - 513.9548', '52 Week Range': '176.99 - 968.99', 'Volume': 8948248, 'Avg. Volume': 20987232, 'TimeStamp': '2012-04-23T18:25:43.511Z'}, {'Name': 'Beyond Meat, Inc.', 'Ticker': 'BYND', 'Previous Close': '64.18', 'Open': '63.86', 'Bid': '61.23 x 1100', 'Ask': '61.19 x 1100', "Day's Range": '60.79 - 63.97', '52 Week Range': '45.00 - 239.71', 'Volume': '2,263,742', 'Avg. Volume': '9,800,174'}, {'Name': 'Alphabet Inc.', 'Ticker': 'GOOGL', 'Previous Close': '1,102.10', 'Open': '1,100.00', 'Bid': '1,115.06 x 800', 'Ask': '1,118.55 x 800', "Day's Range": '1,093.13 - 1,122.08', '52 Week Range': '1,008.87 - 1,530.74', 'Volume': '1,488,943', 'Avg. Volume': '2,482,117'}, {'Name': 'Mastercard Incorporated', 'Ticker': 'MA', 'Previous Close': '228.61', 'Open': '228.39', 'Bid': "236.37 x 800", 'Ask': '236.52 x 800', "Day's Range": '227.35 - 238.37', '52 Week Range': '199.99 - 347.25', 'Volume': '3,369,369', 'Avg. Volume': '6,472,506'}]}
    
def test_getStocksList():

    stocksList = utils.getStocksList(dummyDB)
    assert stocksList == [{'Name': 'Tesla, Inc.', 'Ticker': 'TSLA', 'Previos Close': 524.0, 'Open': 504, 'Bid': '497.63 x 800', 'Ask': '498.49 x 900', "Day's Range": '485.70 - 513.9548', '52 Week Range': '176.99 - 968.99', 'Volume': 8948248, 'Avg. Volume': 20987232, 'TimeStamp': '2012-04-23T18:25:43.511Z'}, {'Name': 'Apple, Inc.', 'Ticker': 'AAPL', 'Previos Close': 524.0, 'Open': 504, 'Bid': '497.63 x 800', 'Ask': '498.49 x 900', "Day's Range": '485.70 - 513.9548', '52 Week Range': '176.99 - 968.99', 'Volume': 8948248, 'Avg. Volume': 20987232, 'TimeStamp': '2012-04-23T18:25:43.511Z'}, {'Name': 'Beyond Meat, Inc.', 'Ticker': 'BYND', 'Previous Close': '64.18', 'Open': '63.86', 'Bid': '61.23 x 1100', 'Ask': '61.19 x 1100', "Day's Range": '60.79 - 63.97', '52 Week Range': '45.00 - 239.71', 'Volume': '2,263,742', 'Avg. Volume': '9,800,174'}, {'Name': 'Alphabet Inc.', 'Ticker': 'GOOGL', 'Previous Close': '1,102.10', 'Open': '1,100.00', 'Bid': '1,115.06 x 800', 'Ask': '1,118.55 x 800', "Day's Range": '1,093.13 - 1,122.08', '52 Week Range': '1,008.87 - 1,530.74', 'Volume': '1,488,943', 'Avg. Volume': '2,482,117'}, {'Name': 'Mastercard Incorporated', 'Ticker': 'MA', 'Previous Close': '228.61', 'Open': '228.39', 'Bid': "236.37 x 800", 'Ask': '236.52 x 800', "Day's Range": '227.35 - 238.37', '52 Week Range': '199.99 - 347.25', 'Volume': '3,369,369', 'Avg. Volume': '6,472,506'}]

def test_getTeslaStock():
    teslaTicker = "TSLA"

    tesla = utils.getStock(teslaTicker, dummyDB)
    assert tesla == {'Name': 'Tesla, Inc.', 'Ticker': 'TSLA', 'Previos Close': 524.0, 'Open': 504, 'Bid': '497.63 x 800', 'Ask': '498.49 x 900', "Day's Range": '485.70 - 513.9548', '52 Week Range': '176.99 - 968.99', 'Volume': 8948248, 'Avg. Volume': 20987232, 'TimeStamp': '2012-04-23T18:25:43.511Z'}

def test_getBeyondMeetStock():
    byndTicker = "BYND"

    bynd = utils.getStock(byndTicker, dummyDB)
    assert bynd == {"Name": "Beyond Meat, Inc.", "Ticker": "BYND", "Previous Close": "64.18", "Open": "63.86", "Bid": "61.23 x 1100", "Ask": "61.19 x 1100", "Day's Range": "60.79 - 63.97", "52 Week Range": "45.00 - 239.71", "Volume": "2,263,742", "Avg. Volume": "9,800,174"}

def test_isAppleOnStockDB():
    ticker = "AAPL"
    assert True == utils.isStockOnDB(ticker, dummyDB)

def test_isBeyondMeetOnStockDB():
    ticker = "BYND"
    assert True == utils.isStockOnDB(ticker, dummyDB)

def test_IsVisaOnStockDBShouldReturnFalse():
    ticker = "V"
    assert False == utils.isStockOnDB(ticker, dummyDB)



