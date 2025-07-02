productos = []

def BuscarProducto(codigo : int):
    for i in range(len(productos)):
        if codigo == codigo:
            return i
    return -1

def RegistrarProducto(codigo : int, nombre : str, stock : int, precio: int):
    if BuscarProducto(codigo) == -1:
        if codigo >=1:
            if len(nombre) >=3:
                if stock >0:
                    if precio >0:
                        datos = {
                            "Código" : codigo,
                            "Nombre" : nombre,
                            "Cantidad" : stock,
                            "Precio" : precio
                        }
                        productos.append(datos)
                        print("Producto registrado")
                    else:
                        print("Precio invalido")
                else:
                    print("Cantidad invalida")
            else:
                print("Nombre invalido")
        else:
            print("Código invalido")
        return False

def ListarProductos():
    for i in range(len(productos)):
        if productos[i]["Cantidad"] > 0:
            print(f"{i+1} - {productos[i]["Código"], {productos[i]["Nombre"]}, {productos[i]["Cantidad"]}, {productos[i]["Precio"]}}")
            return

def EliminarProducto(codigo : int):
    if BuscarProducto(codigo) > 0:
        print("Ingrese el código que quiera eliminar: ")
        if productos(codigo) == codigo:
            codigo.pop()
            print("Producto eliminado")