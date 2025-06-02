import random

""" def one_to_ten(limit):
    cycle = 0
    while cycle < limit:
        cycle += 1
        print(f"This is the cycle number {cycle}")
    print("You came to the end of the cycle")
        
call_one_to_ten = one_to_ten(10)

def sum_numbers(limit):
    cycle = 0
    sum = 0
    
    while cycle < limit:
        cycle += 1
        sum += cycle
    print(f"The complete sum of the numbers is {sum}")
    
sum_of_numbers = sum_numbers(11)
 """




def guess_number():
    target = random.randint(1, 100)
    guess = int(input("Enter a number from 1 to 100: "))

    while guess != target:
        if guess < target:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input("Try again: "))

    print(f"You're right! {guess} is the correct number.")

guess_number()