food = 'samosa'
food[1]
'a'
# food[;2]
# SyntaxError: invalid syntax
# food[:2}
#SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
food[:2]
'sa'
food[2:]
'mosa'
food[-3:]
'osa'
len(food)
6
myfoo='samosa, jalebi'
'jalebi' in myfoo
#True
'Jalebi' in myfoo
#False
'biryani' in myfoo
#False
'biryani' not in myfoo
#True
food[0] = 'x'
#Traceback (most recent call last):
 # File "<pyshell#23>", line 1, in <module>
   # food[0] = 'x'
#TypeError: 'str' object does not support item assignment
myfoo
'samosa, jalebi'
myfoo.replace('jalebi', 'biryani')
'samosa, biryani'
myfoo
'samosa, jalebi'
dir(myfoo)
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
myfoo.lower()
'samosa, jalebi'
myfoo.upper()
'SAMOSA, JALEBI'
myfoo.index('jalebi')
8
myfoo.index('biryani')
#Traceback (most recent call last):
  #File "<pyshell#31>", line 1, in <module>
   # myfoo.index('biryani')
# ValueError: substring not found
states=29
text=states+'states in India'
#Traceback (most recent call last):
  # File "<pyshell#33>", line 1, in <module>
    # text=states+'states in India'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
text=str(states)
newtext = states + 'states in India'
#Traceback (most recent call last):
 # File "<pyshell#35>", line 1, in <module>
    #newtext = states + 'states in India'
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
newtext = str(states) + 'states in India'
newtext
'29states in India'
s='let\'s learn python'
s
"let's learn python"
# multiline string
dialog = '''kitne admi the?
kalia: 'sardar do!'''
dialog
"kitne admi the?\nkalia: 'sardar do!"
print(dialog)
# kitne admi the?
# kalia: 'sardar do!
# \n meaning spacer for new line
s='hey \tbro'
s
'hey \tbro'
print(s)
# hey 	bro
# \t meaning few spaces
# print combine string
first = 'test'
last = 'testing'
print(first + ' ' + last)
# test testing
# new way to combine using f string
#cprint(f'{first last}')
# SyntaxError: f-string: invalid syntax. Perhaps you forgot a comma?
print(f' {first}')
# SyntaxError: invalid syntax
print(f'{first}')
#test
print(f'{first} {last}')
# test testing

# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
street = "13 patli gali"
city = "New Delhi"
country = "India"
address = street + '\n' + city + '\n' + country
print("Address using + operator:",address)
address = f'{street}\n{city}\n{country}'
print("Address using f-string:",address)

# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index
s='Earth revolves around the sun'
print(s[6:14])
print(s[-3:])

# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this.
num_fruits=10
num_veggies=5
print(f"I eat {num_veggies} veggies and {num_fruits} daily")

# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a
# wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.
s='maine 200 banana khaye'
s=s.replace('banana','samosa')
s=s.replace('200','10')
print("Using two line replace:",s)

s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)