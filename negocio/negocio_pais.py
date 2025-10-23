from modelos import Pais
from datos.obtener_datos import obtener_listado_objetos
from auxiliares.comparar_strings import normalizar_string
from prettytable import PrettyTable


def obtener_listado_paises():
    tabla_paises = PrettyTable()
    tabla_paises.field_names = ['N°', 'Código ISO', 'País', 'Nacionalidad']
    listado_paises = obtener_listado_objetos(Pais)
    if listado_paises:
        for pais in listado_paises:
            tabla_paises.add_row(
                [pais.id, pais.codigo_iso, pais.pais_origen, pais.nacionalidad])
        print(tabla_paises)


def obtener_pais_por_nombre(buscar_pais):
    pais_encontrado = None
    listado_paises = obtener_listado_objetos(Pais)
    if listado_paises:
        for pais in listado_paises:
            if normalizar_string(pais.nombre_pais) == normalizar_string(buscar_pais):
                pais_encontrado = pais
        if pais_encontrado == None:
            print('País NO encontrad.')
    return pais_encontrado
