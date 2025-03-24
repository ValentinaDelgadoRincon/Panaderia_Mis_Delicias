import json
from utils.manejador_json import cargar_datos, guardar_datos

FILE_PRODUCTOS = "data/productos.json"

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

def listar_productos():
    productos = cargar_datos(FILE_PRODUCTOS)
    for p in productos:
        print(f"{p['codigo_producto']} - {p['nombre']} - ${p['precio_venta']} - Stock: {p['cantidad_en_stock']}")

def eliminar_producto():
    productos = cargar_datos(FILE_PRODUCTOS)
    codigo = input("Código del producto a eliminar: ")

    productos = [p for p in productos if p["codigo_producto"] != codigo]

    guardar_datos(FILE_PRODUCTOS, productos)
    print("Producto eliminado.")
