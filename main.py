import menus
import productos
import pedidos
import inventario

# Credenciales de administrador
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
            productos.listar_productos()
        elif opcion == "2":
            productos.menu_gestionar_productos()
        elif opcion == "3":
            pedidos.menu_gestionar_pedidos()
        elif opcion == "4":
            if autenticar():
                inventario.menu_inventario()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if _name_ == "_main_":
    menu_principal()
