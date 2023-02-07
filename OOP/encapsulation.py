""" Инкапсуляция """
# Инкапсуляция - принцип ООП, подразумевающий защиту данных и объединение атрибутов и методов внутри класса

class Phone:
    def __init__(self, battery, color, brand) -> None:
        self.battery = battery
        self.color = color
        self.brand = brand
    

phone = Phone(100, 'red', 'Samsung')
phone.battery
phone.battery = -20

"""  
Модификаторы/уровни доступа:
1. public
Публичные методы и атрибуты доступны везде: внутри класса, вне класса, в дочерних классах

2. protected
Защищенные методы и атрибуты доступны внутри класса и в дочерних классах

3. private
Приватные методы и атрибуты доступны только внутри того класса, где они были определены
"""

# Инкапсуляция в python работает на уровне соглашения

class EncapsulatedClass:
    public = 'public'
    _protected = 'protected'
    __private = 'private'

    def __init__(self, pub, prot, priv) -> None:
        self.pub = pub
        self._prot = prot
        self.__priv = priv
    
    def pub_method(self) -> None:
        pass

    def _prot_method(self) -> None:
        pass

    def __priv_method(self) -> None:
        pass


obj = EncapsulatedClass(1, 2, 3)
# print(obj.public)
# print(obj._protected)
# print(dir(obj))
# print(obj.__private)
# print(obj._EncapsulatedClass__private)


# class InheritedClass(EncapsulatedClass):
#     def method1(self):
#         print(self.public)
#         print(self._protected)
#         print(self._EncapsulatedClass__private)

# obj2 = InheritedClass(1, 2, 3)
# obj2.method1()


""" setter & getter - интерфейсные методы """

class Light:
    __is_on = False
    __MIN_BRIGHTNESS = 10
    __MAX_BRIGHTNESS = 100

    def __init__(self, brightness: int) -> None:
        self.__brightness = brightness

    @property
    def brightness(self):
        return self.__brightness
    
    # @brightness.setter
    def brightness(self, value) -> None:
        if value < self.__MIN_BRIGHTNESS:
            raise Exception('Низкая яркость')
        elif value > self.__MAX_BRIGHTNESS:
            raise Exception('Высокая яркость')
        self.__brightness = value

    # def brightness(self):
    #     return self.__brightness
    
    # def set_brightness(self, value):
    #     self.__brightness = value

    # bright = property(brightness, set_brightness)
    
    def turn_off(self):
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True

    def is_on(self) -> bool:
        return self.__is_on

light = Light(50)
# light.turn_on()
# light.turn_off()
# print(light.is_on())
# print(light.brightness)
# light.brightness = 1250
# print(light.brightness)




# class Human:
#     unused_var = 100

#     def eat(self):
#         pass

#     def sleep(self):
#         pass

#     def fly(self):
#         pass