def calculator(marks):
    if 90 <= marks <= 100:
        return 'A', 'Excellent! Keep it up!'
    elif 80 <= marks < 90:
        return 'B', 'Very Good! Keep it up!'
    elif 70 <= marks < 80:
        return 'C', 'Good effort! You can do better! '
    elif 60 <= marks < 70:
        return 'D', 'Needs improvement'
    else:
        return 'F', 'Keep trying! You can improve with practice!'

while True:
    try:
        name = input("Enter studen name: ")
        marks = int(input("Enter marks: "))
        if 0 <= marks <= 100:
            grade, message = calculator(marks)
            print(f"Result for {name.upper()}:")
            print(f"Marks: {marks}/100")
            print(f"Grade: {grade}")
            print(f"Message: {message}")
            break
        else:
            print("Invalid Marks Try again.")
    except ValueError:
        print("Invalid input.. Please enter a valid number for marks between 0 and 100.")