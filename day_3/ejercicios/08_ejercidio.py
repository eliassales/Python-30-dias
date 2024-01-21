''' Ejercicio punto 23 '''

# Punto 23
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print(1, 1, 1,  1,   1)
print(2, 1, 2,  4,   8)
print(3, 1, 3,  9,  27)
print(4, 1, 4, 16,  64)
print(5, 1, 5, 25, 125)

# otra forma
valores = [1, 2, 3, 4, 5]
for item in valores:
    i = 0
    calculo = []
    calculo.append(item)
    calculo.append(1)
    while i < 3:
        num1 = item
        num2 = calculo[-1]
        aux = num1 * num2
        calculo.append(aux)
        i += 1
    print(f"{calculo}")
