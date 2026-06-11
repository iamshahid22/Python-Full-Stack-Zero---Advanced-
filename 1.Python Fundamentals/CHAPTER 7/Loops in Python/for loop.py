# loop through a range of number
for i in range(5):
    print(i)
    
# range (start,stop,step)
for j in range(1,11):
    print(j)
    
for a in range(0,21,2):
    print(a)
    
for b in range(10,0,-1):
    print(b)
    
    
# loop through a list
fruits = ["apple","pineapple","mango"]
for fruit in fruits:
    print(fruit)
    
# loop through string
for letter in "Python":
    print(letter)
    

# loop with index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")