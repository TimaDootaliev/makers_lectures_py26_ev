class AbstracCreature:
    def eat(self):
        pass

    def breathe(self):
        pass

    def move(self):
        pass


class Human(AbstracCreature):
    def eat(self):
        print('Я млекопитающее')

    def breathe(self):
        print('Дышу воздухом')

    def move(self):
        print('Передвигаюсь по земле')


from abc import ABC, abstractmethod

class Tehnika(ABC):

    @abstractmethod
    def sound(self):
        pass

class Phone(Tehnika):
    def sound(self):
        print('Звонок из нокии')

a = Phone()
a.sound()