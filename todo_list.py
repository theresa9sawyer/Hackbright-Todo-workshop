"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""
# This function needs to return something
def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    new_item = raw_input("What would you like to add to your list?")
    my_list.append(new_item)
    print my_list

# This function needs to print
def view_list(my_list):
    """Print each item in the list."""
    print my_list

def delete_first_item(my_list):
    del my_list[0]
    print my_list

# This function needs to return something
def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""
    


    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
    D. Delete first item from list
    >>> """



    while True:
        # Collect input and include your if/elif/else statements here.
        choice = raw_input(user_options)
        if choice == 'A':
            add_to_list(my_list)
        elif choice == 'B':
            view_list(my_list)
        elif choice == 'D':
            delete_first_item(my_list)
        else:

            break

#-------------------------------------------------

my_list = []
display_main_menu(my_list)

