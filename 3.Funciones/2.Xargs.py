def Suma(*Numeros):
    Resultado = 0
    for Numero in Numeros:
        Resultado += Numero
    print(Resultado)

Suma(2, 5, 3)
Suma(2, 5, 3, 4)
Suma(2, 8, 7, 45, 32)