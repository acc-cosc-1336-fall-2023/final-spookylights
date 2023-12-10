import question_a

def display_menu():
    print("1- Loop through the multiplication table")
    print("2- Display the multiplication table")
    print("3- Exit")

def run_menu():
    display_menu()
    choice = input("Please select an option from the menu.")

    if choice == '1':
        run_option_1()
    elif choice == '2':
        run_option_2()
    elif choice == '3':
        print("Goodbye!")
        exit()
    else:
        print("Please make a selection from the menu options.")
        run_menu()

def run_option_1():
    mtable = question_a.create_multiplication_table()
   
    for i in range(len(mtable)):
        
        for j in range(len(mtable[i])):
            print(mtable[i][j], end=' ')
            
        
        

    choice = input("\nDo you want to print again? y/n")

    if choice.lower() == 'y':
        run_option_1()
    else:
        run_menu()

def run_option_2():
    mtable_list = question_a.create_multiplication_table()
    question_a.display_multiplication_table(mtable_list)
    choice = input("Do you want to print the table again? y/n")

    if choice.lower() == 'y':
        run_option_2()
    else:
        run_menu()

run_menu()


