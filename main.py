from code import Student, Teacher, Course, University
from data_manager import load_data, save_data
def add_student_menu(university):

    print("\n========== ADD STUDENT ==========")

    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    email = input("Email: ")
    phone = input("Phone: ")
    roll_no = input("Roll No: ")
    semester = int(input("Semester: "))
    cgpa = float(input("CGPA: "))

    student = Student(
        name,
        age,
        gender,
        email,
        phone,
        roll_no,
        semester,
        cgpa
    )

    university.add_student(student)
def add_teacher_menu(university):

    print("\n========== ADD TEACHER ==========")

    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    email = input("Email: ")
    phone = input("Phone: ")
    employee_id = input("Employee ID: ")
    department = input("Department: ")
    experience = int(input("Experience (years): "))
    salary = float(input("Salary: "))

    teacher = Teacher(
        name,
        age,
        gender,
        email,
        phone,
        employee_id,
        department,
        experience,
        salary
    )

    university.add_teacher(teacher)

def add_course_menu(university):

    print("\n========== ADD COURSE ==========")

    course_code = input("Course Code: ")
    course_name = input("Course Name: ")
    credit_hours = int(input("Credit Hours: "))
    capacity = int(input("Capacity: "))

    course = Course(
        course_code,
        course_name,
        credit_hours,
        capacity
    )

    university.add_course(course)
def find_student(university, roll_no):

    for student in university.students:

        if student.roll_no == roll_no:
            return student

    return None
def find_teacher(university, employee_id):

    for teacher in university.teachers:

        if teacher.employee_id == employee_id:
            return teacher

    return None
def find_course(university, course_code):

    for course in university.courses:

        if course.course_code == course_code:
            return course
    return None
def assign_teacher_menu(university):

    print("\n========== ASSIGN TEACHER ==========")

    employee_id = input("Enter Teacher Employee ID: ")
    course_code = input("Enter Course Code: ")

    teacher = find_teacher(
        university,
        employee_id
    )

    course = find_course(
        university,
        course_code
    )

    if teacher is None:
        print("Teacher not found.")
        return

    if course is None:
        print("Course not found.")
        return

    course.assign_teacher(teacher)
    return None
def enroll_student_menu(university):

    print("\n========== ENROLL STUDENT ==========")

    roll_no = input("Enter Student Roll No: ")
    course_code = input("Enter Course Code: ")

    student = find_student(
        university,
        roll_no
    )

    course = find_course(
        university,
        course_code
    )

    if student is None:
        print("Student not found.")
        return

    if course is None:
        print("Course not found.")
        return

    student.enroll_course(course)

def drop_student_menu(university):

    print("\n========== DROP STUDENT ==========")

    roll_no = input("Enter Student Roll No: ")
    course_code = input("Enter Course Code: ")

    student = find_student(
        university,
        roll_no
    )

    course = find_course(
        university,
        course_code
    )

    if student is None:
        print("Student not found.")
        return

    if course is None:
        print("Course not found.")
        return

    student.drop_course(course)

def remove_teacher_menu(university):

    print("\n========== REMOVE TEACHER ==========")

    employee_id = input("Enter Teacher Employee ID: ")
    course_code = input("Enter Course Code: ")

    teacher = find_teacher(
        university,
        employee_id
    )

    course = find_course(
        university,
        course_code
    )

    if teacher is None:
        print("Teacher not found.")
        return

    if course is None:
        print("Course not found.")
        return

    if course.teacher != teacher:
        print(
            f"{teacher.name} is not teaching "
            f"{course.course_name}."
        )
        return

    course.remove_teacher()
def view_course_students_menu(university):

    print("\n========== VIEW COURSE STUDENTS ==========")

    course_code = input("Enter Course Code: ")

    course = find_course(
        university,
        course_code
    )

    if course is None:
        print("Course not found.")
        return

    course.view_students()

def view_student_courses_menu(university):

    print("\n========== VIEW STUDENT COURSES ==========")

    roll_no = input("Enter Student Roll No: ")

    student = find_student(
        university,
        roll_no
    )

    if student is None:
        print("Student not found.")
        return

    student.view_courses()
def view_teacher_courses_menu(university):

    print("\n========== VIEW TEACHER COURSES ==========")

    employee_id = input("Enter Teacher Employee ID: ")

    teacher = find_teacher(
        university,
        employee_id
    )

    if teacher is None:
        print("Teacher not found.")
        return

    teacher.view_courses()



def main():

    university = load_data()
    # menu goes here
    while True:

        print("\n========== UNIVERSITY MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. Assign Teacher to Course")
        print("5. Enroll Student in Course")
        print("6. Drop Student from Course")
        print("7. Remove Teacher from Course")
        print("8. View Students")
        print("9. View Teachers")
        print("10. View Courses")
        print("11. View Course Students")
        print("12. View Student Courses")
        print("13. View Teacher Courses")
        print("14. University Statistics")
        print("15. Save Data")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            save_data(university)
            print("Data saved. Goodbye!")
            print("Exiting University Management System...")
            break

        elif choice == "1":
            add_student_menu(university)

        elif choice == "2":
            add_teacher_menu(university)

        elif choice == "3":
            add_course_menu(university)

        elif choice == "4":
            assign_teacher_menu(university)

        elif choice == "5":
            enroll_student_menu(university)

        elif choice == "6":
            drop_student_menu(university)

        elif choice == "7":
            remove_teacher_menu(university)

        elif choice == "8":
            university.view_students()

        elif choice == "9":
            university.view_teachers()

        elif choice == "10":
            university.view_courses()

        elif choice == "11":
            view_course_students_menu(university)

        elif choice == "12":
            view_student_courses_menu(university)

        elif choice == "13":
            view_teacher_courses_menu(university)

        elif choice == "14":
            university.display_info()

        elif choice == "15":
            save_data(university)
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()