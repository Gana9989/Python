#USING TEMPRARY

# a = int(input("Give the value of a: "))
# b = int(input("Give the value of b: "))

# temp = a
# a = b
# b = temp
# print(f"Value of a is: {a}")
# print(f"Value of b is: {b}")

#With OUT USING TEMPRARY VARIABLE
a = int(input("Give the value of a: ")) 
b = int(input("Give the value of b: "))
a = a + b # a += b
b = a - b # b -= a
a = a - b # a -= b

print(f"Value of a is: {a}")
print(f"Value of b is: {b}")







