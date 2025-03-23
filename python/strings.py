
# STRING INDEXING

str = "PYTHON"
print(str[5])
print(str[-1])
print(str[-2])
print(str[0])

#STRING SLICING

s = 'hello world'
print(s[1])    #to solve srtring slicing we need to know that 
print(s[-1])    #1)indexing
print(s[1:3])   #2)[start : stop]
print(s[1:-1])  #3)[start : stop : step]
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])

#STRING CONCATENATION

first_name = "Gana"
last_name = "sai surya"
full_name = first_name + " " +last_name
print(full_name)


#Length of the string

string1 = "GANA SAI SURYA"
print(len(string1))

#Python string Manipulation Examples

#Define the original string
s = "Hello, world!"

#Convert the string to upper case
print(s.upper()) 

#Convert the string to lower case
print(s.lower())

#Remove leading and trailing white spaces from the string
print(s.strip())

#Replace all occurrences of 'o' with 'x' in the string
print(s.replace('o','x'))

#count the number of occurences of 'a' in the string
print('Abracadabra'.count('a'))


#string formating
name = "Gana"
age = 30

# using the '%' operator for string formatting (old-style)
print("My name is %s and iam %d years old." % (name, age))

#using the 'formet()' method for string formatting
print("My name is {} and iam {} years old.".format(name, age))

#using f-strings (formated string literals) for string formatting(python)
print(f"My name is {name} and I am {age} years old.")

#PROBLEM-1
#vowel Checking

s = "Hello, world!"
s2 = s.lower()
a = s2.count('a')
e = s2.count('e')
i = s2.count('i')
o = s2.count('o')
u = s2.count('u')

print(f"Number of vowels:{a+e+i+o+u}")

#Grade calculator
m = int(input("Marks in Math: "))
s = int(input("Marks in Scince: "))
e = int(input("Marks in English: "))
total_marks = m+e+s
average = total_marks/3

percentage = (total_marks/300)*100
grade = ""
if percentage > 90:
    grade = "A"
elif percentage > 80 and percentage<=90:
    grade = "B"
elif percentage > 70 and percentage<=80:
    grade = "C"
else:
    grade = "P"

print(f"Total Marks: {total_marks} \nAverage Marks: {average} \nGrade: {grade}")


#PALINDROME CHECKER
s = input("Give a string: ")

reverse = s[::-1]

if reverse == s:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


#LEAP YEAR CHECKING
year = int(input())

leap = False

if year%100 == 0 and year%400 != 0:
    leap = False
elif year%4 == 0:
    leap = True
else:
    leap = False

print(leap)
