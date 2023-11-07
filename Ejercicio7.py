miTupla = ("cuadro", "coche", "perro")

def AñadirATupla(): 
    TempList = list(miTupla)
    Add = input("Introduzca lo que se quiera introducir")
    TempList.append(Add)
    miTupla = tuple(TempList)
AñadirATupla()
print(miTupla)
    