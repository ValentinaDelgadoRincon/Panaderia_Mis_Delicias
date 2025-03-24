import json
import os

def cargar_datos(archivo):
    """Carga los datos desde un archivo JSON. Si el archivo no existe, retorna una lista vacía."""
    if not os.path.exists(archivo):
        guardar_datos(archivo, [])  # Crea el archivo vacío si no existe
        return []

    try:
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []  # Retorna lista vacía si hay un error en el archivo

def guardar_datos(archivo, datos):
    """Guarda los datos en un archivo JSON."""
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)