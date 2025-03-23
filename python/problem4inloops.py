#Print odd Number from 1 to N
n = int(input("Give value of n: "))

# # Method - 1
i = 1
while i <= n:
    if not (i%2 == 0):
        print(i)
    i+=1

# Method - 2

for i in range(1, n+1):
    if not (i%2 == 0):
        print(i)

#Method - 3

i = 1
while i <= n:
    if(i % 2 == 0):

        i += 1
        continue
    print(i)
    i += 1