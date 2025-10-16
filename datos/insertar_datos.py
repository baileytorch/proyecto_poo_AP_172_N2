from modelos.marca import Marca
from datos.conexion import Session

sesion = Session()


def insertar_marca(nombre, pais):
    nueva_marca = Marca(nombre_marca=nombre, pais_origen=pais)
    sesion.add(nueva_marca)
    try:
        sesion.commit()
        print(
            f"La marca '{nueva_marca.nombre_marca}' se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la marca: {e}")
    finally:
        sesion.close()
