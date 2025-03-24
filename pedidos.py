import json
from utils.manejador_json import cargar_datos, guardar_datos

FILE_PEDIDOS = "data/pedidos.json"
FILE_PRODUCTOS = "data/productos.json"


def menu_gestionar_pedidos():
    while True:
        print("\n--- Gestión de Pedidos ---")
        print("1. Crear Pedido")
        print("2. Listar Pedidos")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_pedido()  # Llama a la función que maneja la creación de pedidos
        elif opcion == "2":
            listar_pedidos()  # Llama a la función que lista los pedidos
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.") 
            
import json

# Ruta del archivo JSON donde se guardan los pedidos
PEDIDOS_FILE = "pedidos.json"

# Función para cargar pedidos desde el archivo JSON
def cargar_pedidos():
    try:
        with open(PEDIDOS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retorna una lista vacía si el archivo no existe o está vacío

# Función para guardar pedidos en el archivo JSON
def guardar_pedidos(pedidos):
    with open(PEDIDOS_FILE, "w", encoding="utf-8") as file:
        json.dump(pedidos, file, indent=4, ensure_ascii=False)

# Función para crear un pedido
def crear_pedido():
    pedidos = cargar_pedidos()

    codigo_pedido = input("Ingrese el código del pedido: ")
    cliente = input("Ingrese el nombre del cliente: ")

    pedido = {
        "codigo": codigo_pedido,
        "cliente": cliente,
        "productos": []
    }

    while True:
        producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == "fin":
            break

        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        precio_unitario = float(input(f"Ingrese el precio unitario de {producto}: "))

        pedido["productos"].append({
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario
        })

    pedidos.append(pedido)
    guardar_pedidos(pedidos)

    print("Pedido creado con éxito.")

# Función para listar pedidos
def listar_pedidos():
    pedidos = cargar_pedidos()

    if not pedidos:
        print("No hay pedidos registrados.")
        return

    print("\n--- Lista de Pedidos ---")
    for pedido in pedidos:
        print(f"Código: {pedido['codigo']}, Cliente: {pedido['cliente']}")
        for producto in pedido["productos"]:
            print(f"   - {producto['producto']}: {producto['cantidad']} unidades, ${producto['precio_unitario']} c/u")
        print("-" * 30)

# Función del menú de gestión de pedidos
def menu_gestionar_pedidos():
    while True:
        print("\n--- Gestión de Pedidos ---")
        print("1. Crear Pedido")
        print("2. Listar Pedidos")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_pedido()
        elif opcion == "2":
            listar_pedidos()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


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
    