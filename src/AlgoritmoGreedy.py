
def buscar_mayor_valor(lista):
    i = 0
    if (lista[0] < lista[-1]):
        i = -1
    return i

def buscar_menor_valor(lista):
    i = 0
    if (lista[0] > lista[-1]):
        i = -1
    return i


def eleccion_monedas(lista, lista_sophia, lista_mateo):

    tamanio = len(lista)
    turno = 0
    puntuacion_sofia, puntuacion_mateo = 0, 0

    while tamanio > 0:
        i = 0
        if(turno % 2 == 0):
            i = buscar_mayor_valor(lista)
            if i == 0:
                moneda = lista.popleft()
                puntuacion_sofia += moneda
                lista_sophia.append(moneda)
            else:
                moneda = lista.pop()
                puntuacion_sofia += moneda
                lista_sophia.append(moneda)
        else:
            i = buscar_menor_valor(lista)
            if i == 0:
                moneda = lista.popleft()
                puntuacion_mateo += moneda
                lista_mateo.append(moneda)
            else:
                moneda = lista.pop()
                puntuacion_mateo += moneda
                lista_mateo.append(moneda)
        tamanio -= 1
        turno += 1

    return int((puntuacion_sofia >= puntuacion_mateo))