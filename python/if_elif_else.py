w = float(input("Give the value of w: "))
a = int(input("Enter your age:"))
if w >= 90:
    print("Very much congratulations")
    print("You are directly eligible for this job")
elif w >=75:
    print("congratulations")
    print("You are eligible for interveiw")
elif w >=60 and a <=24:
    print("congrats")
    print("You are elible to write entrence test")
else:
    print("Sorry you are not eligible for this job")