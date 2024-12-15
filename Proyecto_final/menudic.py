#Menu inicial
import os
from colorama import init, Fore, Back, Style
init(autoreset=True)

import sqlite3

def crear_tabla_productos():
   conexion = sqlite3.connect("base_datos.db")
   cursor = conexion.cursor()
   cursor.execute('''CREATE TABLE IF NOT EXISTS Productos (
           id INTEGER primary key autoincrement, nombre TEXT, descripcion TEXT, precio REAL, cantidad INTEGER, categoria TEXT) ''')
   conexion.commit()
   conexion.close()
crear_tabla_productos()


titulos = ["Codigo","Nombre", "Descripcion", "Precio", "Cantidad", "Categoria"]

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
    categoria = input("Ingrese la categoria del producto: ")
    productonuevo = {"nombre" : nombre , "descripcion" : descripcion, "precio" : precio, "cantidad" : cantidad, "categoria" : categoria}
    productos.update({idcount : productonuevo})
    idcount += 1

def mostrar_productos() :
    print(*titulos, sep='\t\t')
    for id, producto in productos.items():
        print()
        print(id, end='\t\t')
        for clave in producto:
            print(producto[clave], end='\t\t')
    print("\n")

def mostrar_menu():
    opcion = 0
    while opcion != 7: 
       print(Style.BRIGHT + Fore.YELLOW + "\nMenú de Gestión de Productos".center(40, " "))
       print(Style.BRIGHT + Fore.CYAN + "1. Alta de nuevos productos")
       print(Style.BRIGHT + Fore.CYAN + "2. Consulta de datos de productos")
       print(Style.BRIGHT + Fore.CYAN + "3. Modificar cantidad de stock de un producto")
       print(Style.BRIGHT + Fore.CYAN + "4. Dar de baja productos")
       print(Style.BRIGHT + Fore.CYAN + "5. Buscar producto")
       print(Style.BRIGHT + Fore.CYAN + "6. Lista de productos con bajo stock")
       print(Style.BRIGHT + Fore.RED + "7. Salir")      
       opcion = int(input(Fore.YELLOW + "\nSeleccione una opción entre 1 y 7: "))
       os.system('cls')
       print(f"Has seleccionado la opción {opcion}")
       if(opcion == 1):
        registrar_producto()
       elif(opcion == 2):
        mostrar_productos()

mostrar_menu()