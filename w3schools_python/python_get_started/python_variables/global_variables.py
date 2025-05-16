x = "awesome"

def my_function():
    x = "fantastic"
    print("Python is", x)

my_function()

print("Python is", x)

def my_new_function():
    global y
    y = "fantastic"
    print("Python is", y)

my_new_function()

print("Outside the function is", y)