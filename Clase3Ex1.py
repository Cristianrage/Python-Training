#El usuario ingresa dos numeros enteros y se muestra el resultado de todas las
#operaciones suma, resta, division, multiplicacion y modulo

num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
modulo = num1 % num2

print(f"La suma de {num1} y {num2} es igual a {suma}")
print(f"La resta de {num1} y {num2} es igual a {resta}")
print(f"La multiplicación de {num1} y {num2} es igual a {multiplicacion}")
print(f"El modulo de {num1} y {num2} es igual a {modulo}")
