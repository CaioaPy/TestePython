list = []
def listadd():
    add = input("what would you like to add to the list?")
    my_bool = input("that should be added at the first position? (yes/no)")
    if my_bool == "yes":
        first = True
    else:
        first = False
    if first :
        list.insert(0, add)
    else:
        list.insert(add)
listadd()
print(list)