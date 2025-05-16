"""class Persona:
    def __init__(self, name:str, age:int, balance:float, is_active:bool):
        self.name = name
        self.age = age
        self.balance = balance
        self.is_active = is_active

    def deposit(self) -> float:
        new_deposit = float(input("Input the quantity to deposit: "))
        self.balance += new_deposit
        return self.balance

    def withdraw(self) -> float:
        new_withdrawal = float(input("Input the quantity to receive: "))
        self.balance -= new_withdrawal
        return self.balance

    def activate_account(self) -> None:
        self.is_active = True

    def deactivate_account(self):
        self.is_active = False

adair = Persona("Adair", 22, 20000, True)
dhayana = Persona("Dhayana", 23, 11300, True)

adair.deposit()
dhayana.withdraw()
print(adair.balance)
print(dhayana.balance)
adair.deactivate_account()
print(adair.is_active)

"""




my_list = []

def add_elements(data_structure, element):
    data_structure.append(element)

def remove_elements(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} is not in the list")

add_elements(my_list, 33)
add_elements(my_list, True)
add_elements(my_list, "444")

print(my_list)

remove_elements(my_list, True)
remove_elements(my_list, [])
print(my_list)










def word_counter(phrase):
    container = []
    dictionary = {}

    container = phrase.split()

    for key in container:
        dictionary[key] = container.count(key)

    print("The frequency of words is: ", dictionary)

word_counter("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")