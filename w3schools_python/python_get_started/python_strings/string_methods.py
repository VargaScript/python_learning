#capitalize()----------------------------------------------------------------------------------------------------------------------
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "python is FUN!"
x = txt.capitalize()
print (x)

txt = "36 is my age."
x = txt.capitalize()
print (x)

#casefold()----------------------------------------------------------------------------------------------------------------------
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#center(width, char)----------------------------------------------------------------------------------------------------------------------
txt = "banana"
x = txt.center(20)
print(x)

txt = "apple"
x = txt.center(20, "%")
print(x)

#count(value, start, end)----------------------------------------------------------------------------------------------------------------------
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 0, 19)
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

#encode(encoding, errors)----------------------------------------------------------------------------------------------------------------------
txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

#endswith(value, start, end)----------------------------------------------------------------------------------------------------------------------
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

#expandtabs(tabsize)----------------------------------------------------------------------------------------------------------------------
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(4)
print(x)

txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#find(value, start, end)----------------------------------------------------------------------------------------------------------------------
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
length = len("welcome")
print(f"The index of the word begins at index {x} and ends at {x + length - 1}")

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))

#format()----------------------------------------------------------------------------------------------------------------------
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

#format_map()----------------------------------------------------------------------------------------------------------------------
#index()----------------------------------------------------------------------------------------------------------------------
#isalnum()----------------------------------------------------------------------------------------------------------------------
#isalpha()----------------------------------------------------------------------------------------------------------------------
#isascii()----------------------------------------------------------------------------------------------------------------------
#isdecimal()----------------------------------------------------------------------------------------------------------------------
#isdigit()----------------------------------------------------------------------------------------------------------------------
#isidentifier()----------------------------------------------------------------------------------------------------------------------
#islower()----------------------------------------------------------------------------------------------------------------------
#isnumeric()----------------------------------------------------------------------------------------------------------------------
#isprintable()----------------------------------------------------------------------------------------------------------------------
#isspace()----------------------------------------------------------------------------------------------------------------------
#istitle()----------------------------------------------------------------------------------------------------------------------
#isupper()----------------------------------------------------------------------------------------------------------------------
#join()----------------------------------------------------------------------------------------------------------------------
#ljust()----------------------------------------------------------------------------------------------------------------------
#lower()----------------------------------------------------------------------------------------------------------------------
#lstrip()----------------------------------------------------------------------------------------------------------------------
#maketrans()----------------------------------------------------------------------------------------------------------------------
#partition()----------------------------------------------------------------------------------------------------------------------
#replace()----------------------------------------------------------------------------------------------------------------------
#rfind()----------------------------------------------------------------------------------------------------------------------
#rindex()----------------------------------------------------------------------------------------------------------------------
#rjust()----------------------------------------------------------------------------------------------------------------------
#rpartition()----------------------------------------------------------------------------------------------------------------------
#rsplit()----------------------------------------------------------------------------------------------------------------------
#rstrip()----------------------------------------------------------------------------------------------------------------------
#split()----------------------------------------------------------------------------------------------------------------------
#splitlines()----------------------------------------------------------------------------------------------------------------------
#startswith()----------------------------------------------------------------------------------------------------------------------
#strip()----------------------------------------------------------------------------------------------------------------------
#swapcase()----------------------------------------------------------------------------------------------------------------------
#title()----------------------------------------------------------------------------------------------------------------------
#translate()----------------------------------------------------------------------------------------------------------------------
#upper()----------------------------------------------------------------------------------------------------------------------
#zfill()----------------------------------------------------------------------------------------------------------------------