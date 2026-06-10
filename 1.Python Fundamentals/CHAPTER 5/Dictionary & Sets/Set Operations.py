set1 = {1,2,3,4,5}
set2 = {6,4,7,8,9}

#union - all items from both
print(set1 | set2)
print(set1.union(set2))

#intersection - only common items 
print(set1 & set2)
print(set1.intersection(set2))

#difference - displays only in set1 but not common in set2
print(set1 - set2)
print(set1.difference(set2))

#symmetric difference - displays except common in both sets 
print(set1 ^ set2)

# add & remove
fruits = {"papaya","kiwi"}
fruits.add("mango")
print(fruits)

fruits.discard("papaya")
fruits.discard("pineapple") # no error if not found 
print(fruits) 
