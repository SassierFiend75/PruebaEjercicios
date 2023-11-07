planta = dict(Name="", Loca="", DBW=0, Size=0)


def InsertName():
    InsertedName = input("Inserte el nombre de la planta \n")
    planta["Name"] = InsertedName


def InsertLoca():
    InsertedLoca = input("Introduzca la localizacion \n")
    planta["Loca"] = InsertedLoca


def InsertDBW():
    stop = 0
    while stop == 0:
        InsertedDBW = input("Introduzca la cantidad de dias entre riegos \n")
        try:
            DER = int(InsertedDBW)
            planta["DBW"] = DER
            stop = 1
        except:
            print("Solo se pueden introducir numeros \n")


def InsertSize():
    stop = 0
    while stop == 0:
        InsertedSize = input("Introduzca el tamaño de la planta \n")
        try:
            Tamaño = int(InsertedSize)
            planta["Size"] = Tamaño
            stop = 1
        except:
            print("Solo se pueden introducir numeros \n")


InsertName()
InsertLoca()
InsertDBW()
InsertSize()
print(planta)
