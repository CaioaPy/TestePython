list = []
def listadd():
    add = input("what would you like to add to the list?")
    my_bool = input("that should be added at the first position? (yes/no)")
    if my_bool == "yes":
        first = True
    else:
        first = False
        return
    if first == True:
        list.insert(0, add)
    elif first == False:
        list.append(add)
def listaremove():
    remove = input("what would you like to remove from the list?")

match input("do you want to see, add or remove from list?"):
    case "see":
        print(list)