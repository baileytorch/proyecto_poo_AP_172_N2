from iu.menu_principal import menu_principal
from negocio.negocio_comunas import obtener_listado_comunas, obtener_comuna_inidividual
from negocio.negocio_marcas import obtener_listado_marcas, obtener_marca_inidividual, agregar_marca
from modelos.combustible import Combustible
from modelos.comuna import Comuna

from prettytable import PrettyTable


# def obtener_listado_cobustibles():
#     listado_combustibles = obtener_listado_objetos(Combustible)
#     if listado_combustibles:
#         for combustible in listado_combustibles:
#             print(
#                 f'N°: {combustible.id} \nCombustible: {combustible.tipo_combustible} \nDescripción: {combustible.descripcion_tipo_combustible}\n')


# def obtener_listado_comunas():

#     listado_comunas = obtener_listado_objetos(Comuna)
#     if listado_comunas:
#         for comuna in listado_comunas:


# def obtener_combustible_inidividual():
#     objeto = Combustible
#     nombre_combustible = input('Ingrese combustible a buscar: ')
#     combustible_encontrado = obtener_objeto_individual(
#         'combustible', nombre_combustible)
#     if combustible_encontrado:
#         print(f'{combustible_encontrado.id} {combustible_encontrado.tipo_combustible} {combustible_encontrado.descripcion_tipo_combustible}')


# obtener_listado_cobustibles()
# obtener_listado_comunas()
# obtener_comuna_inidividual()
# obtener_combustible_inidividual()


def main():
    while True:
        print()
        menu_principal()
        print()
        opcion = input("Seleccione su opción [0-3]: ")

        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            # obtener_listado_comunas()
            # obtener_comuna_inidividual()
            # obtener_listado_marcas()
            # obtener_marca_inidividual()
            agregar_marca()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción NO corresponde, ingrese nuevamente...")


main()
