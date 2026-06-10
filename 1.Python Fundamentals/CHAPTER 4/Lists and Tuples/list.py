# A Python List is exactly like this — a collection of items in order. You can add, remove, and change items.

fruits = ["apple","banana","mango"]

# Change an item
fruits[1] = "grapes"
print(fruits)

# add an item to end
fruits.append("orange")
print(fruits)

# add multiple items at end
fruits.extend(["pear","papaya"])
print(fruits)

# add an item at specific index/positio
fruits.insert(0,"Kiwi")
print(fruits)

# remove specific item by Value
fruits.remove("pear")
print(fruits)

# remove item by index
a = fruits.pop(0)
print(a)
print(fruits)

# delete specific index
del fruits[3]
print(fruits)

# Clear entire list
# fruits.clear()