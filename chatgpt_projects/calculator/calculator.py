def addition(*args):
    total = 0
    for number in args:
        total += number
    return total

def subtraction(*args):
    total = args[0]
    for number in args[1:]:
        total -= number
    return total

def multiplication(*args):
    total = args[0]
    for number in args[1:]:
        total *= number
    return total

def division(*args):
    total = args[0]
    for number in args[1:]:
        if number == 0:
            return "Error: Division by zero is not allowed."
        total /= number
    return total

def exponentiation(*args):
    total = args[0]
    for number in args[1:]:
        total **= number
    return total

users_operation = int(input("""Type the number to choose an operation to perform:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
"""))

while users_operation in [1, 2, 3, 4, 5]:
    numbers_to_operate = input("Type the numbers you want to perform an operation on, separated by a space or a comma: ")

    if " " in numbers_to_operate:
        numbers_to_operate = numbers_to_operate.split()
    elif "," in numbers_to_operate:
        numbers_to_operate = numbers_to_operate.split(",")
    else:
        print("Add a correct separator")
        break

    try:
        numbers_to_operate = [int(num) for num in numbers_to_operate]
        if users_operation == 1:
            result = addition(*numbers_to_operate)
        elif users_operation == 2:
            result = subtraction(*numbers_to_operate)
        elif users_operation == 3:
            result = multiplication(*numbers_to_operate)
        elif users_operation == 4:
            result = division(*numbers_to_operate)
        elif users_operation == 5:
            result = exponentiation(*numbers_to_operate)
        else: 
            print("Type one of the five numbers to perform an operation")
            break

        print(f"Result: {result}")

        another_round = input("Want to perform another calculation? (yes/no): ")

        if another_round != "yes":
            print("Thanks for using the calculator")
            break
    except ValueError:
        print("Please enter valid numbers")
else:
    print("Try with a valid number between 1 to 5")