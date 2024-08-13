print("CALCULATOR")
print("Arithmetic Operators")
num1 = float(input("num1: "))
num2 = float(input("num2: "))
print("Choose which Arithmetic operation you want to perform form 1 to 6")
print("1:+, 2:-, 3:, 4:/, 5:%, 6:*")
choice1 = int(input("ENTER YOUR CHOICE: "))
if choice1 == 1:
    print("Addition of 2 numbers is ", num1 + num2)
elif choice1 == 2:
    print("Subtraction of 2 numbers is ", num1 - num2)
elif choice1 == 3:
    print("Multiplication of 2 numbers is ", num1 * num2)
elif choice1 == 4:
    print("Division of 2 numbers is ", num1 / num2)
elif choice1 == 5:
    print("Remainder is ", num1 % num2)
elif choice1 == 6:
    print("Exponent is ", num1 ** num2)
else:
    print("Not available")