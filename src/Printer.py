def imprimir_resultados(monedas, sophia, mateo):
    print(f"{monedas}\n")
    suma_sophia, suma_mateo = sum(sophia), sum(mateo)
    print("Elecciones hechas por cada uno\n")
    print(f"Sofia: {sophia}\n")
    print(f"Mateo: {mateo}\n")
    print(f"Sofia: {sum(sophia)}\nMateo: {sum(mateo)}\n")
    if(suma_sophia > suma_mateo):
        print("Gana Sofia\n")
    else:
        print("Gana Mateo\n")
    return 