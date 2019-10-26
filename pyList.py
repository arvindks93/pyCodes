'''
There are four collection data types in the Python programming language:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, 
it could mean an increase in efficiency or security.
'''
thislist=["apple", "banana","cherry", "grape","mango","malon","kiwi","berry" ]
print(thislist)
#second item
print(thislist[1])
#last item -1
print(thislist[-1])
#second last item
print(thislist[-2])
print(thislist[2:5])
#This example returns the items from index -4 (included) to index -1 (excluded)
print(thislist[-4:-1])
#loop
for x in thislist:
    print(x)

if "apple" in thislist:
    print("Yes, 'apple' is in the fruit list")

print(len(thislist))
#o add an item to the end of the list, use the append() method:
thislist.append("avocado")
#To add an item at the specified index, use the insert() method:
thislist.insert(1,"orange")
print(thislist)

thislist.remove('orange')
print(thislist)
#The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop(1)
print(thislist)
list1=["apple", "banana","cherry", "grape"]
#The del keyword removes the specified index:
del list1[2]
#The del keyword can also delete the list completely:

# The clear() method empties the list:
#list1.clear()
#copy
copylist=list1.copy()
print(copylist)

newlist=list(list1)
print(newlist)
list3=list1 + newlist
print(list3)
#you can use the extend() method, which purpose is to add elements from one list to another list:
list1.extend(newlist)
print(list1)