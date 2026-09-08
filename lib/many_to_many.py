class Student:
    all =[]
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Student.all.append(self)

    # instance method in student called courses
    def courses(self):
        return [schedule.course for schedule in Schedule.all if schedule.student == self]

    # CALCULATE GPA
    def calculate_gpa(self):
        grades = [schedule.grade for schedule in Schedule.all if schedule.student == self]
        return sum(grades) / len(grades)


class Course:
    all =[]
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        Course.all.append(self)

    #instance method in courses called student
    def students(self):
        return [schedule.student for schedule in Schedule.all if schedule.course == self]

class Schedule:
    all = []
    def __init__ (self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade
        Schedule.all.append(self)

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, value):
        if not isinstance(value, Student):
            raise Exception
        self._student = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        if not isinstance(value, Course):
            raise Exception
        self._course = value

#FAKE DATA:
# students ...
bob = Student("Bob", "bob@uni.edu")
angela = Student("Angela", "angela@uni.edu")
mandi = Student("Mandi", "mandi@uni.edu")

# courses ...
py = Course("Intro to Python", "Mr. Smith")
oop = Course("OOP Python", "Ms. Berge")

# schedules ...
Schedule(bob, py, 3.6)
Schedule(mandi, py, 3.9)
Schedule(angela, oop, 3.3)
Schedule(bob, oop, 3.1)

# print("Bob's Courses")
# print(bob.courses())

# print("Mandi's Courses")
# print(mandi.courses())

# print("Python Students")
# for student in py.students():
#     print(student.name)

# print(bob.calculate_gpa())