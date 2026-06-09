#Every character in a string has an index (position number), starting from 0

name = "Python"
#       P y t h o n
#       0 1 2 3 4 5   ← Forward index
#      -6-5-4-3-2-1   ← Backward index

print(name[0])    # P (first character)
print(name[1])    # y
print(name[5])    # n (last character)
print(name[-1])   # n (last character using negative index)
print(name[-2])   # o (second from last)