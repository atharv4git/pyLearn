dict = {
    "pankha" : "fan",
    "dabba" : "box",
    "vastu" : "item"
}
print("options are:" , dict.keys())
a = input("Enter a hindi word:")
#print("The meaning of", a ," is:" , dict[a])
# below line will not show an error
print("The meaning of", a ," is:" , dict.get(a))