while True:
    grade = int(input("Enter a grade (0-100): "))
    if 0 <= grade <= 100:
        print(f"Valid grade accepted: {grade}")
        break
    else:
        print("Invalid! Must be between 0 and 100.")
