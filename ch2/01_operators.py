a = 3
b = 4

# Arithmetic Operators
print("Arithmetic Operators")
print("The value of 3+4 is" , 3+4)
print("The value of 3-4 is" , 3-4)
print("The value of 3*4 is" , 3*4)
print("The value of 3/4 is" , 3/4)

# Assignment Operators
print("Assignment Operators")
a = 45

print("before assigment operators are used:")
print(a)

print("after assignment operators are used:")
a += 5
print(a ,"+=")

a = 45
a -= 5
print(a , "-=")

a = 45
a *= 5
print(a , "*=")

a = 45
a /= 5
print(a , "/=")

# Comparrision Operators
print("Comparrision Operators")
print(4>5)
print(4<5)
print(4>=5)
print(4<=5)
print(4==5)
print(4!=5)

# Logical Operators
print("Logical Operators")

bool1 = True 
print("bool1 =" , bool1)

bool2 = False
print("bool2 =" , bool2)

print("bool1 AND bool2 =" , (bool1 and bool2))
print("bool1 OR bool2 =" , (bool1 or bool2))
print("NOT bool2 =" , (not bool2))