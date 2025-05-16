#1. Iterator printing the first two elements
numbers = iter([10, 20, 30, 40])
print(next(numbers))
print(next(numbers))

#2. Print an entire word manually
string = iter("Python")
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))

#3. Use iterator and handle StopIteration
"""fruits = iter(["Apple", "Banana", "Coconut", "Dandadan"])
try:
    print(next(fruits))
    print(next(fruits))
    print(next(fruits))
    print(next(fruits))
    print(next(fruits))
except StopIteration:
    raise StopIteration("Watch out, there are no more fruits!")"""

#4. Print the elements on a list using a while loop and break the code when finished
numbers = [1, 2, 3, 4]
iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

#5. Given the list, print each item with its index starting from 1
fruits = ['apple', 'banana', 'cherry']
for index, item in enumerate(fruits, start=1):
    print(index, item)

#6. Print just the even number from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for index, number in enumerate(numbers):
    if index % 2 == 0:
        print(number)
    else:
        pass

#7. Create a dictionary with a list of strings
strings = ["Adair", "Dhayana", "Monserrat", "Christian"]
dictionary = {}
for index, word in enumerate(strings):
    dictionary[index] = word

print(dictionary)

#8. Create a dictionary with countries and capitals using zip()
countries = ["Mexico", "Colombia", "United States"]
capitals = ["Mexico City", "Bogota", "Washington"]
dictionary = dict(zip(countries, capitals))
print(dictionary)

#9. Print full sentences with first name, last name and ages
first_names = ["Adair", "Monserrat", "Dhayana", "Christian"]
last_names = ["Vargas", "Vargas", "Aguilar", "Pastrana"]
ages = [22, 11, 23, 44]

zipped = list(zip(first_names, last_names, ages))
for name, last_name, age in zipped:
    print(f"Hi, my name is {zipped[nfame][1]} {zipped[0][1]} and I'm {zipped[0][2]}")
adair isai vargas pastranaasaqàaaaadfkfueruifddadir isai vargas pastrna aaasshh adair si¿i¿iiiisiajsjskjaaasdf}