# Родительский
class Animal:
    def __init__(self, name):
        self.alive = True  # Живое существо
        self.fed = False  # Накормленное или нет
        self.name = name  # Имя животного


# Родительский
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


# наследник Animal
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# наследник Animal
class Predator(Animal):
    def init(self, name):
        super().init()

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# наследник Plant
class Flower(Plant):
    pass  # цветы по умолчанию несъедобны


# наследник Plant
class Fruit(Plant):
    def init(self, name):
        super().init(name)
        self.edible = True  # Плоды съедобны

    #  животные


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
#  растения
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)  # True, волк жив
print(a2.fed)  # False, Хатико голоден
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
