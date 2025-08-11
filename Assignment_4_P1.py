grades = {"Math": "A", "English": "B"}
courses = ["Math", "English", "Science," "History"]

enrolled_courses = ["Math", "English", "Science"]

while True:
    print("\n--- Student Course Management System ---")
    print("1. View Grades")
    print("2. Enroll in a Course")
    print("3. Drop a Course") 
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nYour Grades:")
        for course, grade in grades.items():
            grade = grades.get(course, "N/A") 
            print(f"{course}: {grade}")

    elif choice == "2":
        print("\nAvailable Courses to Enroll:")
        for course in courses:
            if course not in enrolled_courses:
                print(f" - {course}")
        new_course = input("Enter the course name to enroll: ")

        if new_course in courses and new_course not in enrolled_courses:
            enrolled_courses.append(new_course)
            print(f"Enrolled in {new_course}.")
        else:
            print("Invalid course name or already enrolled.")

    elif choice == "3":
        print("\nEnrolled Courses:")
        for course in enrolled_courses: 
            print(f"- {course}")
        drop_course = input("Enter the course name to drop: ")

        if drop_course in enrolled_courses: 
            enrolled_courses.remove(drop_course)
            print(f"Dropped {drop_course}.")
        else:
            print("Invalid course name or not enrolled in that course.")

    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break # Exit the infinite loop 
    
    else: 
        print("Invalid choice. Please eneter a number between 1 and 4.")