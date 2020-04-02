import argparse
import utils
import stockscrapper




def configureStocksCLIparser():
    parser = argparse.ArgumentParser(description="Give stocks information from yahoo finance")
    addStockTickerArgumentToArgsParser(parser)
    return parser


def addStockTickerArgumentToArgsParser(parser):
    parser.add_argument("Stock", help="Ticker of the stock you want to check")



def main():

    parser = configureStocksCLIparser()
    args = parser.parse_args()

    if utils.isStockOnDB(args.Stock):
        stock = utils.getStock(args.Stock)
        
    else:
        stock = stockscrapper.getStockFromYahooFinance(args.Stock)
        stockscrapper.writeStockIntoDB(stock)


    
    print (stock)


    




if __name__ == "__main__":
    main()
    