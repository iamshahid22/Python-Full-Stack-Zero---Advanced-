# break = exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)
    

# continue = SKIP current iteration, go to next
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
# pass = do nothing
for i in range(5):
    if i == 3:
        pass
    print(i)