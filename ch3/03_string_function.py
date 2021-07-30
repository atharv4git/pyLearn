story = '''wise men say
Only fools rush in
But I can't help falling in love with you
Shall I stay?
Would it be a sin
If I can't help falling in love with you?
Like a river flows
Surely to the sea
Darling, so it goes
Some things are meant to be
Take my hand
Take my whole life too
For I can't help falling in love with you
Like a river flows
Surely to the sea
Darling, so it goes
Some things are meant to be
Take my hand
Take my whole life too
For I can't help falling in love with you
For I can't help falling in love with you'''

print(len(story))                       # shows the length of a string
print(story.endswith("new"))            # boolean for verifying the ending string characters
print(story.endswith("you"))            # boolean for verifying the ending string characters
print(story.count("a"))                 # shows the occurance of a/some character(s) or a word
print(story.capitalize())               # capitalizes first character of a string
print(story.find("break"))              # will return -1 if the word isn't found
print(story.find("love"))               # will return the place at which the entered word is found first in the string
print(story.replace("I" , "Atharv"))    # will replace the first entered character(s) with the second