#Problem: Assign a letter grade based on a student's score: 
 #A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

student_score = int(input("enter the student score : "))

student_grade = False #Assume the user is not eligible by default. Later, we change it only if conditions match.

if  student_score >=90 and student_score <=100:
#90<=student_score <=100 :
    student_grade = "A"

if  80<=student_score <=89 :
    student_grade = "B"

if  70<=student_score <=79 :
    student_grade = "c"

if  60<=student_score <=69 :
    student_grade = "D"

if  student_score <60 :
    student_grade = "F"

else :
    student_grade ="Cant determine. Please provide input between 0-100"

print(f"student score is : {student_score}  hence grade is : {student_grade} ")