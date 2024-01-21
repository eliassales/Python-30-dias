''' Ejercicio punto 21 '''

# Punto 21
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = input("Ingrese la cantidad de horas trabajadas: ")
rate_per_hour = input("Ingrese el monto que gana por hora: ")
pay = float(hours) * float(rate_per_hour)
print(f"Su pago correspondiente es ${pay}")
