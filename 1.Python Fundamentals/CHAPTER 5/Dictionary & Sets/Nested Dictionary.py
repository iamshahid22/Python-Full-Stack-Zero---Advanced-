# Nested Dictionary -  Dictionary inside dictionary
college = {
    "name": "AITS-TPT",
    "department":"CSE",
    "student" : {
        "name":"shahid",
        "Year":4,
        "cgpa":6.87
    }
}

print(college["student"]["name"])
print(college["student"]["cgpa"])