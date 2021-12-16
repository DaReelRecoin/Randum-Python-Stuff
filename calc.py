
num1 = float(input("First, enter your first number: "))
oper = input("Second, input your operator: ")
num2 = float(input("Finally, enter your second number: "))

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
elif oper == "power":
    print(pow(num1, num2))
elif oper == "round":
    print(round(num1, num2))
elif oper == "floor":
    print(floor(num1))
    print(floor(num2))
elif oper == "ceiling":
    print(ceil(num1))
    print(ceil(num2))
elif oper == "remainder":
    print(mod(num1, num2))
else:
    print()
    print("Error 0: Invalid operator") 
