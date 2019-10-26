''' Dictionary
A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values.
'''
dict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":1984
}
print(dict1)
x=dict1["model"]
print(x)
y=dict1.get("brand")
print(y)
dict1["year"]=2001
print(dict1["year"])

for x in dict1:
    print(x)
    print(dict1[x])

for x in dict1.values():
    print(x)
for x, y in dict1.items():
    print(x,y)
#To determine if a specified key is present in a dictionary use the in keyword:
if "models" in dict1:
    print("model is in the dictionary")
#To determine how many items (key-value pairs) a dictionary has, use the len() method.
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
dict1["color"]="red"
print(dict1)
'''There are several methods to remove items from a dictionary:
The pop() method removes the item with the specified key name: thisdict.pop("model")
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
The del keyword removes the item with the specified key name:
The del keyword can also delete the dictionary completely:
The clear() keyword empties the dictionary:
'''