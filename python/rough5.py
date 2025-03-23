"""
Entrence application for Gana it and technoly:
PLEASE ENTER YOUR AGGREGATE AND EXPERIANCE

"""
aggregate = float(input("Please enter your aggregate: "))
experiance = float(input("Enter your experiance: "))

if aggregate >= 90:
    if experiance >= 4:
        print("Congrates!!!")
        print("You are eligible as direct team leader")
    else:
        print("Congrats!!!")
        print("You are eligible as software engineer")
elif aggregate >= 80:
    if experiance >= 4:
        print("Congrats!!!")
        print("You are eligible as software employer")
    else:
        print("Congrats!!!")
        print("You are eligible as junior it employer")
elif aggregate >= 70:
    if experiance>= 2:
        print("Congrats!!!")
        print("You are eligible for Interview")
    else:
        print("Congrats!!!")
        print("You are eligible to write entrence test")
elif aggregate >= 65:
    if experiance >= 3.5:
        print("Congrats!!!")
        print("You are eligible for Interview")
    else:
        print("Sorry!!!")
        print("You are not eligible to apply this job")
elif aggregate >= 60:
    if experiance >= 6:
        print("Congrats!!!")
        print("You are eligible for Interview")
    else:
        print("Sorry!!!")
        print("You are not eligible to apply this job")
else:
    print("Sorry!!!")
    print("You are not eligible to apply this job")
    
