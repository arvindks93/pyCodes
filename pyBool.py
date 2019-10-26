print (8>7)
print (9>10)
print(bool("hello"))
print (bool(0))

''' Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
'''
print (bool([]))
print (bool(["cherry", "apple", "orange"]))

class myClass():
    def __len__(self):
        return 0
print(bool(myClass))

myObj=myClass()
print(bool(myObj))

