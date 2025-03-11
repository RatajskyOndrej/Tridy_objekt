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

        # Studijní předměty a jejich známky, inicializace na None
        self.math = None
        self.czech = None
        self.english = None
        self.programming = None

    def input_grade(self, subject):
        """Metoda pro zadání známky s kontrolou maximální hodnoty 5."""
        while True:
            try:
                # Zadání známky a kontrola, zda je v rozsahu 1 až 5
                grade = float(input(f"Zadej známku z {subject} : "))
                if 1 <= grade <= 5:  # Kontrola rozsahu známek
                    return grade
                else:
                    print(" Chyba: Zadej známku v rozmezí 1-5!")
            except ValueError:
                print(" Chyba: Zadej platné číslo!")  # Ošetření neplatného vstupu (není číslo)

    def set_grades(self):
        """Metoda pro nastavení známek z jednotlivých předmětů."""
        print("\n Zadejte známky z jednotlivých předmětů:")
        # Volání metody input_grade pro každý předmět
        self.math = self.input_grade("matematiky")
        self.czech = self.input_grade("češtiny")
        self.english = self.input_grade("angličtiny")
        self.programming = self.input_grade("programování")

    def calculate_average(self):
        """Metoda pro výpočet průměrné známky."""
        # Výpočet průměru ze všech známek
        return (self.math + self.czech + self.english + self.programming) / 4

    def display_info(self):
        """Metoda pro vypsání všech informací o studentovi, včetně známek a průměru."""
        self.introduce()  # Zavolání metody pro základní informace o studentovi
        # Výpis informací o škole a studijním oboru
        print(f"    Škola           : {self.school}")
        print(f"    Obor            : {self.study_field}")
        print("-" * 40)
        # Výpis jednotlivých známek
        print(f"    Známky:")
        print(f"    Matematika    : {self.math}")
        print(f"    Čeština       : {self.czech}")
        print(f"    Angličtina    : {self.english}")
        print(f"    Programování  : {self.programming}")
        print("-" * 40)
        # Výpočet a výpis průměrné známky
        print(f" Průměrná známka : {self.calculate_average():.2f}")
        print("=" * 40)


# Funkce pro zadání věku, která zaručuje, že bude zadáno pouze číslo
def input_age():
    while True:
        try:
            # Zadání věku a kontrola, zda je kladné číslo
            age = int(input("Zadej věk: "))
            if age > 0:
                return age
            else:
                print("Věk musí být kladné číslo!")  # Kontrola, že věk je kladný
        except ValueError:
            print("Chyba: Zadej platné číslo pro věk!")  # Ošetření neplatného vstupu (není číslo)

# Funkce pro zadání textového vstupu bez čísel
def input_text(prompt):
    while True:
        text = input(prompt).strip()  # Zadání textu, odstranění bílých znaků na začátku a na konci
        # Kontrola, jestli text obsahuje číslice
        if any(char.isdigit() for char in text):
            print("Chyba: Zadejte prosím text bez čísel!")  # Pokud text obsahuje čísla, zobrazení chybové zprávy
        else:
            return text  # Pokud je vstup platný, vrátí text

# Zadání údajů od uživatele
print("\n **Vytvoření nového studenta** \n")
# Získání údajů o studentovi, kontrola pro jméno, příjmení, školu a obor
first_name = input_text("Zadej jméno: ")  # Zadání jména studenta
last_name = input_text("Zadej příjmení: ")  # Zadání příjmení studenta
age = input_age()  # Zadání věku studenta s kontrolou
school = input_text("Zadej název školy: ")  # Zadání názvu školy
study_field = input_text("Zadej studijní obor: ")  # Zadání studijního oboru

# Vytvoření objektu studenta s uvedenými údaji
student1 = Student(first_name, last_name, age, school, study_field)

# Nastavení známek s kontrolou
student1.set_grades()

# Výpis informací o studentovi
student1.display_info()

#promena ve ktera je uloyena instance se kterou pracuju
#innit se rezervuje pamet pro vsechny objekt