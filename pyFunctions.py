#In Python a function is defined using the def keyword:
def myFunction(fname="India"):
    print("Hello this is a function with parameter:" + fname)
#To call a function, use the function name followed by parenthesis:
myFunction()
myFunction("Email")

def listFunc(list1):
    for x in list1:
        print(x)
    return len(list1)


fruits=["apple","banana","orange"]
print(listFunc(fruits))
#If the number of arguments are unknown, add a * before the parameter name:
#def func1(ar1, arg2, arg3):
def funcmanyparam(*args):
    print("youngest is: "+args[1])

funcmanyparam("ram", "rahim", "jesu")

#recusrion
def febNum(n):
    if (n>0):
        result=n+febNum(n-1)
        print(result)
    else:
        result=0
    return result
    
febNum(5)
print("Factorial with recursion")
def factorial(n):
    if (n>1):
        result=n * factorial(n-1)
        print(result)
    else:
        result=1
        print(result)
    return result

x=factorial(10)
print(x)
