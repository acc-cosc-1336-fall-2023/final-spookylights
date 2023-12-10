class Stock:
    

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol

        
    def get_company_name(self):
        return self.__company_name

    def get_stock_list(self, stocks):
        stock_list = {}

def stock_purchase_history():
    stock_list = {
        "AAPL": Stock("AAPL", "Apple Inc"),
        "CAT": Stock("CAT", "Caterpillar"),
        "EK": Stock("EK", "Eastman Kodak"),
        "GOOG": Stock("GOOG", "Google Inc"),
        "MSFT": Stock("MSFT", "Microsoft")
    }

    print("Stock Purchase History:")
    for symbol, stock in stock_list.items():
        print(stock.get_symbol(), stock.get_company_name())