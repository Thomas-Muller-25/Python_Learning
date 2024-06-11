# class Person(object):
#     def __init__(self, name, age):
#         #将属性名以单下划线开头，暗示属性是受保护的
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age < 16:
#             print("%s play 1" % self._name)
#         else:
#             print("%s play 2" % self._name)


# class Person(object):
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age, gender):
#         self._name = name
#         self._age = age
#         self._gender = gender
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @property
#     def gender(self):
#         return self._gender
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#     @age.setter
#     def name(self, age):
#         self._age = age

# from math import sqrt
#
#
# class Triangle(object):
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))
#
#
# if __name__ == '__main__':
#     a, b, c = 3, 4, 5
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         print(Triangle.perimeter(t))
#         print(t.area())
#         print(Triangle.perimeter(t))
#     else:
#         print('invalid parameter for a triangle')

# import os
# from time import time, localtime, sleep
# class Clock(object):
#     def __init__(self, hours, minutes, seconds):
#         self._hours = hours
#         self._minutes = minutes
#         self._seconds = seconds
#
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#
#     def run(self):
#         self._seconds += 1
#         if self._seconds == 60:
#             self._seconds = 0
#             self._minutes += 1
#             if self._minutes == 60:
#                 self._minutes = 0
#                 self._hours += 1
#                 if self._hours == 24:
#                     self._hours = 0
#
#     def show(self):
#         return '%02d:%02d:%02d' % (self._hours, self._minutes, self._seconds)
#
#
# def main():
#     clock = Clock.now()
#     while True:
#         os.system('clear')
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
# if __name__ == '__main__':
#     main()

# class Person(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def eat(self):
#         print('%s is eating steak.' % self._name)
#
#
# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         # super(Student, self).__init__(name, age)
#         self._grade = grade
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @property
#     def grade(self):
#         return self._grade
#
# def main():
#     s = Student('Frank', 11,'大三')
#     print(s.grade)
#     s.eat()
#
#
# if __name__ == '__main__':
#     main()

# from abc import ABCMeta
#
# class Pet(object, metaclass=ABCMeta):
#     def __init__(self, nickname):
#         self._nickname = nickname
#
#     def make_voice(self):
#         pass
#
#     @property
#     def nickname(self):
#         return self._nickname
#
#     @nickname.setter
#     def nickname(self, nickname):
#         self._nickname = nickname
#
# class Dog(Pet):
#    def make_voice(self):
#        print("汪汪汪")
#
# class Pig(Pet):
#     def make_voice(self):
#         print("哼哼哼")
#
#
# def main():
#     pets = [Dog('dodo'), Pig('bobo')]
#     for pet in pets:
#         pet.nickname = '123'
#         print(pet.nickname)
#         pet.make_voice()
#
# if __name__ == '__main__':
#     main()
'''
1. 奥特曼打小怪兽。
'''

from abc import ABCMeta
from random import randint, randrange

class Fighter(object):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @name.setter
    def name(self, name):
        self._name

    @property
    def alive(self):
        return self._hp > 0

    def attack(self, other):
        pass


class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 20)
            return True
        else:
            return False


    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '%s Ultraman\n' % self._name + \
            'Hp: %d\n' % self._hp + \
            'Mp: %d\n' % self._mp


class Monster(Fighter):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '%s Monster\n' % self._name + \
            'Hp: %d\n' % self._hp + \
            'Mp: %d\n' % self._mp

def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive:
            return True
        else:
            return False

def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster)