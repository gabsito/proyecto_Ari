import funciones as fn
msg = '''
**********************************************************************
*                  Mantenimiento de vehiculos                        *
**********************************************************************
Bienvenido a la aplicacion de mantenimiento de vehiculos.
Elija una de las siguientes funciones:

1 :   Cargar datos
2 :   Mantenimiento por placa
3 :   Mantenimiento por partes
4 :   Ayuda
5 :   Salir

'''
filename_mantenimientos = 'tabla_mantenimientos.txt'
filename_historial = 'historial_mantenimientos.txt'
dicMantenimiento = None
dicHistorial = None
print(msg)
op = ""
while op != "5":
    op = input("Opcion: ")
    if op == "1":
        dicMantenimiento, dicHistorial = fn.cargarDatos(filename_mantenimientos, filename_historial)
        print('diccionario historial: ', dicHistorial)
        print('diccionario mantenimiento: ', dicMantenimiento)

    elif op == "2":

        # Valida si los datos estan cargados
        if dicMantenimiento and dicHistorial:
            fn.mantPlaca(dicMantenimiento, dicHistorial)
        else:
            print('No hay datos cargados')

    elif op == "3":

        if dicMantenimiento and dicHistorial:
            fn.mantPartes()
        else:
            print('No hay datos cargados')

    elif op == "4":
        fn.ayuda()
    elif op == "5":
        break
    else:
        print("Opcion no valida.")
        print("""Elija una de las siguientes funciones:

1 :   Cargar datos
2 :   Mantenimiento por placa
3 :   Mantenimiento por partes
4 :   Ayuda
5 :   Salir""")


print("Fin del programa, Hasta la proxima! :D")
