student = {
    "name": "Shahiddin",
    "age": "20",
    "city": "Kurnool",
    "cgpa": "6.87"
}

print(student.keys())
print(student.values())
print(student.items())

#loop through dictionary
for key in student:
    print(key, ":", student[key])
    

#loop with items
for key, value in student.items():
    print(f"{key}-> {value}")
    

#check key exists or not 
print("name" in student)
print("phone" in student)

#length 
print(len(student))

#clear everything
# student.clear()
