# src/animals.py

class Animal:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

class DomesticAnimal(Animal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)

class PackAnimal(Animal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)

class Dog(DomesticAnimal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)

class Cat(DomesticAnimal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)

class Hamster(DomesticAnimal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)

class Horse(PackAnimal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)

class Camel(PackAnimal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)

class Donkey(PackAnimal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)