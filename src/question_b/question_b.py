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

def get_stock_list():
    stock_list = {}
    in_file = open("src/question_b/stocklist.dat", "r")
    for line in in_file:
        symbol, company_name = line.split(",")
        stock = Stock(symbol, company_name)
        stock_list[symbol] = stock
    return stock_list

