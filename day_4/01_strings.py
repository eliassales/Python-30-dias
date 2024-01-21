""" Strings """

# *** CREATING STRING ***
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
# String could be made using a single or double quote,"Hello, World!"
greeting = 'Hello, World!'
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# *** MULTILINE STRING ***
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# *** STRING CONCATENATION ***
first_name = 'Elias'
last_name = 'Sales'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Elias Sales
# Checking the length of a string using len() built-in function
print(len(first_name))  # 5
print(len(last_name))   # 5
print(len(first_name) > len(last_name))  # False
print(len(first_name) == len(last_name))  # True
print(len(full_name))  # 11

# *** ESCAPE SEQUENCES IN STRINGS ***
print('I hope everyone is enjoying the Python Challenge.\nAre you ?')  # line break
print('Days\tTopics\tExercises')  # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)')  # To write a backslash
# to write a double quote inside a single quote
print('In every programming language it starts with \"Hello, World!\"')

# output
# I hope every one is enjoying the Python Challenge.
# Are you ?
# Days	Topics	Exercises
# Day 1	5	    5
# Day 2	6	    20
# Day 3	5	    23
# Day 4	1	    35
# This is a backslash  symbol (\)
# In every programming language it starts with "Hello, World!"

# *** STRING FORMATTING ***
# Strings only
first_name = 'Elias'
last_name = 'Sales'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' % (first_name, last_name, language)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2

formated_string = 'The area of circle with a radius %d is %.2f.' % (
    radius, area)  # 2f refers the 2 significant digits after the point
print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries: %s' % (python_libraries)
# "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
print(formated_string)

formated_string = 'I am {} {}. I teach {}'.format(
    first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))  # 4 + 3 = 7
print('{} - {} = {}'.format(a, b, a - b))  # 4 - 3 = 1
print('{} * {} = {}'.format(a, b, a * b))  # 4 * 3 = 12
# 4 / 3 = 1.33 # limits it to two digits after decimal
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))  # 4 % 3 = 1
print('{} // {} = {}'.format(a, b, a // b))  # 4 // 3 = 1
print('{} ** {} = {}'.format(a, b, a ** b))  # 4 ** 3 = 64

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(
    radius, area)  # 2 digits after decimal
print(formated_string)

# *** STRING INTERPOLATION ***
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# *** STRING UNPACKING CHARATERS ***
language = 'Python'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
