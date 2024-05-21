from paquetes.inventario import *

import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def menu():
    opcion = ["Agregar producto", "Actualizar cantidad de un producto", "Buscar producto", "Mostrar inventario", "Salir"]
    resp = None

    while not resp:
        clear()
        for i in range(len(opcion)):
            print(f'{i + 1} - {opcion[i]}')
        resp = input("Escoja una opcion: ")
        if not resp.isdigit():
            print("Introduzca un valor correcto")
            input("Presione enter para continuar...")
            resp = None
            continue
        resp = int(resp)
        if resp < 1 or resp > len(opcion):
            print("Escoja un valor correcto")
            input("Presione enter para continuar...")
            resp = None
            continue
    if resp == 5:
        exit()

    match resp:
        case 1:
            agregar_producto()
        case 2:
            actualizar_cantidad(input("Ingrese el nombre del producto: "))
        case 3:
            buscar_producto(input("Ingrese el nombre del producto: "))
        case 4:
            mostrar_inventario()