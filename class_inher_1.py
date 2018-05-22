#!/usr/bin/env python3

class Animal(object):
    def __init__(self, name):#must make in name
        self._name = name
    def __repr__(self):
        return "test is :{}".format(self.name)
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value


class Dog(Animal):
    def bark(self):
        print(self.get_name() + "is making sound wangwan")
class Cat(Animal):
    def bark(self):
        print(self.get_name() + "is making sound mmmg")
    
# t = Test("python")#class`s instance#instance 
#print(t)
#print (t.name)
dog = Dog("bandian")
cat = Cat("kitty")
dog.bark()
cat.bark()

print("---------------")
animals = [Dog("caiwang"),Cat('kitty'),Dog("laifu"),Cat('betty')]
# list store the instance?
print(type(animals))
print(type(animals[1]))
for animal in animals:
    animal.bark()  # equal to Dog("caiwang")


print("---------------")
Dog("wangcai").bark()
