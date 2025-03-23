# Pattren of Half pyramid
rows = int(input("Enter the value of n: "))
for i in range(0, rows):
    # Nested loop for each coloumn
    for j in range(0, i + 1):
        # Print Star
        print("*",end='')
    # New line after each row
    print("\r")
