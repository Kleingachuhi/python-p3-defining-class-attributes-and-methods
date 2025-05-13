class Student:
    total_students = 0
    all_students = []
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students +=1
        Student.all_students.append(self)
    @classmethod
    def get_total_students(cls):
        return cls.all_students
    @classmethod
    def list_students(cls):
        print([student.name for student in cls.all_students])
s1 = Student("Alice", 10)
s1 = Student("Klein", 86)
s1.list_students()
