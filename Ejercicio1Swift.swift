print("Para hacer la media, introduzca un total de 5 numeros")
print("Introduzca el primer numero")
var StringNumber1 = readLine()
print("Introduzca el segundo numero")
var StringNumber2 = readLine()
print("Introduzca el tercero numero")
var StringNumber3 = readLine()
print("Introduzca el cuarto numero")
var StringNumber4 = readLine()
print("Introduzca el quinto numero")
var StringNumber5 = readLine()
var StringNumber1Final: String = StringNumber1!
var StringNumber2Final: String = StringNumber2!
var StringNumber3Final: String = StringNumber3!
var StringNumber4Final: String = StringNumber4!
var StringNumber5Final: String = StringNumber5!
var Num1 = Int(StringNumber1Final)!
var Num2 = Int(StringNumber2Final)!
var Num3 = Int(StringNumber3Final)!
var Num4 = Int(StringNumber4Final)!
var Num5 = Int(StringNumber5Final)!
var Suma = Num1 + Num2 + Num3 + Num4 + Num5
print("La media es: ", Suma / 5)