car=["toyota","ford", "honda" ]
print(car[0])
print(len(car))
car.sort()
#for x in car:
#    print(x)

car.append("bmw")
print(car[3])
car.pop(0)
#The list's remove() method only removes the first occurrence of the specified value.

car.insert(2,"volvo")
for x in car:
    print(x)
