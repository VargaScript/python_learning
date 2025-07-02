def print_numbers(limit):
    for number in range (1, limit + 1):
        print(number)

print_numbers(10)


def sum_numbers(numbers_list):
    total_sum = 0
    for number in numbers_list:
        total_sum += number
    return total_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print(sum_numbers(numbers))


def print_multiplication_table(limit_x, limit_y):
    for number_x in range(1, limit_x + 1):
        for number_y in range(1, limit_y + 1):
            multiplication = number_x * number_y
            print(f"{number_x} x {number_y} = {multiplication}")
        print()

print_multiplication_table(10, 10)


def removing_vowels(sentence):
    vowels = "aeiou"
    without_vowels = []

    for letter in sentence.lower():
        if letter not in vowels:
            without_vowels.append(letter)
    return "".join(without_vowels)

name = "Adair Isai Vargas Pastrana"
print("Here's the sentence without vowels:", removing_vowels(name))

def find_prime_numbers(numbers):
    prime_numbers = []
    for number in numbers:
        if number % number == 1 or 1 % number == number:
            prime_numbers.append(number)
    return "T", prime_numbers

range = range(1, 100)
print(find_prime_numbers(range))