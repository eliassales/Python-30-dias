''' Ejercicio punto 6 al 10 '''
import math

# Punto 6
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input("Ingrese la base del rectángulo: ")
height = input("Ingrese la altura del rectángulo: ")
area = float(length) * float(height)
perimeter = 2 * (float(length) + float(height))
print("El área es: ", area, ". El perímetro es: ", perimeter)

# Punto 7
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = input("Ingrese el radio del círculo: ")
area = math.pi * float(radius) * float(radius)
circumference = 2 * math.pi * float(radius)
print("El área es: ", area, ". La circunferencia es: ", circumference)

# Punto 8
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x_intercept = 5
y_intercept = (2*x_intercept) - 2
slope1 = y_intercept / x_intercept
print("La pendiente 1 de la recta es: ", slope1)

# Punto 9
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope2 = (y2-y1) / (x2 - x1)
print("La pendiente 2 de la recta es: ", slope2)

# Punto 10
# Compare the slopes in tasks 8 and 9.
print("La pendiete 1 es igual a la pendiente 2: ", slope1 == slope2)
print("La pendiete 1 es mayor a la pendiente 2: ", slope1 > slope2)
print("La pendiete 1 es menor a la pendiente 2: ", slope1 < slope2)
print("La pendiete 1 es mayor o igual a la pendiente 2: ", slope1 >= slope2)
print("La pendiete 1 es menor o igual a la pendiente 2: ", slope1 <= slope2)
print("La pendiete 1 es distinta a la pendiente 2: ", slope1 != slope2)
