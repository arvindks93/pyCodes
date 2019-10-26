class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myFunc1(self):
        print("My name is "+ self.name + " and age is:" + self.age)

class Student(Person):
    def __init__(self, name, age, year):
        #Person.__init__(self, name, age)
        super().__init__(name,age)
        self.graduationyear=year

#Python also has a super() function that will make the child class inherit all the methods 
# and properties from its parent:

s1=Student("Ram", 25,2018)
print(s1.name)
print(s1.age)
print(s1.graduationyear)

#If you add a method in the child class with the same name as a function in the parent class, 
# the inheritance of the parent method will be overridden.