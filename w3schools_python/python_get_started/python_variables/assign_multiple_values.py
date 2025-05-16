x, y , z = "Orange", "Apple", "Grapes"
print(x)
print(y)
print(z)

x = y = z = "Banana"
print(x)
print(y)
print(z)

fruits = ["Peach", "Watermelon", "Cherry", "Cucumber"]
x, y, z, a = fruits
print(x)
print(y)
print(z)
print(a)


languages = ["Python", "JavaScript", "TypeScript"]
one, two, three = languages
print(one)
print(two)
print(three)

value = "JavaScript"
ml = front = videogames = back = value
print(front, videogames, back, end="\n", sep="/")
print(videogames)
print(back)

numbers = [1, 2, 3, 4, 5]
first, middle, *last = numbers
print(first, middle, last, sep=";")

contestants = ["Adair", "Dhayana", "Monse", "Christian"]
a, b, c, d = contestants
print(a, b, c, d, sep="/", end="\n")

a, b, c, d = d, c, b, a
print(a, b, c, d, sep="/", end="\n")

new_languages = ["Python", "R", "Julia", "Scala"]
for index, language in enumerate(new_languages, start=1):
    print(f"The number {index} is {language}")

numbers = [10, 20, 30, 40, 50, 60]
first, *middle, last = numbers
print("First: ", first)
print("Middle: ", middle)
print("Last: ", last)

full_name = ["Adair", "Isai", "Vargas", "Pastrana"]
first_name, second_name, *last_name = full_name
print(f"The full name is {first_name} {second_name} {" ".join(last_name)}")

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

tasks = ["Clean room", "Do homework", "Exercise"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}: {task}")

words = ["AI", "ML", "Deep Learning", "Data Science", "MLOps"]
for index, word in enumerate(words, start=1):
    if index % 1 == 0:
        print(word)


#Exercises
numbers = [10, 20, 30, 40, 50, 60]
even_indices = []
odd_indices = []

for index, number in enumerate(numbers):
    if index % 2 == 0:
        even_indices.append(number)
    else:
        odd_indices.append(number)

print(even_indices)
print(odd_indices)

for index, number in enumerate(numbers):
    if index % 2 == 0:
        even_indices.append(number)
    if index % 2 == 1:
        odd_indices.append(number)

print(even_indices)
print(odd_indices)





languages = ["Python", "JavaScript", "C++", "Java"]

for index, language in enumerate(languages, start=1):
    print(f"{index}: {language}")



words = ["AI", "ML", "Deep Learning", "Data Science", "MLOps"]
for index, word in enumerate(words):
    if index > 2:
        print(f"{index}: {word}")





numbers = [10, 20, 30, 40, 50, 60]
first, *middle_numbers, last = numbers
print("First:", first)
print("Middle:", middle_numbers)
print("Last:",last)




value = "JavaScript"
ml = front = back = value
print(ml)
print(front)
print(back)
print(value)

