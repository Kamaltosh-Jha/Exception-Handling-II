

print("!*** WELCOME TO BASIC CALCULATOR ***!")
print("Where you can add as well as subtract")
while True:
    operation = input("Choose operation (add/subtract): ").lower()
    if operation not in ['add', 'subtract']:
        print("Invalid operation. Please enter 'add' or 'subtract'.")
        continue  # Restart the loop
    
    # Get user input for the numbers
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Validate input as numbers
    if not num1.isdigit() or not num2.isdigit():
        print("Invalid input. Please enter valid numbers.")
        continue  # Restart the loop


    # Perform the selected operation
    if operation == 'add':
        result = float(num1) + float(num2)
        print("the sum is " + str(result))
    elif operation == 'subtract':
        result = float(num1) - float(num2)
        print("the subtract is " + str(result))

    
    # Ask the user if they want to continue
    user_choice = input("Continue? (yes/no): ").lower()
    # Check if the user wants to continue
    if user_choice != 'yes':
        print("Exiting the calculator.")
        break

