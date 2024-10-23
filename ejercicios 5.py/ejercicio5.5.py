palabras=["hola","adios","balon","futbol"]

def contar_palabra(palabra):
    return len(palabra)

contar_palabras=list(map(contar_palabra,palabras))
print(contar_palabras)