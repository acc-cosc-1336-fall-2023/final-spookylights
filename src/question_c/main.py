import question_c

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
    question_c.stock_purchase_history()
    run_menu()

run_menu()