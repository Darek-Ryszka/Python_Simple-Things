num1 = float(input("Type first number: "))
num2 = float(input("Type second number: "))

operation = input("Choose operation:\n"
                  "1. Additin\n"
                  "2. Subtraction\n"
                  "3. Multiplication\n"
                  "4. Division\n")

if operation == "1":
    print("Result: ", num1 + num2)
elif operation == "2":
    print("Result: ", num1 - num2)
elif operation == "3":
    print("Result: ", num1 * num2)
elif operation == "4":
    print("Result: ", num1 / num2)