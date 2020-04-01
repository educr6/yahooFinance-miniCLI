import argparse




def configureStocksCLI():
    parser = argparse.ArgumentParser(description="Give stocks information from yahoo finance")
    addStockTickerArgumentToArgsParser(parser)


def addStockTickerArgumentToArgsParser(parser):
    parser.add_argument("Stock", help="Ticker of the stock you want to check")



def main():
    print("Hello World")


if __name__ == "__main__":
    main()
    