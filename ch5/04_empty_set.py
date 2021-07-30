# creating an empty set:
a = set()
print(type(a))
print(a)

# Adding values to an empty set:
a.add(1)
a.add(2)
a.add(3)
a.add(6)
a.add(5)
a.add(4)
#a.add([7,8,9])     # TypeError: unhashable type: 'list'
a.add((7,8,9))      # we can add a tuple in a set
#a.add({4:5})       # TypeError: unhashable type: 'dict

print(a)    # it will only print in sorted form

print(len(a))       # prints the length of a set

# Removal:
a.remove(5)         # removes 5 from the set a
#a.remove(45)       # throws an error while removing 45 (not present in the set)
print(a)

# pop() removes a random element and throws it in output
print(a.pop())
print(a)

# clear() emppties the set
#print(a.clear())  -->  output : None