#Count the number of accurences of a specific elements in a list
l = [int(item) for item in input("Give the input values: ").split(",")]
n = int(input("Give the value of n: "))
#method - 1
count = 0

for i in l:
    if i == n:
        count += 1
        
        
print("Output: ",count)
#Method - 2
c = l.count(n)
print(c)
