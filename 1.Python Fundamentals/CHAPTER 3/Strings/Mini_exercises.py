# Exercise 1: Reverse a string
name = "Shahiddin"
reversed_name = name[::-1]
print(reversed_name)

#prepending characters
text = "python"
temp = ""
for i in text:
    temp = i+temp
print(temp)
    
#iterating with range
a="abcdeesf"
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
print(b)
       
#using reversed()
name1 = "Shahiddin"
temp1 = ""
for char in reversed(name1):
    temp1 = temp1+char
print(temp1)


# Exercise 2: Count vowels in a string
word = "python programming"
vowels = "aeiou"
count = 0
for letter in word:
    if letter in vowels:
        count = count + 1 #count+=1
print("Vowels:",count)

# Exercise 3: Check if string is palindrome
c = "racecar"
if c==c[::-1]:
    print("Palindrome!")
else:
    print("Not palindrome!")


# Exercise 4: Format personal info
name = input("enter ur name:")
age = int(input("your age:"))
city = input("enter ur city:")
print(f"My name is {name}, and i am {age} years old, from {city}")