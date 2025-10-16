from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version


def menu_principal():
    print(f"{nombre_aplicacion} v.{numero_version}")
    print("=======================================")
    print("[1] Gestión  Talleres")
    print("[2] Gestión  Mecánicos")
    print("[3] Gestión  Clientes")
    print("[4] Gestión  Reparaciones")
    print("[5] Configuración Sistema")
    print("[0] Salir")
