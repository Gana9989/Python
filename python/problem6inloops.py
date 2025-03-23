#calculate the factorial of a number
n = int(input("Give the value of n: "))
factorial = 1

while n>0:
    factorial = factorial * n
    n -= 1
print(factorial)