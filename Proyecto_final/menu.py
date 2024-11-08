#Menu inicial
import os

titulos = ["Nombre", "Cantidad", "Precio unitario"]
productos = []

opcion = 0
while opcion != 7: 
    print("Menu de gestion de productos:\n")

    print("1. Alta de nuevos productos.")
    print("2. Consulta de datos de productos.")
    print("3. Modificar cantidad de stock de un producto.")
    print("4. Dar de baja productos.")
    print("5. Listado de completo de productos.")
    print("6. Lista productos con bajo stock")
    print("7. Salir")

    opcion = int(input("Seleccione una opción entre 1 y 7: "))
    os.system('cls')
    print(f"Has seleccionado la opción {opcion}")
    if(opcion == 1):
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio unitario: "))
        productos.append([nombre, cantidad, precio])
    elif(opcion == 2):
        print(f"{titulos[0]}\t\t{titulos[1]}\t{titulos[2]}")
        for producto in productos:
            print(f"{producto[0]}\t\t{producto[1]}\t\t{producto[2]}")
