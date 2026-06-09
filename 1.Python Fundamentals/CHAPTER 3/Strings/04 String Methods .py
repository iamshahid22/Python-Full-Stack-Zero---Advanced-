#Python has TONS of built-in tools for strings
text = " Shahiddin Shaik "

#case methods
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

#space methods
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#search methods
print(text.find("Shaik"))
print(text.count("i"))
print("hi" in text)
print(text.startswith("S"))
print(text.endswith(" "))

#replace methods
print(text.replace("Shaik", "Hello"))

#split and join
list = "apple,banana,orange"
fruits = list.split(",")
print(fruits)

join = "-".join(fruits)
print(join)

#length
print(len(text))


# text = "  Hello World  "

# # CASE methods
# print(text.upper())        # "  HELLO WORLD  "
# print(text.lower())        # "  hello world  "
# print(text.title())        # "  Hello World  "
# print(text.capitalize())   # "  hello world  " (only first letter of string)
# print(text.swapcase())     # "  hELLO wORLD  "

# # SPACE methods
# print(text.strip())        # "Hello World" (removes spaces from both sides)
# print(text.lstrip())       # "Hello World  " (removes left spaces)
# print(text.rstrip())       # "  Hello World" (removes right spaces)

# # SEARCH methods
# print(text.find("World"))  # 8 (finds the index where "World" starts)
# print(text.count("l"))     # 3 (counts how many times "l" appears)
# print("Hello" in text)     # True (checks if "Hello" exists in text)
# print(text.startswith("  Hello"))  # True
# print(text.endswith("  "))         # True

# # REPLACE methods
# print(text.replace("World", "Python"))  # "  Hello Python  "

# # SPLIT & JOIN
# sentence = "hi,hello,bye"
# sen = sentence.split(",")    # ['hi', 'hello', 'bye']
# print(sen)

# joined = "-".join(fruits)       # "apple-banana-mango"
# print(joined)

# # LENGTH
# print(len(text))    # 15 (counts ALL characters including spaces)