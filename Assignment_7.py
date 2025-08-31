#Course Dictionairies
room_number = {
    "CSC101": "3004:",
    "CSC102": "4501:",
    "CSC103": "6755:",
    "NET110:": "1244:",
    "COM241:": "1411:"
}

instructor_name = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110:": "Burke",
    "COM241:": "Lee"
}   

meeting_time = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110:": "11:00 a.m.",
    "COM241:": "1:00 p.m."
}

#Info Input
course = input("Enter a course number: ").upper()

#Info Output
if course in room_number:
    print(f"Course: {course}")
    print(f"Room Number: {room_number[course]}")
    print(f"Instructor: {instructor_name[course]}")
    print(f"Meeting Time: {meeting_time[course]}")
else:
    print("Course not found. Please enter valid course information.")
