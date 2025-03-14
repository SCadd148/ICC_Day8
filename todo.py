
# save the newly inputted item
# idea: pretty print the list (1 item on each line)
# idea: clear the screen after we print the list
# idea: delete item from the list
# idea: edit an item in the list
# idea: add numbers to the items when I print them out

import os 
def my_clear_func():
    os.system('cls' if os.name == 'nt' else 'clear')

my_clear_func()
print("Welcome to my to-do list app!")
my_list = []
while True:
    new_item = input("Please enter a new item or 'q' to quit:")
    if new_item == 'q':
        print("Goodbye!")
        break
    else:
        my_list.append(new_item) # add new item to list
        my_clear_func()
        print("My List:")
        for item in my_list:
            print("- " + item)