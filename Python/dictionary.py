students_marks = {"Rachit" : 62, "Vaishnavi": 75, "Shalini" : 83, "Amit" : 23, "Neha" : 45,"Rahul" : 55, "Priya": 35, "Ankit" : 88}
for students, marks in students_marks.items():
    if marks >= 90:
        grade = 'A+'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B+'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    else :
        grade = 'F'
    print(f"{students} scored {marks} and grade {grade}.")

    