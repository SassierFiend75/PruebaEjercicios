while True : 
    print("Vamos a calcular el area de un triangulo")
    stop = int(0)
    while stop == 0 :
        Base = UserAge = int(input("Introduce la base del triangulo \n"))
        Altura = UserAge = int(input("Introduce la edad del usuario \n"))
        if Base <0 or Altura <0 or Base == None or Altura == None : 
            print ("Tanto la base como la altura deben ser positivos \n")
        else : 
            stop+=1
    print("El area del triangulo es: "+ (Base*Altura)/2  +"\n")
    Continue = int(input("Desea continuar? 1 para si, 2 para no \n"))
    if Continue > 1 : 
        break