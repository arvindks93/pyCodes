# use of gloab keyword
def myFunc():
    global x
    x="Awesome"
    #print ("Python is " + x)

myFunc()
print("Python is "+x)

y="fantasic"
def myFunc2():
    global y
    y="great"

myFunc2()

print ("Python is "+y)