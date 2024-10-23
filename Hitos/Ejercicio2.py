#Muestra la opcion que eligira el usuario
def opciones():
    print("1-Piedra")
    print("2-Papel")
    print("3-Tijera")

Def piedra()
Def papel()
Def tijera()








opcion=0
while opcion != 1 and opcion != 2 and opcion != 3:
    opciones()
    opcion= int(input("ingresar una opcion: ")) #Solicitamos al usuario que eliga una opción.
    
    match opcion:
        case 1:  #si introduce la opcion 1 (piedra)
            piedra()
        case 2:  #Si introduce la opcion 2 (papel)
            papel()
        case 3:  #Si introduce la opcion 3 (stijera) 
            tijera()
        case _:  #Si no introduce ninguna de las otras opciones
            print("opcion incorrecta")































while opcion != 1 and opcion !=2 and opcion != 3:
    opcion_usuario()
    opcion=int(input("Introduzca una opción"))
    match opcion:
        case 1:
            print("Piedra")# Si introduce la opcion 1 (piedra)
        case 2:
            print("Papel")# Si introduce la opcion 2 (papel)
        case 3:
            print("Tijera")# Si introduce la opcion 3 (tijera)
        case _:
            print("Opcion incorrecta")# Si no es ninguna de las otras opciones








