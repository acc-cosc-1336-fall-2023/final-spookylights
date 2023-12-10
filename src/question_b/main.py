import question_b

stock_list = question_b.get_stock_list()

def display_main_menu():
    print("1- Display stock purchase history")
    print("2- Exit")

def run_menu():
    display_main_menu()
    choice = input("Please make a selection from the following menu.")

    if choice == '1':
        run_option_1()
    elif choice == '2':
        print("Goodbye!")
        exit()
    else:
        print("Invalid input. Please make your selection from the menu.")
        run_menu()

def run_option_1():
    print("Stock Purchase History: ")
    for symbol, stock in stock_list.items():
        print(stock.get_symbol(), stock.get_company_name())
    run_menu()

run_menu()
