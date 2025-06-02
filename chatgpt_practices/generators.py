""" def pairs_until(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

numbers_list = pairs_until(100)
print(list(numbers_list)) """


""" def read_file(file):
    with open(file) as file_read:
        for line in file_read: 
            yield line.strip()

lines = read_file("datos.txt")
print(list(lines)) """


""" numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def squares(limit):
    for number in range(limit):
        yield number ** 2

squared_numbers = squares(12)
print(list(squared_numbers)) """



def infinite_numbers():
    counter = 0
    while counter < 114:  # condición para frenar
        yield counter
        counter += 1

for num in infinite_numbers():
    print(num)


""" 
values = [1, 2, 3, 4]

def reverse(values):
    iterator = iter(values) 
    for value in iterator:
        next(value)

reversed_list = reverse(values)
print(reversed_list) """



class multipendOf():
    def __init__(self, multipend, limit):
        self.multipend = multipend
        self.limit = limit

    def __iter__(self):
        multipend

    def __next__():
        conditional_numbers = []
        for number in range(limit):
            if number % multipend == 0:
                conditional_numbers.append(number)
        return conditional_numbers

first_try = multipendOf(7, 432)

class MultiplosDe:
    def __init__(self, multiplo, limite):
        self.multiplo = multiplo
        self.limite = limite
        self.actual = 0  # Punto de partida para buscar múltiplos

    def __iter__(self):
        return self

    def __next__(self):
        while self.actual < self.limite:
            numero = self.actual
            self.actual += 1
            if numero % self.multiplo == 0:
                return numero
        raise StopIteration

first_try = multipendOf(7, 432)



""" def natural_numbers(recursion):
    if recursion == 0:
        return 1
    else:
        return recursion + natural_numbers(recursion - 1)

for number in natural_numbers(3):
    print(number)
 """


def natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + natural_numbers(n - 1)

print(natural_numbers(4))  # Imprime 6 (3 + 2 + 1 + 0)


def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else: 
        return fibonacci(number - 1) + fibonacci(number - 2) 

print(fibonacci(10))



def natural_numbers(number):
    if number == 0:
        return 0
    else:
        return number + natural_numbers(number - 1)

print(natural_numbers(5))