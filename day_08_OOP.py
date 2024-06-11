# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         print('%d years old %s walking on the street.' % (self.age, self.name))
#
#     def sleep(self):
#         print(f'{self.name} is sleeping')

class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __walk(self):
        print('%d years old %s walking on the street.' % (self.__age, self.__name))

    def __sleep(self):
        print(f'{self.__name} is sleeping')



def main():
    p1 = Person('DYW', 20)
    # print(p1.name)
    # print(p1.age)
    # p1.walk()
    # p1.sleep()

    # print(p1.__name)
    # print(p1.__age)
    # p1.__walk()
    # p1.__sleep()

    print(p1._Person__name)
    print(p1._Person__age)
    p1._Person__walk()
    p1._Person__sleep()

if __name__ == '__main__':
    main()





