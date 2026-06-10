#list/tuple unpacking
fruits=["apple","grapes","papaya"]
first, second, third = fruits
print(first)
print(second)
print(third)

#swap two variables
a=10
b=20
a,b=b,a
print(a,b)

#ignores some values with _
c=(10,20,30)
x,_,z=c
print(x,z)