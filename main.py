from funciones import *
from os import system
from msvcrt import getch

while True:
    print("""
    Bienvendio a su supermercado de confanza
    1.- Registrar producto
    2.- Listar productos con stock
    3.- Eliminar producto por código
    4.- Salir
    """)

    select = int(input("Ingrese una opción: "))

    match select:
        case 1:
            codigo = int(input("Ingrese código: "))
            nombre = input("Ingrese nombre del producto: ").capitalize()
            stock = int(input("Ingrese cantidad deseada: "))
            precio = int(input("Ingrese el precio: "))
            RegistrarProducto(codigo, nombre, stock, precio)
        case 2:
            print("Lista de productos")
            print("---------------------------------")
            print("<<<TOQUE UNA TECLA PARA CONTINUAR>>>")
            getch()
            print("Lista de productos")
            ListarProductos()
            getch()
            system("cls")
        case 3:
            print("Eliminar producto por código")
            print("----------------------------------")
            print("Ingrese el códiigo que quiera borrar: ")
            EliminarProducto(codigo)
        case 4:
            print("La compra se cerrará si toca cualquier tecla...")
            getch()
            system("cls")
            print("Muchas gracias por su tiempo")
            break
        case _:
            break