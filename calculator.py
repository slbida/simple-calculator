print("This is Sab's Calculator!") 

#take user's input
number1 = float(input("Enter your first number: "))
operation = input("Choose the operation from the following: +, -, *, / : ")
number2 = float(input("Enter your second number: "))

#performing the calculation

if operation == "+":
    answer = number1 + number2
elif operation == "-":
    answer = number1 - number2
elif operation == "*":
    answer = number1 * number2
elif operation == "/":
    answer = number1 / number2
else:
    answer = "Invalid operation! Please select from the choices and try again!"

print("Answer:", answer)