#Menu inicial
import os

titulos = ["id","Nombre", "Descripcion", "Precio", "Cantidad", "Categoria"]

Producto1 = {"nombre" : "manzana", "descripcion" : "deliciosa", "precio" : 2000.00, "cantidad" : 100, "categoria" : "fruta"}
Producto2 = {"nombre" : "mayonesa", "descripcion" : "BC", "precio" : 1800.00, "cantidad" : 100, "categoria" : "aderezo"}

productos = {1 : Producto1, 2 : Producto2}

idcount = 3

def ingresar_precio():

    no_es_real = True
    while(no_es_real):
        try:
            precio = float(input("Ingrese el precio unitario: "))
        except ValueError:
            print("Por favor ingrese un número \n")
        else:
            no_es_real = False
            return precio

def ingresar_cantidad():

    no_es_entero = True
    while(no_es_entero):
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
        except ValueError:
            print("Por favor ingrese un número entero como cantidad \n")
        else:
            no_es_entero = False
            return cantidad

def registrar_producto() :
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = ingresar_precio()
    cantidad = ingresar_cantidad()
    productos.append([nombre, cantidad, precio])

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
        registrar_producto()
    elif(opcion == 2):
        print(f"{titulos[0]}\t\t{titulos[1]}\t{titulos[2]}")
        for producto in productos:
            print(f"{producto[0]}\t\t{producto[1]}\t\t{producto[2]}")
