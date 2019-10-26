x=""" This is a multiline string
being tesetd in python class
and it's indentation needs to be correct."""
x=''' This is also a multiline string in python 
that starts with three single quotes
and span over multiple line.'''
x="Hello, this, is, string lessons     "
print(x[0])
#Get the characters from position 1 to position 5 (not included):
print(x[1:5])
#Use negative indexes to start the slice from the end of the string:
print(x[-20:-15])
print(len(x))
#The strip() method removes any whitespace from the beginning or the end:
print(x.strip())
print(x.lower())
print(x.upper())
print(x.replace("s", "z"))
print(x.split(","))
print(x.strip().lower().split(","))
txt="The raon in Spain stays mainly in the plain"
a="ain" not in txt
'''To check if a certain phrase or character is present in a string, 
we can use the keywords in or not in.
'''
print(a)

x1="This is"
x2=" a string "
x3="concatenation"
print(x1+x2+x3)

#format()
age=38
add=" 5/8 Gail Gulee, Kalikat"
p="Mohan is an Indian and his age is {} and he live at {}"
print(p.format(age,add))
