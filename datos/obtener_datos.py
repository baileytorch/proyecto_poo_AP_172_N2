from datos.conexion import Session
from sqlalchemy import func
from modelos.comuna import Comuna
from modelos.combustible import Combustible

sesion = Session()


def obtener_listado_objetos(object):
    listado_objetos = sesion.query(object).all()
    if len(listado_objetos) > 0:
        return listado_objetos


def obtener_comuma_individual(object, comuna: str):
    objeto_especifico = sesion.query(object).filter_by(
        nombre_comuna=comuna.title()).first()
    if objeto_especifico:
        return objeto_especifico


def obtener_combustible_individual(object, combustible: str):
    objeto_especifico = sesion.query(object).filter_by(
        tipo_combustible=combustible.title()).first()
    if objeto_especifico:
        return objeto_especifico
