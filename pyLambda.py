#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
x=lambda a : a+10
print(x(2))

x=lambda a, b:a * b
print(x(3,5))

def myfunc(n):
    return lambda a: a*n

mydouble=myfunc(2)
mytriple=myfunc(3)
#print(mydouble(10))
print(mydouble(10))
print(mytriple(10))
