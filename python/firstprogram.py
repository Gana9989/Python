#ASCII VALUES ORD
char_a = 'A'
char_b = 'B'
ascii_a = ord(char_a)
ascii_b = ord(char_b)

print(ascii_a)
print(ascii_b)

#ASCII VALUES CHAR
ascii_value = 65
character = chr(ascii_value)
print("Charecter of ASCII value 65 is: ",character)

#Operators
a = 89
b = 59

result1 = a + b
result2 = a - b
result3 = a * b
result4 = a / b
print(result1,result2,result3,result4)

# EXPONENTIAL(squaring two numbers)

i = 2
j = 2

result = i ** j

print(result)

#Integer division(Floor division)
i = 10
j = 3

result = i // j
print(result)

#modulo operation(Remainder)

i = 10
j = 3

result = i % j
print(result)

# ADD AND ASSIGN 

a = 10
b = 20

a += b #or a = a + b

print(a)

#subract and assign

a = 10
b = 20

a -= b

print(a)

#comparision operaters

a = 10
b = 20


print(a==b)
print(a!=b)
print(a>b)
print(a<b)

#logical operater:AND
a = True
b = False

c = a and b

print(c)

#tuple example
t =[1,2,3]
print(1 in t)
print(10 not in t)

#Member Ship operators

fruits = ['apple', 'orange', 'banana', 'grape']

is_apple_in_list = 'apple' in fruits
print("apple is in the list: ", is_apple_in_list)


#Identify operaters
name1 = "Gana"
name2 = "Gana"

result = name1 is not name2

print(result)

#Checking == operator

name1 = "Gana"
name2 = "Gana"

result = name1 == name2
print(result)
