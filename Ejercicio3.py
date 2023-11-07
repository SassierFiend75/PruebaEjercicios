NumberList=[]
while True:
    stop = 0
    while stop == 0 :
        Insert = input("Introduzca el numero \n")
        try : 
            Number = int(Insert)
            NumberList.append(Number)
            stop+=1
            Continue = int(input("Desea añadir mas numeros? 1 para si, 2 para no \n"))
        except :
            print ("Solo se pueden introducir numeros \n")
    if Continue > 1 : 
        break
NumberList.sort(reverse=False)
print(NumberList)