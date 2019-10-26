#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
tuple1=("apple","banana","cherry","mango")
print(tuple1)
print(tuple1[1])
print(tuple1[-1])
print(tuple1[1:4])
for x in tuple1:
    print(x)

#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
tuple2=("mango",)
print(type(tuple2))

tuple3=("mango")
print(type(tuple3))
#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
#The del keyword can delete the tuple completely:
del tuple3