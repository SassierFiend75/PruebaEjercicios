print("Introduzca la frase, las palabras que empiecen por j, m o p seran censuradas ")
let Frase = readLine()!
var Letras: [Character] = ["J", "P", "M"]
var FraseMayus = Frase.uppercased()
let FraseSeparada = FraseMayus.split(separator: " ")
var FraseFinal = ""
for palabra in FraseSeparada   {
    var palabra2 : String = String(palabra)
    if palabra.first == "J" || palabra.first == "P" || palabra.first == "M" {
        palabra2 = String(palabra.first!)
        for _ in 0...palabra.count {
            palabra2 += "*"
        }
    }
    FraseFinal += palabra2 + " "
}
print (FraseSeparada)