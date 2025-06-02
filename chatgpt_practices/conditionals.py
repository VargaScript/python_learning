import string

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

print(is_leap_year(300))

def check_number(number):
    printed_message = ""
    if number > 0:
        printed_message = f"The number {number} is positive"
    elif number < 0:
        printed_message = f"The number {number} is negative"
    else:
        printed_message = f"The number is {number}"
    return printed_message

digit = 1
print(check_number(digit))

def classify_triangle(side_a, side_b, side_c):
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        return "Not a triangle"
    if side_a == side_b == side_c:
        return "Equilateral"
    elif (side_a == side_b) or (side_a == side_c) or (side_b == side_c):
        return "Isosceles"
    else:
        return "Scalene"

first, second, third = 1, 2, 3
print(classify_triangle(first, second, third))

def password_strength(password: str):
    splitted_password = password.split()
    if (len(password >= 8) and splitted_password in string.ascii_letters and splitted_password in string.digits  and splitted_password in string.punctuation):
        return "Strong"
    elif ():
        return "Moderate"
    else:
        return "Weak"

password_try = "Varga$295478"
print(password_strength(password_try))