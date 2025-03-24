from utils.manejador_json import cargar_datos, guardar_datos

FILE_PRODUCTOS = "data/productos.json"

def modificar_inventario():
    productos = cargar_datos(FILE_PRODUCTOS)
    codigo = input("Ingrese el código del producto: ")
    
    for p in productos:
        if p["codigo_producto"] == codigo:
            nueva_cantidad = int(input("Nueva cantidad en stock: "))
            p["cantidad_en_stock"] = nueva_cantidad
            guardar_datos(FILE_PRODUCTOS, productos)
            print("Inventario actualizado.")
            return
    
    print("Producto no encontrado.")

def listar_inventario():
    productos = cargar_datos(FILE_PRODUCTOS)
    for p in productos:
        print(f"{p['codigo_producto']} - {p['nombre']} - Stock: {p['cantidad_en_stock']}")