''' Variables '''
import math

# Day 2: 30 Days of python programming

first_name = 'Elias'
last_name = 'Sales'
full_name = f"{first_name} {last_name}"
country = "Argentina"
city = "Córdoba"
age = 37
year = 2023
is_married = False
is_true = True
is_light_on = True

profesion, study, university = 'Engineer', 'Computer Science Engineer', 'Universidad Blas Pascal'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(first_name), len(last_name))

num_one, num_two = 5, 4

total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(math.pi)
radio = 30
area_of_circle = math.pi * (radio**2)
circum_of_circle = 2 * math.pi * radio

radio = input("Ingrese el radio del circulo: ")
radio = float(radio)
area_of_circle = math.pi * (radio**2)
circum_of_circle = 2 * math.pi * radio
print("El area es:", area_of_circle)
print("El perímetro es:", circum_of_circle)

first_name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
country = input("Ingrese su país: ")
age = input("Ingrese su edad: ")

print(first_name, last_name, 'Pais: ', country, 'Edad: ', age)

help('keywords')

print(pow(89, 1/2))  # igual que 8 ** (1/2)
