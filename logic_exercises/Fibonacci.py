 # Escribe un programa que imprima los 50 primeros números de la sucesión
 # de Fibonacci empezando en 0.
 # - La serie Fibonacci se compone por una sucesión de números en
 #   la que el siguiente siempre es la suma de los dos anteriores.
 #   0, 1, 1, 2, 3, 5, 8, 13...
 #/

def fibonacci(numero):
    if (numero == 0):
        return 0
    else:
        if (numero == 1):
            return 1
        else:
            if(numero >= 2):
                resultado = (fibonacci(numero - 1) + fibonacci(numero - 2)) 
                return resultado


def main():
    num = int(input("Indique cuantos numeros de la serie calcular: "))
    print("Serie de Fibonacci: ")
    for i in range(num):
        serie = fibonacci(i)
        print(f"{serie}",end=", ")

main()