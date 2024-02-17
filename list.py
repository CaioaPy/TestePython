list = ["Oscar", "User", "Claire", "John", "Dazai"]
user = input("Hello, who are you?")
list.insert(0, user)
list.remove("User")
que = input("Do you want to see the list of students?")
if que == "yes":
    print(list)
elif que != "yes":
    print("Ok, that's all!")