student = {
    "name": "Shahiddin",
    "age": "20",
    "city": "Kurnool",
    "cgpa": "6.87"
}

# method 1 
print(student["name"])
print(student["age"])
print(student["city"])

# method 2
print(student.get("name"))
print(student.get("phone")) #none returns 
print(student.get("age"))