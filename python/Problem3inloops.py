#PRINT EVEN NUMBERS FROM 1 TO N
n = int(input("Give value of n: "))
#in for loop
for i in range(2,n+1,2):
    print(i)
#in while loop

i = 2
while i<=n:
    print(i)
    i+=2

#By using module - swaroop anna method
n = int(input("Give value of n: "))
i = 1
while i <= n:
    if i%2 == 0:
        print(i)
    i+=1

#By using continue
n = int(input("Give value of n: "))

i = 1

while i<=n:
    if not (i%2 == 0):
        i+=1

        continue
    print(i)
    i+=1


