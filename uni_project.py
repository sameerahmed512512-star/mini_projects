# Student Performance Management System
class Person:

    def __init__(self, name, department, semester, roll_no):

        self.name = name
        self.department = department
        self.semester = semester
        self.roll_no = roll_no


# Inheritance
class Student(Person):

    def __init__(self, name, department, semester, roll_no):

        super().__init__(name, department, semester, roll_no)

        self.subjects = {}

        # Encapsulation
        self.__total_marks = 0
        self.__gpa = 0
        self.total_credit_hours = 0
        self.total_grade_points = 0

    def add_marks(self):

        subjects = [
            "OOP",
            "Quantitative Reasoning",
            "Introduction To Data Analytics",
            "Islamic Studies",
            "DMCS",
            "Expository Writing"
        ]

        for subject in subjects:

            print("\n")
            print(subject)

            mid = int(input("Enter Mid Marks Out Of 20 : "))

            final = int(input("Enter Final Marks Out Of 50 : "))

            quiz_assignment = int(
                input("Enter Quiz + Assignment Marks Out Of 20 : ")
            )

            presentation = int(
                input("Enter Presentation Marks Out Of 10 : ")
            )

            credit_hours = int(
                input("Enter Credit Hours : ")
            )

            total = (
                mid
                + final
                + quiz_assignment
                + presentation
            )

            self.subjects[subject] = total

            self.__total_marks = (
                self.__total_marks + total
            )

            self.total_credit_hours = (
                self.total_credit_hours + credit_hours
            )

            # GPA Calculation

            if total >= 85:
                grade_point = 4.0

            elif total >= 80:
                grade_point = 3.7

            elif total >= 75:
                grade_point = 3.3

            elif total >= 70:
                grade_point = 3.0

            elif total >= 65:
                grade_point = 2.7

            elif total >= 60:
                grade_point = 2.3

            elif total >= 55:
                grade_point = 2.0

            elif total >= 50:
                grade_point = 1.7

            else:
                grade_point = 0.0

            self.total_grade_points = (
                self.total_grade_points
                + (grade_point * credit_hours)
            )

        self.__gpa = (
            self.total_grade_points
            / self.total_credit_hours
        )

    def display_result(self):

        print("\n")
        print("====Student Result====")

        print("Name :", self.name)

        print("Department :", self.department)

        print("Semester :", self.semester)

        print("Roll Number :", self.roll_no)

        print("\n====Subjects Marks====:")

        for sub in self.subjects:

            print(sub, ":", self.subjects[sub], "/100")

        print("\nTotal Marks :", self.__total_marks)

        print("GPA :", round(self.__gpa, 2), "/4.0")

    def get_total_marks(self):

        return self.__total_marks


# =====================================
# Main Program
# =====================================

students = []

num = int(
    input("How Many Students Data You Want To Enter : ")
)

for i in range(num):

    print("\n")
    print("Enter Student", i + 1)

    name = input("Enter Name : ")

    department = input("Enter Department : ")

    semester = input("Enter Semester : ")

    roll_no = input("Enter Roll Number : ")

    obj = Student(
        name,
        department,
        semester,
        roll_no
    )

    obj.add_marks()

    students.append(obj)


# =====================================
# Display Result
# =====================================

print("\n")
print("All Students Result")

for student in students:

    student.display_result()


# =====================================
# Ranking System
# =====================================

for i in range(len(students)):

    for j in range(i + 1, len(students)):

        if (
            students[j].get_total_marks()
            >
            students[i].get_total_marks()
        ):

            temp = students[i]

            students[i] = students[j]

            students[j] = temp


print("\n")
print("==Ranking System==")

position = 1

for student in students:

    print(position, "Position :", student.name)

    position = position + 1