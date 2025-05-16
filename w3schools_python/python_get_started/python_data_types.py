x = str("Adair")
print(type(x), x, end="\n")

x = int(22)
print(type(x), x, end="\n")

x = float(22.4)
print(type(x), x, end="\n")

x = complex(1j)
print(type(x), x, end="\n")

x = list(["Adair", "Vargas", "Pastrana"])
print(type(x), x, end="\n")

x = tuple(("Adair", "Vargas", "Pastrana"))
print(type(x), x, end="\n")

x = range(1, 1000)
print(type(x), x, end="\n")

x = dict(name="Adair", age=22)
print(type(x), x, end="\n")

x = set({"Adair", "Vargas", "Pastrana"})
print(type(x), x, end="\n")

x = frozenset({"Adair", "Vargas", "Pastrana"})
print(type(x), x, end="\n")

x = bool(True)
print(type(x), x, end="\n")

x = bytes(5)
print(type(x), x, end="\n")

x = bytearray(bytes(5))
print(type(x), x, end="\n")

x = None
print(type(x), x, end="\n")
