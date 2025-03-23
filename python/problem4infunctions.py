#Swaping two variables using functions
def swap(a,b):
    b = b + a
    a = b - a 
    b = b - a
    print(f"Value of a is: {a}")
    print(f"Value of b is: {b}")
    
swap(5,10)
swap(10,5)
swap(20,30)


