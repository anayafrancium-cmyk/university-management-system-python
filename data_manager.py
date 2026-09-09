import json  # python builtin module, this gives
# json.dump() and json.load()
# Because we want to convert Python data into JSON and JSON back into Python data.
# JSON understands dictionaries, lists, strings, numbers, booleans, and null

from code import Student, Teacher, Course, University


FILE_NAME = "university_data.json"


# ============================================================
# SAVE DATA
# ============================================================

def save_data(university, filename=FILE_NAME):

    data = {  # data is a dict on its own
        "university": {
            "name": university.name  # name attribute from code , class University
        },

        "students": [],

        "teachers": [],

        "courses": []
    }

    # --------------------------------------------------------
    # SAVE STUDENTS
    # --------------------------------------------------------

    for student in university.students: # .students refers to the student list above

        student_data = {
            "name": student.name,  #attributes of object from class Student
            "age": student.age,
            "gender": student.gender,
            "email": student.email,
            "phone": student.phone,

            "roll_no": student.roll_no,
            "semester": student.semester,
            "cgpa": student.cgpa
        }

        data["students"].append(student_data)

    # --------------------------------------------------------
    # SAVE TEACHERS
    # --------------------------------------------------------

    for teacher in university.teachers:

        teacher_data = {
            "name": teacher.name,
            "age": teacher.age,
            "gender": teacher.gender,
            "email": teacher.email,
            "phone": teacher.phone,

            "employee_id": teacher.employee_id,
            "department": teacher.department,
            "experience": teacher.experience,

            # Access private salary through getter
            "salary": teacher.get_salary()
        }

        data["teachers"].append(teacher_data)

    # --------------------------------------------------------
    # SAVE COURSES
    # --------------------------------------------------------

    for course in university.courses:

        # Store teacher ID instead of entire Teacher object
        teacher_id = None  # None becomes null in JSON

        if course.teacher is not None:   
            teacher_id = course.teacher.employee_id

        # Store student IDs instead of entire Student objects
        student_roll_numbers = []

        for student in course.students:
            student_roll_numbers.append(student.roll_no)
        # we are converting course object into dictionary
        course_data = {
            "course_code": course.course_code,
            "course_name": course.course_name,
            "credit_hours": course.credit_hours,
            "capacity": course.capacity,

            "teacher": teacher_id,
            "students": student_roll_numbers
        }

        data["courses"].append(course_data)

    # --------------------------------------------------------
    # WRITE TO JSON FILE
    # --------------------------------------------------------

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print("University data saved successfully.")


# ============================================================
# LOAD DATA
# ============================================================

def load_data(filename=FILE_NAME):

    try:

        with open(filename, "r") as file:
            data = json.load(file)

    except FileNotFoundError:

        print("No saved data found.")
        print("Starting with a new university.")

        return University("Punjab University")

    except json.JSONDecodeError:

        print("JSON file is corrupted or invalid.")
        print("Starting with a new university.")

        return University("Punjab University")

    # --------------------------------------------------------
    # CREATE UNIVERSITY
    # --------------------------------------------------------
    # converting json back to an actual oop object
    university_name = data["university"]["name"]

    university = University(university_name)

    # --------------------------------------------------------
    # CREATE STUDENTS
    # --------------------------------------------------------

    students_by_roll_no = {}

    for student_data in data["students"]:

        student = Student(   # creating student object
            student_data["name"],
            student_data["age"],
            student_data["gender"],
            student_data["email"],
            student_data["phone"],
            student_data["roll_no"],
            student_data["semester"],
            student_data["cgpa"]
        )

        university.add_student(student)

        # Store object for quick lookup later
        students_by_roll_no[student.roll_no] = student    # adding key value pair in above dict
        # ID → Object

    # --------------------------------------------------------
    # CREATE TEACHERS
    # --------------------------------------------------------

    teachers_by_id = {}

    for teacher_data in data["teachers"]:

        teacher = Teacher(
            teacher_data["name"],
            teacher_data["age"],
            teacher_data["gender"],
            teacher_data["email"],
            teacher_data["phone"],
            teacher_data["employee_id"],
            teacher_data["department"],
            teacher_data["experience"],
            teacher_data["salary"]
        )

        university.add_teacher(teacher)

        # Store object for quick lookup later
        teachers_by_id[teacher.employee_id] = teacher  # employee ID → actual Teacher object

    # --------------------------------------------------------
    # CREATE COURSES
    # --------------------------------------------------------

    courses_by_code = {}

    for course_data in data["courses"]:

        course = Course(
            course_data["course_code"],
            course_data["course_name"],
            course_data["credit_hours"],
            course_data["capacity"]
        )

        university.add_course(course)

        # Store object for relationship rebuilding
        courses_by_code[course.course_code] = course

    # ========================================================
    # REBUILD RELATIONSHIPS
    # ========================================================

    for course_data in data["courses"]:

        course = courses_by_code[course_data["course_code"]]

        # ----------------------------------------------------
        # REBUILD TEACHER RELATIONSHIP
        # ----------------------------------------------------

        teacher_id = course_data["teacher"]

        if teacher_id is not None:

            teacher = teachers_by_id.get(teacher_id)

            if teacher is not None:
                course.assign_teacher(teacher)

        # ----------------------------------------------------
        # REBUILD STUDENT RELATIONSHIPS
        # ----------------------------------------------------

        for roll_no in course_data["students"]:

            student = students_by_roll_no.get(roll_no)

            if student is not None:
                course.add_student(student)

    print("University data loaded successfully.")
# The function gives the reconstructed University object back to your main program.
    return university

    #              YOUR OOP PROGRAM
    #                    │
    #                    │
    #            Python Objects
    #                    │
    #     ┌──────────────┼──────────────┐
    #     ↓              ↓              ↓
    #  Student         Teacher        Course
    #     │              │              │
    #     └──────────────┼──────────────┘
    #                    │
    #              save_data()
    #                    │
    #                    ↓
    #          Convert Objects
    #                 into
    #       Dictionaries + Lists
    #                    │
    #                    ↓
    #               json.dump()
    #                    │
    #                    ↓
    #           university_data.json


    # When program starts again
    #               university_data.json
    #                    │
    #                    ↓
    #               json.load()
    #                    │
    #                    ↓
    #           Dictionaries + Lists
    #                    │
    #                    ↓
    #          Recreate Python Objects
    #                    │
    #     ┌──────────────┼──────────────┐
    #     ↓              ↓              ↓
    #  Student         Teacher        Course
    #     │              │              │
    #     └──────────────┼──────────────┘
    #                    │
    #                    ↓
    #           Rebuild relationships
    #                    │
    #                    ↓
    #                University object


# JSON can't directly preserve those Python object references, so you save their identifiers, then use those identifiers to reconnect everything when loading.
# That's the core idea.