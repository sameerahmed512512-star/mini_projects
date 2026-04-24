class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        else:
            return "Fail"


subjects = ["OOP", "DA", "QR", "EW", "DM&C", "IS"]

n = int(input("How many students? "))

students = []

for i in range(n):
    print(f"\nEnter data for Student {i+1}")

    name = input("Enter name: ")
    rollno = input("Enter roll no: ")

    marks = {}

    for sub in subjects:
        m = int(input(f"Enter marks for {sub}: "))
        marks[sub] = m

    s = Student(name, rollno, marks)
    students.append(s)

print("===== RESULT CARDS =====")

for s in students:

    print("Name =", s.name)
    print("Roll No =", s.rollno)

    print("Marks:")
    for sub, m in s.marks.items():
        print(sub, "=", m)

    print("Average =", s.average())
    print("Grade =", s.grade())