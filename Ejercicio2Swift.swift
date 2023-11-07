print("Para empezar, vamos a decidir el jugador que comienza, como es un juego de dos jugadores se hara a Cara o Cruzplo")
var numAle = Int.random(in:1..<3)
if numAle == 1 {
    print("Ha salido Cara")
}else{
    print("Ha salido Cruzplo")
}
var PosicionBala = Int.random(in:1...6)
print("Una vez escogido quien dispara os vais a ir turnando, por consola vais a ir introduciendo un numero, al sexto fallo, la bala dispara, al adivinar el numero de la posicion de la bala, esta se dispara")
for _ in 1...6 {
    print("Introduzca numero")
    let StringNumber = readLine()!
    let Numero = Int(StringNumber)
    if Numero == PosicionBala {
        print("Bang")     
        break
    }
}
print("Bang")



    
