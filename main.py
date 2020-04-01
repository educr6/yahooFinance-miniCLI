import argparse




def configureStocksCLIparser():
    parser = argparse.ArgumentParser(description="Give stocks information from yahoo finance")
    addStockTickerArgumentToArgsParser(parser)
    return parser


def addStockTickerArgumentToArgsParser(parser):
    parser.add_argument("Stock", help="Ticker of the stock you want to check")



def main():
    print("Hello World")
    parser = configureStocksCLIparser()
    args = parser.parse_args()

    print (args.Stock)




if __name__ == "__main__":
    main()
    