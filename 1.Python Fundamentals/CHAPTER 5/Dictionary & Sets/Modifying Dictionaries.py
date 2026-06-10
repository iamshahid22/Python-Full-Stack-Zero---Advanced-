student = {
    "name": "Shahiddin",
    "age": "20",
    "city": "Kurnool",
    "cgpa": "6.87"
}

#Add new key-value
student["phone"]="923123123"
print(student)

#update existing value
student["age"]="21"
print(student)

#delete a key 
del student["phone"]
print(student)

#using pop() - remove and return value
age=student.pop("age")
print(age)
print(student)

#update multiple keys at once
student.update({"age":"22","city":"Hyderbad","course":"Python Full Stack"})
print(student)