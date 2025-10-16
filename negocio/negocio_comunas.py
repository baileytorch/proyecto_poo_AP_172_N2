from modelos.comuna import Comuna
from datos.obtener_datos import obtener_listado_objetos
from auxiliares.comparar_strings import normalizar_string
from prettytable import PrettyTable


def obtener_listado_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas.field_names = ['N°', 'Código Comuna', 'Nombre Comuna']
    listado_comunas = obtener_listado_objetos(Comuna)
    if listado_comunas:
        for comuna in listado_comunas:
            tabla_comunas.add_row(
                [comuna.id, comuna.codigo_comuna, comuna.nombre_comuna])
        print(tabla_comunas)


def obtener_comuna_inidividual():
    comuna_encontrada = None
    nombre_comuna = input('Ingrese nombre de comuna a buscar: ')
    listado_comunas = obtener_listado_objetos(Comuna)
    if listado_comunas:
        for comuna in listado_comunas:
            if normalizar_string(comuna.nombre_comuna) == normalizar_string(nombre_comuna):
                comuna_encontrada = comuna
        if comuna_encontrada != None:
            print(
                f'{comuna_encontrada.id} {comuna_encontrada.codigo_comuna} {comuna_encontrada.nombre_comuna}')
        else:
            print('Comuna NO encontrada.')
