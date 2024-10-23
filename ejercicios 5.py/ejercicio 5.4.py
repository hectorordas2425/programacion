numeros=[1.3, 2.4, 3.6]

def redondear_numero(numero):
    return round(numero)

redondeo=list(map(redondear_numero,numeros))
print(redondeo)