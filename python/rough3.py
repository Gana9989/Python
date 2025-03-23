"""
IT IS JUST A ROUGH PRACTICE THAT IF ICASE I HAVE A COMPANY GANA IT THE JOB ALLOTEMENTS ARE OPEND 
THE REQUIRED CGPA OF THE EMPLOYER IS >7.5 
"""
aggregrate = float(input("Please enter your aggregate: "))
experiance = float(input("Please enter your experiance: "))

if aggregrate >= 9.5:
    if experiance >= 4:
        print("very much congratulations!!")
        print("You are directly eligible as manager of the it sector")
    else:
        print("Congrates you are eligible as software leading engineer")
elif aggregrate >= 8.5:
    if experiance >= 2:
        print("congrates you are eligible for web devloper of our company")
    else:
        print("Congrates you are eligible as junior software devloper")
elif aggregrate >= 7.5:
    if experiance >= 2:
        print("Congrates!!! you are eligible for junior webdevloper interveiw")
    else:
        print("ongrates you are eligible for junior software engineer interveiw")
else:
    print("Sorry!!!Yoy are not eligible to apply for this job")


    



