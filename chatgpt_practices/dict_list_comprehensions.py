numbers = [1, 2, 3, 4, 5, 6, 7, 8]

squared_list = [number ** 2 for number in numbers]
print(squared_list)

words = ["hello", "world", "python", "rocks"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

words = ["apple", "banana", "avocado", "grape", "apricot"]
start_with_a = [word.upper() for word in words if word.startswith("a")]#or word[0] == "a"
print(start_with_a)

nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
complete_list = [number for number in numbers]
print(complete_list)

numbers = [1, 2, 3, 4, 5, 6]
squares_dict = {key: key ** 2 for key in numbers }
print(squares_dict)

people = {"Alice": 25, "Bob": 17, "Charlie": 19, "David": 15}
legal_age = {key: people[key] for key in people if people[key] > 18}
print(legal_age)

original = {"a": 1, "b": 2, "c": 3}
shuffle_dict = {original[key]: key for key in original}
print(shuffle_dict)

numbers = {1: "one", 2: "two", 3: "three"}
for key in numbers:
    print(f"{key} = {numbers[key]}")

data = {"a": 10, "b": 20, "c": "hello", "d": 30}

new_data = {key: value * 2 for key, value in data.items() if isinstance(value, int)}

for key in data:
    if isinstance(data[key], int):
        print({key: data[key] * 2})