from modelos import Marca, Pais
from datos.obtener_datos import obtener_listado_objetos
from datos.insertar_datos import insertar_objeto
from auxiliares.comparar_strings import normalizar_string
from negocio.negocio_pais import obtener_pais_por_nombre
from prettytable import PrettyTable


def obtener_listado_marcas():
    tabla_marcas = PrettyTable()
    tabla_marcas.field_names = ['N°', 'Nombre Marca', 'País de Origen']
    listado_marcas = obtener_listado_objetos(Marca)
    if listado_marcas:
        for marca in listado_marcas:
            tabla_marcas.add_row(
                [marca.id, marca.nombre_marca, marca.pais_origen])
        print(tabla_marcas)


def obtener_listado_marcas_pais():
    pais = input('Ingrese nombre de país de origen: ')


def obtener_marca_por_nombre(nombre_marca):
    marca_encontrada = None
    listado_marcas = obtener_listado_objetos(Marca)
    if listado_marcas:
        for marca in listado_marcas:
            if normalizar_string(marca.nombre_marca) == normalizar_string(nombre_marca):
                marca_encontrada = marca
        if marca_encontrada != None:
            return marca_encontrada
        else:
            print('Marca NO encontrada.')


def agregar_marca():
    marca = input('Ingrese nombre de marca: ')
    buscar_marca = obtener_marca_por_nombre(marca)
    if buscar_marca:
        print(f'Marca {buscar_marca.nombre_marca} ya existe.')
    else:
        while True:
            pais = input('Ingrese nombre de país de origen: ')
            if pais != '':
                buscar_pais = obtener_pais_por_nombre(pais)
                if buscar_pais != None:
                    pais = buscar_pais.id
                    break
                else:
                    print('Intente nuevamente...')

        if marca != '':
            nueva_marca = Marca(nombre_marca=marca, id_pais=pais)
            insertar_objeto(nueva_marca)


def editar_marca():
    pass


def elimnar_marca():
    pass
