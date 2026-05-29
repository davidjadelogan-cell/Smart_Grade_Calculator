# Smart Grade Calculator for Students.

# This prompts the user to enter the test score, assignment score and exam score. 
student_testscore = int(input("Enter your test score ( /100): "))
student_assignmentscore = int(input("Enter your assignment score ( /100): "))
student_examscore = int(input("Enter your exam score ( /100): "))

# This calculates the total score and average score of the student.
total = student_testscore + student_assignmentscore  + student_examscore
average = total / 3

print(f"Your average score is {round(average, 2)}")

# This checks if the student passed or failed based on the average score and also checks eligbility for awards 
# then prints out the appopriate message.
if average >= 75 and average <= 100:
        print("congratulations! you passed with distinction\nYou are eligible for the honors roll award.")
elif average >= 50 and average <= 75:
        print("Congratulations! You passed.")
else:
    print("you failed, try harder next time.")

