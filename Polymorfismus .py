# Základní třída Animal
class Animal:
    def make_sound(self):
        # Každé zvíře má svůj vlastní zvuk, takže zde vyvoláme výjimku,
        # aby podtřídy musely tuto metodu implementovat
        raise NotImplementedError("Subclasses must implement this method")

    def describe(self):
        # Obecný popis pro všechna zvířata
        return "This is an animal.\nIt has an unspecified number of legs."


# Odvozená třída Dog
class Dog(Animal):
    def make_sound(self):
        # Zvuk, který vydává pes
        return "Woof!"

    def describe(self):
        # Popis psa
        return "This is a dog.\nIt has 4 legs.\nDogs are loyal and friendly."


# Odvozená třída Cat
class Cat(Animal):
    def make_sound(self):
        # Zvuk, který vydává kočka
        return "Meow!"

    def describe(self):
        # Popis kočky
        return "This is a cat.\nIt has 4 legs.\nCats are independent and playful."


# Další odvozená třída Bird
class Bird(Animal):
    def make_sound(self):
        # Zvuk, který vydává pták
        return "Chirp!"

    def describe(self):
        # Popis ptáka
        return "This is a bird.\nIt has 2 legs.\nBirds can often fly."


# Funkce, která demonstruje polymorfismus
def animal_info(animal):
    # Vypíše popis zvířete
    print(animal.describe())
    # Vypíše zvuk, který zvíře vydává
    print(animal.make_sound())


# Seznam instancí různých tříd
animals = [Dog(), Cat(), Bird()]

# Otestování polymorfismu
for animal in animals:
    animal_info(animal)
    # Oddělující řádek pro přehlednost výstupu
    print("-")
