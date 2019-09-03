
checklist = list()
# Create
def create(item):
    checklist.append(item)
# read
def read(index):
    return checklist[int(index)]
#update
def update(index, item):
    checklist[index] = item
#destroy
def destroy(index):
    checklist.pop(index)

def printChecklist():
    i = 0
    for item in checklist:
        print("{} {}".format(i, checklist))
        i+=1
def mark_completed(index):
    update(index, "√"+checklist[index])
def mark_unchecked(index):
    update(index, checklist[index])

def select(function_code):
    function_code = function_code.lower()
    # Create item
    if function_code == "c":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "r":
        item_index = user_input("Index Number?")

        try:
            read(item_index)
        except:
            print("That is not a valid index")

    # Print all items
    elif function_code == "p":
        list_all_items()

    elif function_code == "q":
        return False

    #modify index specified item
    elif function_code == "u":
        itemIndex = user_input("input index")
        updatedItem = user_input("input new item")
        try:
            update(itemIndex,updatedItem)
        except:
            print("That is not a valid index")

    elif function_code == "d":
        itemIndex = user_input("Enter index")
        try:
            destroy(itemIndex)
        except:
            print("That is not a valid index")
    #add checkmark to item
    elif function_code == "m":
        itemIndex = user_input("Enter Index")
        try:
            mark_completed(itemIndex)
        except:
            print("That is not a valid index")
    elif function_code == "o":
        itemIndex = user_input("Enter Index")
        try:
            mark_unchecked(itemIndex)
        except:
            print("That is not a valid index")
    # Catch all
    else:
        print("Unknown Option")
        return true

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    printChecklist()
    mark_completed(0)
    print(checklist[0])
    select("C")
    printChecklist()
    select("R")
    printChecklist()
    user_value = user_input("Please Enter a value:")
    print(user_value)


running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list, D to remove from list, U to update the item, P to list all items, m to mark an item as checked, O to uncheck, and Q to quit")
    running = select(selection)
