# Abstrakce
from abc import ABC, abstractmethod

class AbstractPerson(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def introduce(self):
        pass


class AbstractStudent(AbstractPerson):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")
        print("I am a student with ID", self.student_id)


class AbstractTeacher(AbstractPerson):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")
        print("I teach", self.subject)


# Vytvoření objektů pro abstraktní třídy
student2 = AbstractStudent("Bob", 22, "S67890")
teacher2 = AbstractTeacher("Dr. Johnson", 50, "Physics")

# Výpis informací
student2.introduce()
teacher2.introduce()
