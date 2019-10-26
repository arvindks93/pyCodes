class myClass:
    x=5
    name="Ram"
    subjects=["hindi", "english", "math", "science"]

c1=myClass()
#print(c1.x)
#print(c1.name)
for x in c1.subjects:
    #print(x)
    a=10

'''
class constructor
All classes have a function called __init__(), which is always executed 
when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations 
that are necessary to do when the object is being created:
'''
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age =age
    def func1(self):
        print("my name is:" + self.name)

p1=Person("ram", 34)

print(p1.name)
print(p1.age)
p1.func1()
#The __init__() function is called automatically every time the class is being used to create a new object.
#Note: The self parameter is a reference to the current instance of the class, and
#  is used to access variables that belong to the class. IT IS like this

#It does not have to be named self , you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:


