#Set
#A set is a collection which is unordered and unindexed. 
#In Python sets are written with curly brackets.
set1={"apple","banana","cherry","mango","grapes"}
print(set1)
#Note: Sets are unordered, so you cannot be sure in which order the items will appear.
for x in set1:
    print(x)
print("mango" in set1)
#To add one item to a set use the add() method.
set1.add("orange")
print(set1)
#To add more than one item to a set use the update() method.
set1.update(["kiwi","melon"])
print(set1)
#If the item to remove does not exist, remove() will raise an error.
set1.remove("kiwi")
print(set1)
#If the item to remove does not exist, discard() will NOT raise an error.
set1.discard("mango")
print(set1)
#Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
set1={1,2,3, "a"}
set2={"a","b","c", 3}
set3=set1.union(set2)
print(set3)
set2.update(set1)
set4=set2
print(set4)
