class Member:
    def __init__(self,name,age,status,subject):
        self.name = name
        self.age = age
        self.status = status
        self.subject = subject

class Teacher(Member):
    def __init__(self,name,age,status,subject,salary):
        super().__init__(name,age,status,subject)
        self.__salary = salary
    def calculate_yearly_salary(self):
        return self.salary * 12

class Student(Member):
    def __init__(self, name,age, status,grade):
        super().__init__(name,age,status,grade)
        self.grade = grade

    def __str__(self):
        return f"name:{self.name}, age={self.age}, status={self.status}, grade={self.grade}"

achi = Student("achi", 16, "Student", 97)
# shotiko = Teacher("shotiko" , 21 ,"Teacher" "programming", 99999)
print (achi.__str__())