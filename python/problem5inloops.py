#Multiplication table of a number
n = int(input("Give the value of n: "))
# in while loop
i = 1

while i<=10:
    print(f"{n} x {i} = {n*i}\n")
    i+=1

#in for loop
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    