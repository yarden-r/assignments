from guardicore_crawler.helpers.singleton import Singleton

# Create a singleton person object
class Person(Singleton):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

p1 = Person('John', 30)
p2 = Person('Jane', 20)

p1.age = 40
print (p1)
print (p2)