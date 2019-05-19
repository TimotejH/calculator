user_name = input("Enter your user name: ")
print( "Hello " + user_name + " the calculator awaits")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

operation = input("Choose your mathematical operation (+, -, *, /): ")

if operation == "+":
    print(first_number + second_number)

elif operation == "-":
    print(first_number - second_number)

elif operation == "*":
    print(first_number * second_number)

elif operation == "/":
    print(first_number / second_number)

else:
    print("You have not entered the correct mathematical operation.")
