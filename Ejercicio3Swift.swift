print("Primero, introduzca entre cuantos numeros quiere hacer la media")
var Num = 0
let CantNumString = readLine()!
let CantNumInt = Int(CantNumString)!

func PedirNum() -> Int {
    for i in 1...CantNumInt {
        print("Introduzca el ", i, " numero")
        let StringNum = readLine()!
        let NumPedido = Int(StringNum)!
        Num += NumPedido
        print(Num)
    }
    return Num