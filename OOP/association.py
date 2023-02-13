""" Ассоциация """
# Ассоциация - принцип ООП, который определяет взаимодействие между классами. Включает в себя 2 принципа: Композиция, Агрегация

class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        print('Двигатель завелся')


class Car:
    def __init__(self, brand, engine_power):
        self.brand = brand
        self.engine = Engine(engine_power)

    def start(self):
        self.engine.start()
        print('Машина завелась')

car = Car('BMW', 3200)
car.start()

engine = Engine(2000)

# Агрегация - случай, когда классы могут существовать друг без друга и имеют слабую связь между собой


class Human:
    class __Heart:
        def beat(self):
            print('Сердце бьется')
    
    class __Brain:
        def think(self):
            print('Мозг думает')
    
    def __init__(self, name):
        self.name = name
        self.heart = self.__Heart()
        self.brain = self.__Brain()


human = Human('Malika')
human.brain.think()

# brain = Human.Brain() # Error

# Композиция - случай, когда классы не могут существовать друг без друга и имеют сильную связь. Объекты одних классов нельзя создавать, пока не будут созданы связанные с ними


class A:
    def __init__(self, name):
        self.name = name

obj = A('Aliya')