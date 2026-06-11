# normal way
squares = []
for i in range(1,6):
    squares.append(i**2)
print(squares)

# List Comprehension in one line
squares = [i**2 for i in range(1,10)]
print(squares)

# with condition 
even_squares = [i**2 for i in range(1,11) if i%2==0]
print(even_squares)

# Example 
words = ["hello","world","python","is","awesome"]
words_upper = [w.upper() for w in words if len(w)>4]
print(words_upper)
