# normal function
def square(x):
    return x**2

#lambda function - same thing but in one line !
square = lambda x: x**2
print(square(5))

#lambda with multiple parameters
add = lambda a,b:a+b
print(add(5,6))

# lambda is great with sort !
students = [("Shahid",90),("Venu",89),("Priya",85)]
students.sort(key=lambda student:student[1])
print(students)