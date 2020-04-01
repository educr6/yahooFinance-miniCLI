import argparse
import utils




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
        print (stock)
    else:
        raise Exception("We need to scrap it")


    




if __name__ == "__main__":
    main()
    