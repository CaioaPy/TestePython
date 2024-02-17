list = ["Oscar", "User", "Claire", "John", "Dazai"]
user = input("Hello, who are you?")
list[1] = user
que = input("Do you want to see the list of students?")
if que == "yes":
    print(list)
elif que != "yes":
    print("Ok, that's all!")