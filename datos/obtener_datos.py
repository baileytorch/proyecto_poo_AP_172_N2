from datos.conexion import Session
from sqlalchemy import func

sesion = Session()


def obtener_listado_objetos(object):
    listado_objetos = sesion.query(object).all()
    if len(listado_objetos) > 0:
        return listado_objetos
