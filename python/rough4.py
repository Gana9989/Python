a = float(input("Enter the value of a: "))
e = int(input("Enter the value of e: "))

if a >= 9.3:
    if e >= 3:
        print("Congratulations!!!")
        print("YOU ARE DIRECLTLY ELIGIBLE AS TEAM MANNAGER")
    else:
        print("Congratulations!!!")
        print("you are directly eligible as engineer")
elif a >= 8.5:
    if e >= 3:
        print("Congrats!! you are directly elegible as senior engineer")
    else:
        print("Congrats!! you are eligible as junior engineer")
elif a >= 7.5:
    if e >= 2:
        print("Congrats you are employed for interview")
    else:
        print("Congrats you are eligible to written antrence Test")
else:
    print("Sorry you are not eligible to apply for this job")