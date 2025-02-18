# Třídy a objekty
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        super().introduce()
        print(f"I am a student with ID {self.student_id}.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I teach {self.subject}.")


# Vytvoření objektů studentů a učitelů
student1 = Student("Alice", 20, "S12345")
teacher1 = Teacher("Pan Smith", 45, "Mathematics")

# Výpis informací o studentech a učitelích
student1.introduce()
teacher1.introduce()
#aplikuj modifikaci
#udelej minimalen 5 veci (jmeno prijmeni trida obor skola )
#metoda vypsat
#novy objekt student