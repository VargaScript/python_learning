"""import random

password_length = int(input("Type a number to generate the length of your password: "))
password_strength =  int(input(""""""Choose an option to generate the strength of your password:
1. Low
2. Medium
3. Strong"""
"""""))

low = "abcdefghijklmnopqrstuvwxyz0123456789"
medium = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
strong = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@{}+´.,-|°=)(/#$%&?¡¿"

def generate_password(password_strength, password_length):
    if password_strength in [1, 2, 3]:
        try:
            password = []

            if password_strength == 1:
                password = [random.choice(low) for _ in range(password_length)]
            elif password_strength == 2:
                password = [random.choice(medium) for _ in range(password_length)]
            elif password_strength == 3:
                password = [random.choice(strong) for _ in range(password_length)]
            else:
                print("Choose a right strength and length")

            return print(f"Here´s your password: {"".join(password)}. Take a photo, write it down or download it, this must be the last time you see it")
        except Exception as e:
            print("Error: ", e)
    else:
        print("Choose a number between 1 to 3")

generate_password(password_strength, password_length)"""

import random
import string

# Define character sets using string module
LOW = string.ascii_lowercase + string.digits
MEDIUM = string.ascii_letters + string.digits
STRONG = string.ascii_letters + string.digits + string.punctuation

# Get user input with validation
try:
    password_length = int(input("Type a number to generate the length of your password: "))
    password_strength = int(input("""Choose an option to generate the strength of your password: 
1. Low
2. Medium
3. Strong
"""))

    if password_strength not in [1, 2, 3]:
        raise ValueError("Invalid choice. Select 1 (Low), 2 (Medium), or 3 (Strong).")
    if password_length < 1:
        raise ValueError("Password length must be at least 1.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

def generate_password(password_strength, password_length):
    # Select character set based on strength
    char_set = LOW if password_strength == 1 else MEDIUM if password_strength == 2 else STRONG

    # Generate password and shuffle for better randomness
    password = random.sample(char_set, password_length) if password_length <= len(char_set) else [
        random.choice(char_set) for _ in range(password_length)]
    random.shuffle(password)

    return "".join(password)


# Generate and print the password
generated_password = generate_password(password_strength, password_length)
print(
    f"Here’s your password: {generated_password}\nTake a photo, write it down, or store it securely. This must be the last time you see it.")