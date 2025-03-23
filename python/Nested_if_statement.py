p = float(input("Give the value of p: "))
a = int(input("Enter your age:"))
if p >= 90:
    if a >= 25:
        print("Very much congratulations")
        print("You are directly eligible for this job as a manager")
    else:
        print("Very much congratulations")
        print("You are directly eligible for this job as a software engineer")
    
elif p >=75:
    print("congratulations")
    print("You are eligible for interveiw")
elif p >=60:
    if a <= 24:
        print("congrats")
        print("You are elible to write entrence test")
    else:
        print("Sorry your age is not reached the required percentage")
else:
    print("Sorry you are not eligible for this job")    