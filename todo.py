print("Welcome to my to-do list app!")
my_list = []
# save the newly inputted item
while True:
    new_item = input("Please enter a new item or 'q' to quit:")
    if new_item == 'q':
        print("Goodbye!")
        break
    else:
        my_list.append(new_item) # add new item to list
        print(my_list)