frases=["hola soy hector"]

def primera_mayuscula(lista_frases):
    return lista_frases.title()

primera_letra_mayuscula=list(map(primera_mayuscula,frases))
print(primera_letra_mayuscula)