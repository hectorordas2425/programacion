numeros=[1,2,3,4,5,]


def sumar_el_doble(numero):
    return numero * 2

numero_doble=list(map(sumar_el_doble, numeros))
print(numero_doble)