#Calculate the sum of n natural numbers
n = int(input("Give the value of n: "))
#in while loop
i = 1
sum = 0
while i<=n:
    sum += i
    i+=1
print("VALUE OF SUM IN WHILE LOOP:",sum)
#in for loop
add = 0
for i in range(1,n+1):
    add += i
print("VALUE OF SUM IN FOR LOOP",add)