# Třídy a objekty
class Person:
    """Třída reprezentující základní osobu se jménem, příjmením a věkem."""
    def __init__(self, first_name, last_name, age):
        self.full_name = f"{first_name} {last_name}"  # Sloučené jméno a příjmení
        self.age = age  # Věk

    def introduce(self):
        """Metoda pro vypsání základních informací o osobě."""
        print("=" * 40)
        print(f"   Jméno a příjmení : {self.full_name}")
        print(f"    Věk             : {self.age} let")


class Student(Person):
    """Třída Student, která dědí z Person a přidává další informace související se studiem."""
    def __init__(self, first_name, last_name, age, school, study_field):
        super().__init__(first_name, last_name, age)  # Volání konstruktoru rodičovské třídy
        self.school = school  # Název školy
        self.study_field = study_field  # Studijní obor

        # Studijní předměty a jejich známky
        self.math = None
        self.czech = None
        self.english = None
        self.programming = None

    def input_grade(self, subject):
        """Metoda pro zadání známky s kontrolou maximální hodnoty 5."""
        while True:
            try:
                grade = float(input(f"Zadej známku z {subject} : "))
                if 1 <= grade <= 5:  # Kontrola rozsahu známek
                    return grade
                else:
                    print(" Chyba: Zadej známku v rozmezí 1-5!")
            except ValueError:
                print(" Chyba: Zadej platné číslo!")

    def set_grades(self):
        """Metoda pro nastavení známek z jednotlivých předmětů."""
        print("\n Zadejte známky z jednotlivých předmětů:")
        self.math = self.input_grade("matematiky")
        self.czech = self.input_grade("češtiny")
        self.english = self.input_grade("angličtiny")
        self.programming = self.input_grade("programování")

    def calculate_average(self):
        """Metoda pro výpočet průměrné známky."""
        return (self.math + self.czech + self.english + self.programming) / 4  # Výpočet průměru

    def display_info(self):
        """Metoda pro vypsání všech informací o studentovi, včetně známek a průměru."""
        self.introduce()  # Zavolání metody pro základní informace
        print(f"    Škola           : {self.school}")
        print(f"    Obor            : {self.study_field}")
        print("-" * 40)
        print(f"    Známky:")
        print(f"    Matematika    : {self.math}")
        print(f"    Čeština       : {self.czech}")
        print(f"    Angličtina    : {self.english}")
        print(f"    Programování  : {self.programming}")
        print("-" * 40)
        print(f" Průměrná známka : {self.calculate_average():.2f}")
        print("=" * 40)


# Funkce pro zadání věku, která zaručuje, že bude zadáno pouze číslo
def input_age():
    while True:
        try:
            age = int(input("Zadej věk: "))
            if age > 0:
                return age
            else:
                print("Věk musí být kladné číslo!")
        except ValueError:
            print("Chyba: Zadej platné číslo pro věk!")

# Funkce pro zadání textového vstupu bez čísel
def input_text(prompt):
    while True:
        text = input(prompt).strip()
        if any(char.isdigit() for char in text):  # Kontrola, jestli text obsahuje čísla
            print("Chyba: Zadejte prosím text bez čísel!")
        else:
            return text


# Zadání údajů od uživatele
print("\n **Vytvoření nového studenta** \n")
first_name = input_text("Zadej jméno: ")  # Zadání jména studenta
last_name = input_text("Zadej příjmení: ")  # Zadání příjmení studenta
age = input_age()  # Zadání věku studenta s kontrolou
school = input_text("Zadej název školy: ")  # Zadání názvu školy
study_field = input_text("Zadej studijní obor: ")  # Zadání studijního oboru

# Vytvoření objektu studenta
student1 = Student(first_name, last_name, age, school, study_field)

# Nastavení známek s kontrolou
student1.set_grades()

# Výpis informací o studentovi
student1.display_info()
