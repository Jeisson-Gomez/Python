Buscar = 10

for Numero in range(5):
    print(Numero)

    if Numero == Buscar:
        print("Encontrado", Buscar)
        break

else:
    print("No encontre el numero buscado :(")