#Default arguments in functions
def greet_user(name,greeting="Hello"):
    return greeting + ", " + name + "!"
greeting1 = greet_user("Bob")
greeting2 = greet_user("Charlie","Hi")

print(greeting1)
print(greeting2)
