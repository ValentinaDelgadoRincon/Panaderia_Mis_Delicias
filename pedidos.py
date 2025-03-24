import json
from utils.manejador_json import cargar_datos, guardar_datos

FILE_PEDIDOS = "data/pedidos.json"
FILE_PRODUCTOS = "data/productos.json"

def solicitar_pedido():
    productos = cargar_datos(FILE_PRODUCTOS)
    pedidos = cargar_datos(FILE_PEDIDOS)

    print("\nSeleccione productos:")
    for i, p in enumerate(productos, 1):
        print(f"{i}. {p['nombre']} - ${p['precio_venta']} - Stock: {p['cantidad_en_stock']}")

    pedido = []
    total = 0

    while True:
        seleccion = int(input("Seleccione el número del producto (0 para finalizar): ")) - 1
        if seleccion == -1:
            break
        if seleccion < 0 or seleccion >= len(productos):
            print("Selección inválida.")
            continue
        
        cantidad = int(input("Cantidad: "))
        if cantidad > productos[seleccion]['cantidad_en_stock']:
            print("No hay suficiente stock.")
            continue
        
        total += cantidad * productos[seleccion]["precio_venta"]
        productos[seleccion]["cantidad_en_stock"] -= cantidad
        pedido.append({"producto": productos[seleccion]["nombre"], "cantidad": cantidad, "total": cantidad * productos[seleccion]["precio_venta"]})

    pedidos.append({"codigo_pedido": len(pedidos) + 1, "detalles_pedido": pedido, "total": total})

    guardar_datos(FILE_PEDIDOS, pedidos)
    guardar_datos(FILE_PRODUCTOS, productos)

    print(f"\nPedido registrado. Total: ${total}")