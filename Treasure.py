res = ""
te = ""
cabo = False
map = [
  
  [3, 2, 1], 
  [7, 9, 0], 
  [8, 4, 6],
  
]
print("Hello and welcome to the teasure hunt! Im gonna show you some cordinates, and then you have to find the teasure!")
print(str(map))
while te != "yes":
  te = input("Have you understood the map?")
  if te != "yes":
    print("Ok, I will show you the map again.\n" + str(map))
print("Ok then, lets start!")
print("The treasure your looking for is in the middle of the map, and that number can't be divided")
while cabo == False:
  res = input("Where do you think the treasure is?")
  if res == "0":
    print("Congrats you have found my bees!")
    cabo = True
  else:
    print("Try again!")
