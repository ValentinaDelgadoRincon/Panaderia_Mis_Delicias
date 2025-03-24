import json
from utils.manejador_json import cargar_datos, guardar_datos

FILE_PRODUCTOS = "data/productos.json"  # Archivo JSON con los productos

# Función para buscar un producto por código
def buscar_producto_por_codigo():
    productos = cargar_datos(FILE_PRODUCTOS)
    codigo = input("Ingrese el código del producto: ").strip().lower()

    for producto in productos:
        if producto["codigo_producto"] == codigo:
            print("\n--- Producto Encontrado ---")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Proveedor: {producto['proveedor']}")
            print(f"Stock: {producto['cantidad_en_stock']}")
            print(f"Precio de Compra: ${producto['precio_proveedor']}")
            print(f"Precio de Venta: ${producto['precio_venta']}")
            return
    
    print("Producto no encontrado.")

# Función para buscar un producto por nombre
def buscar_producto_por_nombre():
    productos = cargar_datos(FILE_PRODUCTOS)
    nombre = input("Ingrese el nombre del producto: ").strip().lower()

    for producto in productos:
        if producto["nombre"].strip().lower() == nombre:
            print("\n--- Producto Encontrado ---")
            print(f"Código: {producto['codigo_producto']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Proveedor: {producto['proveedor']}")
            print(f"Stock: {producto['cantidad_en_stock']}")
            print(f"Precio de Compra: ${producto['precio_proveedor']}")
            print(f"Precio de Venta: ${producto['precio_venta']}")
            return
    
    print("Producto no encontrado.")

# Submenú de búsqueda de productos
def menu_buscar_producto():
    while True:
        print("\n--- Buscar Producto ---")
        print("1. Buscar por código")
        print("2. Buscar por nombre")
        print("3. Volver al menú anterior")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar_producto_por_codigo()
        elif opcion == "2":
            buscar_producto_por_nombre()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Menú de gestión de productos
def menu_gestionar_productos():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Buscar producto")
        print("2. Agregar producto")
        print("3. Listar productos")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_buscar_producto()  # Ahora este submenu se ejecutará correctamente
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            listar_productos()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Función para agregar un nuevo producto
def agregar_producto():
    productos = cargar_datos(FILE_PRODUCTOS)
    codigo = input("Código del producto: ")
    
    if any(p["codigo_producto"] == codigo for p in productos):
        print("El código ya existe.")
        return
    
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    descripcion = input("Descripción: ")
    proveedor = input("Proveedor: ")
    cantidad = int(input("Cantidad en stock: "))
    precio_venta = float(input("Precio de venta: "))
    precio_proveedor = float(input("Precio de proveedor: "))

    productos.append({
        "codigo_producto": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "descripcion": descripcion,
        "proveedor": proveedor,
        "cantidad_en_stock": cantidad,
        "precio_venta": precio_venta,
        "precio_proveedor": precio_proveedor
    })
    
    guardar_datos(FILE_PRODUCTOS, productos)
    print("Producto agregado exitosamente.")

# Función para listar todos los productos
def listar_productos():
    productos = cargar_datos(FILE_PRODUCTOS)
    
    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- Lista de Productos ---")
    for p in productos:
        print(f"{p['codigo_producto']} - {p['nombre']} - ${p['precio_venta']} - Stock: {p['cantidad_en_stock']}")

# Función para eliminar un producto
def eliminar_producto():
    productos = cargar_datos(FILE_PRODUCTOS)
    codigo = input("Código del producto a eliminar: ")

    productos_actualizados = [p for p in productos if p["codigo_producto"] != codigo]

    if len(productos) == len(productos_actualizados):
        print("El producto no existe.")
    else:
        guardar_datos(FILE_PRODUCTOS, productos_actualizados)
        print("Producto eliminado exitosamente.") 
