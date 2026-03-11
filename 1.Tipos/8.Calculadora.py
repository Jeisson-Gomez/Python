n1 = input("Ingresa Primer Numero:")
n2 = input("Ingresa Segundo Numero:")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

Mensaje = f"""
Para los numeros {n1} y {n2},
El resultado de la suma es: {suma}.
El resultado de la resta es: {resta}.
El resultado de la multiplicacion es: {multi}.
El resultado de la división es: {div}.
"""

print(Mensaje)