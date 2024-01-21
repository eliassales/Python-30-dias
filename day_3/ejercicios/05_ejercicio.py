''' Ejercicio punto 11 al 20 '''

# Punto 11
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# x = input("Ingrese un número: ")
# x = float(x)
x = -3
y = (x * x) + (6 * x) + 9
print("El valor de x fue ", x, " y el valor de Y es: ", y)

# Punto 12
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') != len('dragon'))

# Punto 13
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# Punto 14
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# Punto 15
# There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')

# Punto 16
# Find the length of the text python and convert the value to float and convert it to string
my_string = 'Python'
print(str(float(len(my_string))))

# Punto 17
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
index = 1
print(index % 2 == 0)  # odd, cuando es distinto 0 entonces #odd
index = 2
print(index % 2 == 0)  # even, cuando es igual 0 entonces #even
index = 13
print(index % 2 == 0)  # odd, cuando es distinto 0 entonces #odd
index = 36
print(index % 2 == 0)  # even, cuando es igual 0 entonces #even

# Punto 18
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

# Punto 19
# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Punto 20
# Check if int('9.8') is equal to 10
print(int('9.8') == 10)  # da error
# correccion, y el resultado es False, ya que quita la parte decimal, y se queda solo con 9
print(int(9.8) == 10)
