import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

lista_productos = [{
    "Nombre del producto": "manzana",
    "Precio": "50bs",
    "Cantidad": "30"
}]


'''
Nombre del producto: ""
Precio: ""
Cantidad: ""
'''

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad en existencia: ")
    producto = {
        "Nombre del producto": nombre,
        "Precio": precio,
        "Cantidad": cantidad
    }
    lista_productos.append(producto)

def actualizar_cantidad(dato):
    resultado = list(filter(lambda elemento: elemento["Nombre del producto"].startswith(dato), lista_productos))
    cantidad = input("Ingrese la cantidad del producto: ")
    producto = {
        "Cantidad": cantidad
    }
    clear()
    for producto in resultado:
        print(f'Nombre del producto: {producto["Nombre del producto"]}\nCantidad: {producto["Cantidad"]}')
        print("==================")
        input("Presione enter para continuar...")

def buscar_producto(dato):
    resultado = list(filter(lambda elemento: elemento["Nombre del producto"].startswith(dato), lista_productos))
    clear()
    for producto in resultado:
        print(f'Nombre del producto: {producto["Nombre del producto"]}\nCantidad: {producto["Cantidad"]}\nPrecio: {producto["Precio"]}')
        print("==================")
        input("Presione enter para continuar...")

def mostrar_inventario():
    clear()
    for producto in lista_productos:
        print(f'Nombre del producto: {producto["Nombre del producto"]}\nPrecio: {producto["Precio"]}\nCantidad: {producto["Cantidad"]}')
        print("==================")
        input("Presione enter para continuar...")