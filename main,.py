from datos.obtener_datos import obtener_listado_objetos, obtener_objeto_individual, obtener_combustible_individual
from modelos.comuna import Comuna
from modelos.combustible import Combustible


def obtener_listado_comunas():
    objeto = Comuna
    listado_comunas = obtener_listado_objetos(objeto)
    if listado_comunas:
        for comuna in listado_comunas:
            print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')


def obtener_comuna_inidividual():
    objeto = Comuna
    nombre_comuna = input('Ingrese nombre de comuna a buscar: ')
    comuna_encontrada = obtener_objeto_individual(objeto, nombre_comuna)
    if comuna_encontrada:
        print(f'{comuna_encontrada.id} {comuna_encontrada.codigo_comuna} {comuna_encontrada.nombre_comuna}')


def obtener_listado_cobustibles():
    objeto = Combustible
    listado_combustibles = obtener_listado_objetos(objeto)
    if listado_combustibles:
        for combustible in listado_combustibles:
            print(
                f'{combustible.id} {combustible.tipo_combustible} {combustible.descripcion_tipo_combustible}')


def obtener_combustible_inidividual():
    objeto = Combustible
    nombre_combustible = input('Ingrese combustible a buscar: ')
    combustible_encontrado = obtener_objeto_individual(
        objeto, nombre_combustible)
    if combustible_encontrado:
        print(f'{combustible_encontrado.id} {combustible_encontrado.tipo_combustible} {combustible_encontrado.descripcion_tipo_combustible}')


obtener_comuna_inidividual()
obtener_combustible_inidividual()

# from iu.menu_principal import menu_principal

# def main():
#     while True:
#         print()
#         menu_principal()
#         print()
#         opcion = input("Seleccione su opción [0-3]: ")

#         if opcion == "1":
#             pass
#         elif opcion == "2":
#             pass
#         elif opcion == "3":
#             pass
#         elif opcion == "0":
#             print("Saliendo del sistema...")
#             break
#         else:
#             print("Opción NO corresponde, ingrese nuevamente...")

# main()
