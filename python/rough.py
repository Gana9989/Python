#Find the largest number
x,y,z = map(int, input().split(","))
largest = 0
if x > y:
    if x > z:
        largest = x
    else:
        largest = z
elif y > x:
    if y > z:
        largest = y
    else:
        largest = z
elif z > x:
    if z > y:
        largest = z
    else:
        largest = y
print("The largest number:",largest)