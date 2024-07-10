import funciones as fn
sueldo= {}

while True:
    print("BIENVENIDO")
    print("**********")
    print("1. asignar sueldos")
    print("2. Clasificar sueldos")
    print("3. Ver estadísitcas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    opcion = input("seleccione una opcion...")

    if opcion == "1":
        sueldo = fn.asignar_sueldos()
    elif opcion == "2":
        fn.clasificar_sueldos(sueldo)
    elif opcion == "3":
        fn.estadisticas_sueldos(sueldo)
    elif opcion == "4":
        fn.generar_reporte(sueldo)
    elif opcion=="5":
        print("Finalizando programa...")
        print("Desarrolado por Constanza Jerez")
        print("RUT 21.281.717-1")
        break

