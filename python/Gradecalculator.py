#Grade calculator
m = int(input("Marks in Math: "))
s = int(input("Marks in Scince: "))
e = int(input("Marks in English: "))
total_marks = m+e+s
average = total_marks/3

percentage = (total_marks/300)*100
grade = ""
if percentage > 90:
    grade = "A"
elif percentage > 80 and percentage<=90:
    grade = "B"
elif percentage > 70 and percentage<=80:
    grade = "C"
else:
    grade = "P"

print(f"Total Marks: {total_marks} \nAverage Marks: {average} \nGrade: {grade}")