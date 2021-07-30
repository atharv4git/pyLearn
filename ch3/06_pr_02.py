letter = '''Dear <|NAME|> ,
You are Selected!
date: <|DATE|>'''

name = input("Enter your name\n")
date = input("Enter a date\n")

letter = letter.replace("<|NAME|>" , name)
letter = letter.replace("<|DATE|>" , date)

print(letter)