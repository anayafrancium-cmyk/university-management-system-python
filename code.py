class Person:
    total_people = 0

    def __init__(self, name, age, gender, email, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone = phone

        Person.total_people += 1

    @classmethod
    def get_total_people(cls):
        return cls.total_people

    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email

    @staticmethod
    def validate_phone(phone):
        return len(phone) == 11 and phone.isdigit()

    def update_email(self, new_email):
        if self.validate_email(new_email):
            self.email = new_email
            print(
                f"{self.name}'s email has been updated "
                f"successfully to {self.email}"
            )
        else:
            print("Invalid email. It can't be updated.")

    def update_phone(self, new_phone):
        if self.validate_phone(new_phone):
            self.phone = new_phone
            print(
                f"{self.name}'s phone number has been updated "
                f"successfully to {self.phone}"
            )
        else:
            print("Invalid phone number. It can't be updated.")

    def display_info(self):
        print("======= PERSONAL INFORMATION =======")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Email  : {self.email}")
        print(f"Phone  : {self.phone}")


# ============================================================
# STUDENT CLASS
# ============================================================

class Student(Person):

    def __init__(
        self,
        name,
        age,
        gender,
        email,
        phone,
        roll_no,
        semester,
        cgpa
    ):
        super().__init__(name, age, gender, email, phone)

        self.roll_no = roll_no
        self.semester = semester
        self.cgpa = cgpa

        # Courses this student is enrolled in
        self.courses = []

    def enroll_course(self, course):
        if course in self.courses:
            print(f"{course.course_name} is already enrolled by {self.name}.")
            return

        course.add_student(self)  
        print(f"{course.course_name} has been added to the courses of {self.name}.")
       # Course.add_student(course, self)  self is student, works the same 
        # object.method(argument) Python automatically does : Class.method(object, argument)
        # Course is the class. course is a variable holding an object created from that class.

    def drop_course(self, course):
        if course not in self.courses:
            print(f"{course.course_name} is not enrolled by {self.name}.")
            return

        course.remove_student(self)
        print(f"{course.course_name} has been removed from the courses of {self.name}.")

    def view_courses(self):
        print(f"\nCourses of {self.name}:")

        if not self.courses:
            print("No courses enrolled.")
            return

        for course in self.courses:
            print(
                f"{course.course_code} - "
                f"{course.course_name}"
            )

    def display_info(self):
        print("\n========== STUDENT INFORMATION ==========")

        super().display_info()

        print("======= ACADEMIC INFORMATION =======")
        print(f"Roll No  : {self.roll_no}")
        print(f"Semester : {self.semester}")
        print(f"CGPA     : {self.cgpa}")

        print("Courses:")
        if self.courses:
            for course in self.courses:
                print(
                    f"  - {course.course_code}: "
                    f"{course.course_name}"
                )
        else:
            print("  No courses enrolled.")

        print("=========================================")


# ============================================================
# TEACHER CLASS
# ============================================================

class Teacher(Person):

    def __init__(
        self,
        name,
        age,
        gender,
        email,
        phone,
        employee_id,
        department,
        experience,
        salary
    ):
        super().__init__(name, age, gender, email, phone)

        self.employee_id = employee_id
        self.department = department
        self.experience = experience

        # Encapsulation
        self.__salary = salary

        # Courses taught by this teacher
        self.courses_teaching = []

    def get_salary(self):   #getter
        return self.__salary

    def update_salary(self, amount):  #setter
        if amount > 0:
            self.__salary = amount
            print(f"Salary updated to: {self.__salary}")
        else:
            print("Invalid salary amount!")

    def assign_course(self, course):

        if course in self.courses_teaching:
            print(f"{course.course_name} is already assigned to {self.name}.")
            return

        course.assign_teacher(self)
        print(f"{course.course_name} has been assigned to {self.name}.")


    def remove_course(self, course):

        if course not in self.courses_teaching:
            print(f"{course.course_name} is not assigned to {self.name}.")
            return

        course.remove_teacher()
        print(f"{course.course_name} has been removed from {self.name}.")

    def view_courses(self):
        print(f"\nCourses taught by {self.name}:")

        if not self.courses_teaching:
            print("No courses assigned.")
            return

        for course in self.courses_teaching:
            print(
                f"{course.course_code} - "
                f"{course.course_name}"
            )

    def display_info(self):
        print("\n========== TEACHER INFORMATION ==========")

        super().display_info()

        print("======= TEACHING INFORMATION =======")
        print(f"Employee ID : {self.employee_id}")
        print(f"Department  : {self.department}")
        print(f"Experience  : {self.experience} years")
        print(f"Salary      : {self.__salary}")

        print("Courses Teaching:")
        if self.courses_teaching:
            for course in self.courses_teaching:
                print(
                    f"  - {course.course_code}: "
                    f"{course.course_name}"
                )
        else:
            print("  No courses assigned.")

        print("=========================================")


# ============================================================
# COURSE CLASS
# ============================================================

class Course:

    def __init__(
        self,
        course_code,
        course_name,
        credit_hours,
        capacity
    ):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.capacity = capacity

        # One teacher
        self.teacher = None

        # Multiple students
        self.students = []

    # --------------------------------------------------------
    # TEACHER RELATIONSHIP
    # --------------------------------------------------------

    def assign_teacher(self, teacher):

        # If the same teacher is already assigned
        if self.teacher == teacher:
            print(
                f"{teacher.name} is already teaching "
                f"{self.course_name}."
            )
            return

        # If another teacher is already assigned
        if self.teacher is not None:
            print(
                f"{self.course_name} already has "
                f"{self.teacher.name} assigned."
            )
            return

        self.teacher = teacher

        # Synchronize Teacher -> Course
        if self not in teacher.courses_teaching:
            teacher.courses_teaching.append(self)

        print(
            f"{teacher.name} has been assigned "
            f"to {self.course_name}."
        )

    def remove_teacher(self):

        if self.teacher is None:
            print("No teacher is currently assigned.")
            return

        teacher = self.teacher

        # Remove Course from Teacher's list
        if self in teacher.courses_teaching:
            teacher.courses_teaching.remove(self)

        # Remove Teacher from Course
        self.teacher = None

        print(
            f"{teacher.name} has been removed "
            f"from {self.course_name}."
        )

    # --------------------------------------------------------
    # STUDENT RELATIONSHIP
    # --------------------------------------------------------

    def add_student(self, student):

        # Prevent duplicate enrollment
        if student in self.students:
            print(
                f"{student.name} is already enrolled "
                f"in {self.course_name}."
            )
            return

        # Check capacity
        if len(self.students) >= self.capacity:
            print(
                f"{self.course_name} is full."
            )
            return

        # Add student to Course
        self.students.append(student)

        # Synchronize Student -> Course
        if self not in student.courses:
            student.courses.append(self)

        print(
            f"{student.name} has been enrolled "
            f"in {self.course_name}."
        )

    def remove_student(self, student):

        if student not in self.students:
            print(
                f"{student.name} is not enrolled "
                f"in {self.course_name}."
            )
            return

        # Remove Student from Course
        self.students.remove(student)

        # Synchronize Course -> Student
        if self in student.courses:
            student.courses.remove(self)

        print(
            f"{student.name} has been removed "
            f"from {self.course_name}."
        )

    # --------------------------------------------------------
    # DISPLAY STUDENTS
    # --------------------------------------------------------

    def view_students(self):

        print(
            f"\nStudents enrolled in "
            f"{self.course_name}:"
        )

        if not self.students:
            print("No students enrolled.")
            return

        for student in self.students:
            print(
                f"Roll No: {student.roll_no} | "
                f"Name: {student.name}"
            )

    # --------------------------------------------------------
    # DISPLAY COURSE INFORMATION
    # --------------------------------------------------------

    def display_info(self):

        print("\n========== COURSE INFORMATION ==========")

        print(f"Course Code   : {self.course_code}")
        print(f"Course Name   : {self.course_name}")
        print(f"Credit Hours  : {self.credit_hours}")
        print(f"Capacity      : {self.capacity}")

        if self.teacher is not None:
            print(f"Teacher       : {self.teacher.name}")
        else:
            print("Teacher       : Not Assigned")

        print(
            f"Enrolled      : "
            f"{len(self.students)}/{self.capacity}"
        )

        print("=========================================")


# ============================================================
# UNIVERSITY CLASS
# ============================================================

class University:

    def __init__(self, name):
        self.name = name

        # University contains all students
        self.students = []

        # University contains all teachers
        self.teachers = []

        # University contains all courses
        self.courses = []

    # --------------------------------------------------------
    # STUDENT MANAGEMENT
    # --------------------------------------------------------

    def add_student(self, student):

        if student in self.students:
            print(
                f"{student.name} is already registered."
            )
            return

        self.students.append(student)

        print(
            f"{student.name} has been added "
            f"to {self.name}."
        )

    def remove_student(self, student):

        if student not in self.students:
            print(
                f"{student.name} is not registered."
            )
            return

        # Remove student from all courses first
        for course in self.courses[:]:
            if student in course.students:
                course.remove_student(student)

        self.students.remove(student)

        print(
            f"{student.name} has been removed "
            f"from {self.name}."
        )

    def view_students(self):

        print(
            f"\n========== STUDENTS OF "
            f"{self.name} =========="
        )

        if not self.students:
            print("No students registered.")
            return

        for student in self.students:
            print(
                f"Roll No: {student.roll_no} | "
                f"Name: {student.name} | "
                f"Semester: {student.semester}"
            )

    # --------------------------------------------------------
    # TEACHER MANAGEMENT
    # --------------------------------------------------------

    def add_teacher(self, teacher):

        if teacher in self.teachers:
            print(
                f"{teacher.name} is already registered."
            )
            return

        self.teachers.append(teacher)

        print(
            f"{teacher.name} has been added "
            f"to {self.name}."
        )

    def remove_teacher(self, teacher):

        if teacher not in self.teachers:
            print(
                f"{teacher.name} is not registered."
            )
            return

        # Remove teacher from all courses
        for course in self.courses[:]:
            if course.teacher == teacher:
                course.remove_teacher()

        self.teachers.remove(teacher)

        print(
            f"{teacher.name} has been removed "
            f"from {self.name}."
        )

    def view_teachers(self):

        print(
            f"\n========== TEACHERS OF "
            f"{self.name} =========="
        )

        if not self.teachers:
            print("No teachers registered.")
            return

        for teacher in self.teachers:
            print(
                f"Employee ID: {teacher.employee_id} | "
                f"Name: {teacher.name} | "
                f"Department: {teacher.department}"
            )

    # --------------------------------------------------------
    # COURSE MANAGEMENT
    # --------------------------------------------------------

    def add_course(self, course):

        if course in self.courses:
            print(
                f"{course.course_name} already exists."
            )
            return

        self.courses.append(course)

        print(
            f"{course.course_name} has been added "
            f"to {self.name}."
        )

    def remove_course(self, course):

        if course not in self.courses:
            print(
                f"{course.course_name} does not exist."
            )
            return

        # Remove teacher relationship
        if course.teacher is not None:
            course.remove_teacher()

        # Remove student relationships
        for student in course.students[:]:
            course.remove_student(student)

        self.courses.remove(course)

        print(
            f"{course.course_name} has been removed "
            f"from {self.name}."
        )

    def view_courses(self):

        print(
            f"\n========== COURSES OF "
            f"{self.name} =========="
        )

        if not self.courses:
            print("No courses available.")
            return

        for course in self.courses:

            if course.teacher:
                teacher_name = course.teacher.name
            else:
                teacher_name = "Not Assigned"

            print(
                f"Code: {course.course_code} | "
                f"Name: {course.course_name} | "
                f"Credits: {course.credit_hours} | "
                f"Teacher: {teacher_name} | "
                f"Students: {len(course.students)}/"
                f"{course.capacity}"
            )

    # --------------------------------------------------------
    # UNIVERSITY INFORMATION
    # --------------------------------------------------------

    def display_info(self):

        print("\n=========================================")
        print(
            f"       {self.name.upper()}"
        )
        print("=========================================")

        print(
            f"Total Students : {len(self.students)}"
        )

        print(
            f"Total Teachers : {len(self.teachers)}"
        )

        print(
            f"Total Courses  : {len(self.courses)}"
        )

        print("=========================================")
