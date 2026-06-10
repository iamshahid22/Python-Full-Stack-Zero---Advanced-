#nested lists - lists inside lists
# 2D list - like a table
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])       # [1, 2, 3] (first row)
print(matrix[1][2])    # 6 (row 1, column 2)
print(matrix[2][0])    # 7 (row 2, column 0)

# Student grades example
students = [
    ["Shahid", 90, "A"],
    ["Rahul", 75, "B"],
    ["Priya", 85, "A"]
]

print(students[0][0])   # Shahid
print(students[0][1])   # 90