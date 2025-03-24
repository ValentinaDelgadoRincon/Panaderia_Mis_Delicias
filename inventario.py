from utils.manejador_json import cargar_datos, guardar_datos
import json

FILE_PRODUCTOS = "data/productos.json"

# Función para modificar el inventario de un producto
def modificar_inventario():
    productos = cargar_datos(FILE_PRODUCTOS)
    codigo = input("Ingrese el código del producto: ").strip().lower()
    
    for p in productos:
        if p["codigo_producto"].strip().lower() == codigo:
            nueva_cantidad = int(input("Nueva cantidad en stock: "))
            p["cantidad_en_stock"] = nueva_cantidad
            guardar_datos(FILE_PRODUCTOS, productos)
            print("Inventario actualizado.")
            return
    
    print("Producto no encontrado.")

# Función para listar el inventario correctamente desde productos.json
def mostrar_inventario():
    productos = cargar_datos(FILE_PRODUCTOS)  # Leer productos desde productos.json
    
    if not productos:
        print("No hay productos en el inventario.")
        return

    print("\n--- Inventario ---")
    for p in productos:
        print(f"Código: {p['codigo_producto']} | Nombre: {p['nombre']} | Stock: {p['cantidad_en_stock']} | Precio: ${p['precio_venta']}")
    print("-" * 30)

# Función para actualizar el stock de un producto
def actualizar_stock():
    productos = cargar_datos(FILE_PRODUCTOS)
    
    codigo_producto = input("Ingrese el código del producto a actualizar: ").strip().lower()
    
    for producto in productos:
        if producto["codigo_producto"].strip().lower() == codigo_producto:
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {producto['nombre']}: "))
            producto["cantidad_en_stock"] = nueva_cantidad
            guardar_datos(FILE_PRODUCTOS, productos)
            print("Stock actualizado correctamente.")
            return
    
    print("Producto no encontrado en el inventario.")

# Menú de gestión de inventario
def menu_inventario():
    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Mostrar Inventario")
        print("2. Actualizar Stock")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            actualizar_stock()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
