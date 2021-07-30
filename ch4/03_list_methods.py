l1 = [1 , 8 , 7 , 2 , 21 , 15]
print(l1)

#l1_sorted = l1.sort() --> wrong method

l1.sort()       # sorts the list in accending order
print(l1)

l1.reverse()    # sorts the list in decsending order
print(l1)

l1.append(45)   # adds to the end of the list
print(l1)

l1.insert(3,77) # will insert 77 at index 3
print(l1)

l1.pop(2)       # will remove element from index 2
print(l1)

l1.remove(21)   # will remove 21 from the list
print(l1)

# these are not all the methods
# find more at: https://docs.python.org/3/tutorial/datastructures.html