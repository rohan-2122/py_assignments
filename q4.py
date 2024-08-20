def grade():
    Subjects = ["English","Hindi","Maths","Science","Social Studies"]

    marks = []

    for i in range(5):
        sub_marks = float(input(f"Enter the Marks of {Subjects[i]}: "))
        marks.append(sub_marks)

    total_marks = sum(marks)

    # Percentage
    percentage = total_marks/5

    print(f"Percentage : {percentage}")

    if percentage > 85:
        grade = 'A'
    elif percentage > 75:
        grade = 'B'    
    elif percentage > 50:
        grade = 'c'
    elif percentage > 30:
        grade = 'D'
    else:
        print("Reappear")


    print(f"Grade: {grade}")

grade()