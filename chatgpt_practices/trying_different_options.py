numbers = range(0, 11)
squared_numbers_list_object = list(map(lambda x: x ** 2, numbers))
print("Result of squared numbers with map and lambda: ", squared_numbers_list_object)

squared_numbers_list_comprehension = [x ** 2 for x in range(len(numbers))]
print("Result of squared numbers with list comprehension: ", squared_numbers_list_comprehension)

squared_numbers_with_loop = []
for x in range(len(numbers)):
    squared_numbers_with_loop.append(x ** 2)
print("Result of squared numbers with loop: ", squared_numbers_with_loop)