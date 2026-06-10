# Exercise 1: Create a todo list
todo = []
todo.append("Wake up early")
todo.append("Exercise")
todo.append("Study Python")
todo.append("Build project")
print("My Todo List:")
for i, task in enumerate(todo, 1):
    print(f"{i}. {task}")
    
# Exercise 2: Find max, min, average
marks = [90,89,95,91]
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks)/len(marks))

    
# Exercise 3: Reverse a list without slicing
nums = [4,5,67,8,9]
nums.reverse()
print(nums)
