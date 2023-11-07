def CrearPlanta():
    planta = dict(Name="", Loca="", DBW=0, Size=0)
    InsertedName = input("Inserte el nombre de la planta \n")
    planta["Name"] = InsertedName
    InsertedLoca = input("Introduzca la localizacion \n")
    planta["Loca"] = InsertedLoca
    stop = 0
    while stop == 0:
        InsertedDBW = input("Introduzca la cantidad de dias entre riegos \n")
        try:
            DER = int(InsertedDBW)
            planta["DBW"] = DER
            stop = 1
        except:
            print("Solo se pueden introducir numeros \n")
    stop = 0
    while stop == 0:
        InsertedSize = input("Introduzca el tamaño de la planta \n")
        try:
            Tamaño = int(InsertedSize)
            planta["Size"] = Tamaño
            stop = 1
        except:
            print("Solo se pueden introducir numeros \n")
    return planta
temporaldict = dict(CrearPlanta())
temporaldict["Name"] = "Nuevo Nombre"
listplant = []
listplant.append(temporaldict)

Continue = input("Desea modificar alguna planta? si = 1 no = 2 \n")
if (Continue == 1):
    
    for i in range(len(listplant)):
        print(listplant[i] + " ")
    Selected = input("Cual desea modificar?, introduzca el nombre de las plantas")
    AtToChange = input("Que atributo desea cambiar. 1 para nombre, 2 para localizacion, 3 para dias entre riegos y 4 para tamaño")
    NumPlant = 0
    for i in len(listplant):
        if (listplant[i]["Name"] == Selected) :
            NumPlant = i
            break
    if (AtToChange == 1):
        NewName = input("Inserte el nuevo nombre de la planta \n")
        listplant[NumPlant]["Name"] = NewName
    if (AtToChange == 2):
        NewLoca = input("Inserte la nueva localizacion de la planta \n")
        listplant[NumPlant]["Loca"] = NewLoca
    if (AtToChange == 3):
        stop = 0
        while stop == 0:
            NewDBW = input("Introduzca la cantidad de dias entre riegos \n")
        try:
            NewDER = int(NewDBW)
            listplant[NumPlant]["DBW"] = NewDER
            stop = 1
        except:
            print("Solo se pueden introducir numeros \n")
    if (AtToChange == 1):
        stop = 0
        while stop == 0:
            NewSize = input("Introduzca el nuevo tamaño de la planta \n")
        try:
            NewTam = int(NewDBW)
            listplant[NumPlant]["Size"] = NewTam
            stop = 1
        except:
            print("Solo se pueden introducir numeros \n")
    
    




#listaDict = [{"name":"hola","lugar":"salon"},{"name":}]
#listaDict[0]["name"] = "atun"