myDict = {
    "fast" : "In a quick manner",
    "atharv" : "A coder",
    "marks": [1,2,3,4],
    "d2" : {'atharv' : 'Player'},
    1 : 2
}

# Dictionary Methods :
print(myDict.keys())        # prints the keys of the dictionary
print(myDict.values())      # prints the values of the dictionary
print(type(myDict.keys()))  # we can convert it into a list by list(myDict.keys())
print(myDict.items())       # prints the items (keys and values) of the dictionary

# update() appends content(s) in a dictionary
updateDict = {
    "kalash" : "friend",
    "atharv" : "A dancer",  #updates in old dict too
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("ak"))     # Prints value associated with key "ak"
print(myDict["ak"])         # Prints value associated with key "ak"

# The difference between .get and [] syntax in dictionaries:
print(myDict.get("ak"))     # Returns None as ak is not present in myDict
print(myDict["ak"])         # throws an error as ak was not found in myDict (KeyError: 'ak')

# More methods: https://docs.python.org/3/c-api/dict.html