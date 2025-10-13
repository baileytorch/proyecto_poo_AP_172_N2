from datos.obtener_datos import obtener_listado_objetos
from modelos.comuna import Comuna

objeto = Comuna

listado_comunas = obtener_listado_objetos(objeto)
if listado_comunas:
    for comuna in listado_comunas:
        print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')

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
