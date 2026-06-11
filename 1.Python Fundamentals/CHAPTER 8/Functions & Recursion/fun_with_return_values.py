# # return sends back a value
def add(a,b):
    return a+b

result=add(9,4)
print(result)

# Without return, function returns None
def greet(name):
    print(f"Hello,{name}!")
    # return name

x=greet("Shahid")
print(x)

# Return multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([1,3,2,4,5,6,8])
print("Low:",low)
print("High:",high)