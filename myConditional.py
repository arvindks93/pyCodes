# IF conditions begins
'''
a=20
b=33
if a>b:
    print("a is greater than b")
#The elif keyword is pythons way of saying "if the previous conditions were not true, 
# then try this condition".
elif a==b:
    print("a equals b")
#The else keyword catches anything which isn't caught by the preceding conditions.
else:
    print("a is less than b")

a = 330
b = 430
print("A") if a > b else print("=") if a == b else print("B")
''' # END of IF
# Begin while and loop
a=1
while(a<6):
    #if a==3:
    #    break   #break statement we can stop the loop even if the while condition is true
    a+=1
    if a==4:
        continue
    print(a)
#end while and loop
for x in range(6): 
    print(x)
else:
    print("done")

for x in range(2,20,3):
    print( x)

