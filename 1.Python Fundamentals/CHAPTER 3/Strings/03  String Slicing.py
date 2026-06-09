#Slicing = Cutting a piece of the string

text = "Shahiddin Shaik"

print(text[0:])
print(text[0:9])
print(text[10:])
print(text[0:5:1])
print(text[::2])
print(text[::-1])
print(text[:9])
print(text[10:])

# text = "Hello World"
# #       0123456789...

# print(text[0:5])    # Hello (from index 0 to 4, NOT including 5)
# print(text[6:11])   # World
# print(text[0:5:1])  # Hello (step 1)
# print(text[::2])    # HloWrd (every 2nd character)
# print(text[::-1])   # dlroW olleH (REVERSED! Very useful trick!)
# print(text[:5])     # Hello (from start to 4)
# print(text[6:])     # World (from 6 to end)

# string[start : stop : step]
#          ↓       ↓      ↓
#       where   where   jump
#       start   stop    size