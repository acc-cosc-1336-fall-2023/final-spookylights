import question_d

def display_menu():
    print("1- Run Get Most Likely Ancestor Consensus")
    print("2- Exit")

def run_menu():
    display_menu()
    choice = input("Please make a selection from the above menu.")

    if choice == '1':
        run_option_1()
    elif choice == '2':
        print("Goodbye!")
        exit()
    else:
        print("Please make a selection from the menu.")
        run_menu()

def run_option_1():

    dna_string1 = input("Input DNA string 1: ")
    
    if len(dna_string1) > 8 and len(dna_string1) <= 16:
        dna_string2 = input("Input DNA string 2: ")
        if len(dna_string2) == 4:
            print("Matches found at index positions", question_d.get_most_likely_ancestor_consensus(dna_string1, dna_string2))
        else:
            print("Invalid input. String must be four characters exactly.")
            run_option_1()
    else:
        print("Invalid input. String must be greater than eight characters and less than or equal to 16 characters.")
        run_option_1()

run_menu()