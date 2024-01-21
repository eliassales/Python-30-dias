''' Ejercicio punto 22 '''

# Punto 22
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = input("Ingrese su edad: ")
years = int(years)

seconds_lived = years * 365 * 24 * 60 * 60
print(f"Has vivido {seconds_lived} segundos")
