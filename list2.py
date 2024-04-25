list = []
def listadd():
    add = input("what would you like to add to the list?")
    first = input("that should be added at the first position?")
    if first :
        list.insert(0, add)
    else:
        list.insert(add)
listadd()
print(list)