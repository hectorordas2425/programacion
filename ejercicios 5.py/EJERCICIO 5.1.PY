numeros=[1,2,3,4,5]

def suma_5(lista_numeros):
   return lista_numeros + 5

numero_mas_5=list(map(suma_5,numeros))
print(numero_mas_5)