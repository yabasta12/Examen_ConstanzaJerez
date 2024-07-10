import random
import csv
from statistics import geometric_mean

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"] 


def asignar_sueldos():

    sueldos={}
    for trabajador in trabajadores:
        sueldo= random.randint (300000,2500000)
        descuentoAFP= round(sueldo*0.12)
        descuentoSalud= round(sueldo*0.07)
        sueldoLiquido = sueldo-descuentoAFP-descuentoSalud

        sueldos[trabajador]= {"sueldoBase":sueldo,
                                "descuentoAFP":descuentoAFP,
                                "descuentoSalud":descuentoSalud,
                                "sueldoLiquido":sueldoLiquido}
    print(sueldos)
    return sueldos
    

def clasificar_sueldos(sueldos):
    if sueldos == {}:
        print("Por favor, primero asigne sueldos a los trabajadores")
        return
    
    sueldo_menor={}
    sueldo_medio={}
    sueldo_mayor={}

    for trabajador,sueldo in sueldos.items():
        if sueldo["sueldoBase"] < 800000:
            sueldo_menor[trabajador] = sueldo["sueldoBase"]
        elif sueldo["sueldoBase"] >=800000 and sueldo["sueldoBase"] <=2000000:
            sueldo_medio[trabajador]= sueldo["sueldoBase"]
        elif sueldo["sueldoBase"] > 2000000:
            sueldo_mayor[trabajador]=sueldo["sueldoBase"]

    print("el número de trabajadores con sueldo menor a $800.000 es de:", len(sueldo_menor))
    for trabajador,sueldo in sueldo_menor.items():
        print(trabajador,"$",sueldo)
    print("el número de trabajadores con sueldo entre $800.000 y $2.000.000 es de:", len(sueldo_medio))
    for trabajador,sueldo in sueldo_medio.items():
        print(trabajador,"$",sueldo)
    print("el número de trabajadores con sueldo mayor a $2.000.000 es de:",len(sueldo_mayor))
    for trabajador, sueldo in sueldo_mayor.items():
        print(trabajador, "$", sueldo)

def estadisticas_sueldos(sueldos):
    if sueldos == {}:
        print("Por favor, primero asigne sueldos a los trabajadores")
        return
    
    Sueldo_lista=[]

    for trabajador,sueldo in sueldos.items():
        Sueldo_lista.append(sueldo["sueldoBase"])
    maximo= max(Sueldo_lista)
    minimo = min(Sueldo_lista)
    promedio= round(sum(Sueldo_lista)/len(Sueldo_lista))
    media_geo= round(geometric_mean(Sueldo_lista))

    for trabajador, sueldo in sueldos.items():
        if sueldos[trabajador]== maximo:
            print("el trabajador con el sueldo más alto es:", trabajador,"con un total de:", sueldo)
        elif sueldos[trabajador]== minimo:
            print("el trabajador con el sueldo más bajo es:", trabajador, "con un total de:", sueldo)
        print("el promedio de sueldos es de:", promedio)
        print("la media geométrica es de:", media_geo)

def generar_reporte(sueldos):
    if sueldos == {}:
        print("Por favor, primero asigne sueldos a los trabajadores")
        return
    
    with open ("reporteSueldos.csv","w",newline="") as archivo:
        escritor= csv.writer(archivo, delimiter=",")
        escritor.writerow([f"trabajador\t\t,sueldoBase\t\t,descuentoAFP\t\t,descuentoSalud\t\t,SueldoLiquido\t\t"])
        for trabajador,datos in sueldos.items():
            escritor.writerow ([trabajador,datos["sueldoBase"], datos["descuentoAFP"],datos["descuentoSalud"],datos["sueldoLiquido"]])


    print(f"Nombre trabajador \t\t, Sueldo Base\t\t, Descuento AFP\t\t, Descuento Salud\t\t, Sueldo líquido")
    for trabajador, datos in sueldos.items():
        print([trabajador,datos["sueldoBase"], datos["descuentoAFP"],datos["descuentoSalud"],datos["sueldoLiquido"]])
    



