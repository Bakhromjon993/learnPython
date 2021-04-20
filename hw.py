import sys, time                        # importing necessary libraries

my_list = []                            # Array which will collect all shopping list items

try:
    my_file = open('list.txt', 'r')     # 'r' means "read", here system opens file and reads it
    for item in my_file:                # The strip() method removes characters from both left and right based on the argument
        my_list.append(item.strip())    # append mean to adding item that we wrote to our file.
    my_file.close()
except:
    pass

def home_page():
    print("-----------------------------")
    print("      SHOPPING LIST      ")
    print("-----------------------------")
    print('\n\nYour list contains', len(my_list), 'items.\n')
    print("Please choose from the following options:\n")
    print("(a) - Add to the list")
    print("(d) - Delete from the list")
    print("(v) - View the list")
    print("(q) - Quit the program")
    select = input('\nYour choice: ')
    if len(select) > 0:                 # len() func check the length
        if select.lower()[0] == 'a':    # lower() func transforms letters into lowercase
            add_page()                  # which means even if you type A not a it will transform into lowercase
        elif select.lower()[0] == 'd':
            delete_page()
        elif select.lower()[0] == 'v':
            view_page()
        elif select.lower()[0] == 'q':
            sys.exit()
        else:
            home_page()
    else:
        home_page()


def add_page():
    print("-------------------------------------------")
    print("     ADD SECTION    ")
    print("-------------------------------------------")
    print("\n")
    print("Please enter the name of the item that you want to add.")
    print("Press ENTER to return to the main menu.\n")
    shl_item = input("\nItem: ")
    if len(shl_item) > 0:
        my_list.append(shl_item)        #adding item from input to our shopping list array
        print('Item successfully added to your list!')
        save_list()                     # runs save function below
        time.sleep(1)                   # sleep func: Delay execution for a given number of seconds.
        add_page()                      # redirected to add page
    else:
        home_page()                     # redirected to home page

def view_page():
    print("-------------------------------------------")
    print("     VIEW SECTION    ")
    print("-------------------------------------------")
    print("\n\n")
    for item in my_list:                # looping all items from my shopping list
        print(item)                     # printing them one by one with for loop

    print("\n\n")
    print("Press enter to return to the main menu")
    input()                             # if input is empty then
    home_page()                         # redirected to home page

def delete_page():
    print("-------------------------------------------")
    print("     DELETE SECTION    ")
    print("-------------------------------------------")
    num = 0
    for item in my_list:
        print(num, ' - ', item)
        num += 1

    print("What number to delete?")
    choice = input("number: ")
    if len(choice) > 0:                 # here system check the length of item that came from input field
        try:
            del my_list[int(choice)]
            print('Item successfully deleted!')
            save_list()                 # runs save function below
            time.sleep(1)               # sleep func: Delay execution for a given number of seconds.
        except:
            print('Invalid number')
            time.sleep(1)               # sleep func: Delay execution for a given number of seconds.
        delete_page()
    else:
        home_page()


def save_list():
    my_file = open('list.txt', 'w')     # 'w' means "write"
    for list in my_list:                # all items will be looped with for func
        my_file.write(list + '\n')      # all items in array will be written to our .txt file
    my_file.close()

home_page()
