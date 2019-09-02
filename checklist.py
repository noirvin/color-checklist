
checklist = list()
# Create
def create(item):
    checklist.append(item)
# read
def read(index):
    return checklist[index]
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

    # Catch all
    else:
        print("Unknown Option")
        
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
test()
