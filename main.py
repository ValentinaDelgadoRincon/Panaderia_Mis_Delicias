import menus
import productos
import pedidos
import inventario

ADMIN_USUARIO = "panaderia"
ADMIN_CONTRASEÑA = "1403"

def autenticar():
    """Solicita usuario y contraseña para acceder al inventario."""
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    if usuario == ADMIN_USUARIO and contraseña == ADMIN_CONTRASEÑA:
        return True
    else:
        print("Acceso denegado. Credenciales incorrectas.")
        return False

def mostrar_menu(menu):
    print(menu)

def menu_principal():
    while True:
        mostrar_menu(menus.menu_principal)
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            productos.menu_buscar_producto()  # Aseguramos que se ejecute la búsqueda correctamente
        elif opcion == "2":
            productos.menu_gestionar_productos()
        elif opcion == "3":
            pedidos.menu_gestionar_pedidos()
        elif opcion == "4":
            if autenticar():
             inventario.menu_inventario()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal() 
   
