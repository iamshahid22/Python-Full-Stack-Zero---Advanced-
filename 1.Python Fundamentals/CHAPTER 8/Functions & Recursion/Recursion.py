# Recursion = Function calling itself !
def count(n):
    if n<=0:
        print("loop completed !")
        return
    print(n)
    count(n-1)
    
count(6)

# factorial using recursion
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))


# using sys.getrecursionlimit() # get to input
import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(200) # set  to output