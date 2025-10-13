import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        da =  datetime.date.today()
        year = da.year
        year2 =(int(year)) -  self.age
        print(year2)
        print(self.name + ", " + (str(self.age)) + " Jahre alt. geboren am " + str(year2) + ".")
class Student(Person):
    def __init__(self, name, age, fach):
        super().__init__(name, age)
        self.fach = fach
    def display(self):
        print(self.name + ", " + (str(self.age)) + "studiert: " + self.fach)
norman = Person("Norman", 18)
norman.display()

alice = Person("Alice", 22)
alice.display()

Endy = Student("Endy", 22, "Wirtschaft")
Endy.display()