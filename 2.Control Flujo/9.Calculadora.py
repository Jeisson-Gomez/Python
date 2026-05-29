print("Bienvenido a la calculadora")
print("Para salir, escriba 'salir'")
print("Las operaciones disponibles: suma, resta, multi, div")

Resultado = ""
while True:
    if not Resultado:
        Resultado = input("Ingrese el número: ")
        if Resultado.lower() == "salir":
            break
        Resultado = int(Resultado)

    op=input("Ingrese la operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese el segundo número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        Resultado += n2
    elif op == "resta":
        Resultado -= n2
    elif op.lower() == "multi":
        Resultado *= n2
    elif op.lower() == "div":
        Resultado /= n2
    
    else:
            print("Error: Operacion No valida.")
            break
    print(f"El reusltado es {Resultado}")