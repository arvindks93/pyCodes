"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""
import random
x=5 #int
x="Hello world" #str
x=20.5  #float
x=["a", "v", "r"]   #list
x=("a", "w", "3")   #tuple
x=range(6)  # <class 'range'>
x={"name":"Jhon", "age":6}  #<class 'dict'>
x={"Apple", "Banana", "Cherry"} #<class 'set'>
x=frozenset({"Apple", "Banana", "Cherry"})  #"frozenset"
x=True  #bool
x=b"Hello"  #byte
x=bytearray(4)  #bytearray
x=memoryview(bytes(5))  #memoryview
x=2j    #complex
#print(type(x))

y=3+4j
z=4+5j
a=y+z
#print(a)
print(random.randrange(1,10))



#https://www.w3schools.com/python/python_numbers.asp
