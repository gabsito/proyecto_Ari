
def cargarDatos(filename_mantenimientos: str, filename_historial: str):
    dic_mantenimientos = {'Preventivo': {}, 'Correctivo': {}}
    dic_historial = {}  # claves del diccionario son las placas

    # Abre el archivo usando encoding UTF-8 para evitar problemas con caracteres
    f1 = open(filename_mantenimientos, "r", encoding='UTF-8')
    for line in f1:
        line = line.strip().replace(' ', '').split(",")
        if line[0] in dic_mantenimientos:
            dic_mantenimientos[line[0]][line[1]] = {'Dias': int(line[2]), 'km': int(line[3])}
    f1.close()

    f2 = open(filename_historial, "r", encoding='UTF-8')
    placas = []
    for line in f2:
        line = line.strip().replace(' ', '').split(",")
        if line[0] not in placas:  # si la placa no estaba en el diccionario
            placas.append(line[0])
            dic_historial[line[0]] = {line[2]: {'Dias': int(line[3]), 'km': int(line[4])}}
        else:
            dic_historial[line[0]][line[2]] = {'Dias': int(line[3]), 'km': int(line[4])}
    f2.close()

    print('Datos cargados con exito! :D')

    return dic_mantenimientos, dic_historial


def mantPlaca(dicMantenimiento, dicHistorial: dict):
    placa = input('Ingrese placa: ')
    while placa not in dicHistorial:
        placa = input('Ingrese una placa valida: ')
    mantenimientos = dicHistorial[placa]
    print('Mantenimientos no realizados: ')
    for parte in dicMantenimiento['Preventivo'].keys():
        if parte not in mantenimientos:
            print('Falta mantenimiento preventivo de', parte)
    for parte in dicMantenimiento['Correctivo'].keys():
        if parte not in mantenimientos:
            print('Falta mantenimiento correctivo de', parte)



def mantPartes():
    print("Opcion mantenimiento por partes aun no implementada :(")


def ayuda():
    print('''Ayuda:
    1 :   Cargar datos.- Carga los datos en el sistema.
    2 :   Mantenimiento por placa.- Permite ingresar la placa del vehiculo para luego mostrar los mantenimientos que no ha recibido.
    3 :   Mantenimiento por partes.- Muestra una lista de placas de vehiculos que requieren el tipo de mantenimiento para una parte especifica.
    4 :   Ayuda.- Muestra este mensaje
    5 :   Salir.- Cierra el programa''')


def mantenimientos(placa, dicHistorial, dicManteminiemto):
    print("falta")

