#simple calculator program(Project1)
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
operator = input("Give the operator: ")

if operator == "+":
    print(f"Addition of 2 numbers is {num1+num2}")
elif operator == "-":
    print(f"Subraction of 2 numbers is {num1-num2}")
elif operator == "*":
    print(f"Multiplication of 2 numbers is {num1*num2}")
elif operator == "/":
    print(f"Division of 2 numbers is {num1/num2}")
else:
    print("Invalid operator")





