# src/menu.py

from animals import *
from counter import Counter

class Menu:
    def __init__(self):
        self.animals = []
        self.counter = Counter()

    def add_animal(self, animal):
        with self.counter:
            self.animals.append(animal)
            self.counter.add()
            print(f"Добавлено новое животное: {animal.name}")

    def show_commands(self, animal):
        # В данном простом примере мы просто выводим команды
        print(f"{animal.name} выполняет команды: {animal.__class__.__name__}")

    def display_menu(self):
        while True:
            print("\n1. Завести новое животное")
            print("2. Выход")
            choice = input("Выберите опцию: ")

            if choice == "1":
                name = input("Введите имя животного: ")
                birthday = input("Введите дату рождения (YYYY-MM-DD): ")
                animal_type = input("Введите тип животного (собака, кошка, хомяк, лошадь, верблюд, осел): ")

                if animal_type.lower() == "собака":
                    animal = Dog(name, birthday)
                elif animal_type.lower() == "кошка":
                    animal = Cat(name, birthday)
                elif animal_type.lower() == "хомяк":
                    animal = Hamster(name, birthday)
                elif animal_type.lower() == "лошадь":
                    animal = Horse(name, birthday)
                elif animal_type.lower() == "верблюд":
                    animal = Camel(name, birthday)
                elif animal_type.lower() == "осел":
                    animal = Donkey(name, birthday)
                else:
                    print("Неизвестный тип животного!")
                    continue

                self.add_animal(animal)
                self.show_commands(animal)
            elif choice == "2":
                break
            else:
                print("Неверный выбор, попробуйте снова.")