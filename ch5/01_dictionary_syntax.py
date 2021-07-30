'''
a = { "key" : "value" }
a["key"] --> prints "value"

we can also make a dictionary inside a dictionary:
d1 = {
    "key" : "value",
    "d2" : {'key2' : 'value2' , 'key3' : 'value3'}
}

1. Dictionaries are unordered
2. Dictionaries are mutable (we can change the values of keys)
3. It is indexed
4. We cannot form duplicate keys
'''

myDictionary = {
    "marine garden" : "a large area of water or very wet land that is used to grow plants for food",
    "comfort planting": "the activity of putting your favourite plants into the soil in your garden, usually ones that are brightly coloured and easy to grow",
    "Atharv" : "A coder",
    "Marks" : [20 , 25 , 13 , 45],
    "AnotherDictionary" : {'atharv' : 'player'}
}

print(myDictionary['marine garden'])
print(myDictionary['comfort planting'])
print(myDictionary['Atharv'])
print(myDictionary['Marks'])
print(myDictionary['AnotherDictionary'])
print(myDictionary['AnotherDictionary']['atharv'])