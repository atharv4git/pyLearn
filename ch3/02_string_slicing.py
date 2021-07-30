# greeting = "Good Morning"
# name = "atharv"

# print(greeting + " " + name)  # Concatenation

name = input("Enter a fun name:")
# for x in range(0 , len(name) , 1):
#     print(name[x])
'''
here len(name) is for total length of the string
"for x in range():" is the syntax for FOR LOOP in python
the string is sliced and showed in terminal
'''

#we cannot change the character in a string

#print(name[0:3])    # excluding 3
print(name[0:6] , "name[0:6]")
print(name[1:6] , "name[1:6]")
print(name[:6] , "name[:6]")     #is same as name[0:6]
print(name[1:] , "name[1:]")     #is same as name[1:6]


# Negative Indices
print(name[-4:-1] , "name[-4:-1]")

#skip value
name2 = "demotext"
d = name2[0::2]
print(d)