def Ejercicio1():
    UserName = input("Introduce el nombre de usuario \n")
    UserAge = int(input("Introduce la edad del usuario \n"))
    print(
        "El nombre es: "
        + UserName
        + " y su edad es: "
        + str(UserAge)
        + " años que al cambio son: "
        + str((UserAge * 360))
        + " dias"
    )


def Ejercicio2():
    while True:
        print("Vamos a calcular el area de un triangulo")
        stop = int(0)
        while stop == 0:
            Base = UserAge = int(input("Introduce la base del triangulo \n"))
            Altura = UserAge = int(input("Introduce la edad del usuario \n"))
            if Base < 0 or Altura < 0 or Base == None or Altura == None:
                print("Tanto la base como la altura deben ser positivos \n")
            else:
                stop += 1
        print("El area del triangulo es: " + (Base * Altura) / 2 + "\n")
        Continue = int(input("Desea continuar? 1 para si, 2 para no \n"))
        if Continue > 1:
            break


def Ejercicio3():
    NumberList = []
    while True:
        stop = 0
        while stop == 0:
            Insert = input("Introduzca el numero \n")
            try:
                Number = int(Insert)
                NumberList.append(Number)
                stop += 1
                Continue = int(
                    input("Desea añadir mas numeros? 1 para si, 2 para no \n")
                )
            except:
                print("Solo se pueden introducir numeros \n")
        if Continue > 1:
            break
    NumberList.sort(reverse=False)
    print(NumberList)

select = int(input("¿Que ejercicio desea abrir? 1 para el ejercicio 1, 2 para el ejercicio 2... \n"))
if select == 1 :
    Ejercicio1()
elif select == 2:
    Ejercicio2()
elif select == 3: 
    Ejercicio3()