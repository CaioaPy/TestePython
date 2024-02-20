done = False
num1 = input("Hello! I'm here to help you with a simple math operation. Choose the first number: ")
num2 = input("Nice! Now choose the second number: ")
while done == False:
  op = input("Now, what would you like to do with these numbers? (add, subtract, multiply, divide)")
  if op == "add" or op == "+":
    utimoa = float(num1) + float(num2)
    print("The answer is: " + str(utimoa))
    done = True
  elif op == "subtract" or op == "-":
    utimos = float(num1) - float(num2)
    print("The answer is: " + str(utimos))
    done = True
  elif op == "multiply" or op == "*":
    utimom = float(num1) * float(num2)
    print("The answer is: " + str(utimom))
    done = True
  elif op == "divide" or op == "/":
    utimod = float(num1) / float(num2)
    print("The answer is: " + str(utimod))
    done = True
  else:
    print("Invalid. Try again.")

# funcionavel B)
