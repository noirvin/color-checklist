
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

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return false
    #modify index specified item
    elif function_code == "U":
        itemIndex = user_input("input index")
        updatedItem = user_input("input new item")
        update(itemIndex,updatedItem)
    elif function_code == "D":
        itemIndex = user_input("Enter index")
        destroy(itemIndex)    
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

test()
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list")
    running = select(selection)
