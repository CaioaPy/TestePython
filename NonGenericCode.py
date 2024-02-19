num1 = input("Hello! I'm here to help you with a simple math operation. Choose the first number: ")
num2 = input("Nice! Now choose the second number: ")
op = input("Now, what would you like to do with these numbers? (add, subtract, multiply, divide)")
if op == "add" or "+":
  utimoa = float(num1) + float(num2)
  print("The answer is: " + str(utimoa))
elif op == "subtract" or "-":
  utimos = float(num1) - float(num2)
  print("The answer is: " + str(utimos))
elif op == "multiply" or "*":
  utimom = float(num1) * float(num2)
  print("The answer is: " + str(utimom))
elif op == "divide" or "/":
  utimod = float(num1) / float(num2)
  print("The answer is: " + str(utimod))
else:
  print("Invalid. Try again.")

# funcionavel B)
