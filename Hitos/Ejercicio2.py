import random
#Muestra la opcion que eligira el usuario
def opciones():
    print("1-Piedra")
    print("2-Papel")
    print("3-Tijera")
#Creamos una funcion para relacionar 1 = piedra, 2 = papel y 3 = tijera
def eleccion(eleccion):
    if eleccion == 1:
        return "piedra"
    elif eleccion == 2:
        return "papel"
    elif eleccion == 3:
        return "tijera"
#Creamos otra funcion para que el usuario eliga una opcion del 1 al 3 y sino que le de error y vuelva a introducir la opcion
def opcion_usuario():
    while True:
        opciones()
        opcion=int(input("Elegir opcion (1,2,3): "))
        if opcion in [1,2,3]:
            return opcion
        else:
            print("Opcion incorrecta, porfavor eliga 1,2 o 3")
#Establecemos otra funcion para los posibles resultados que salgan. Compara las opciones y nos devuelve si el usuario ganó, perió o empató.
def ganador(opcion_usuario,maquina):
    match (opcion_usuario,maquina):
        case(1,3) | (2,1) | (3,2):
            return "Ganaste"
        case (3,1) | (1,2) | (2,3):
            return "Perdiste"
        case (1,1) | (2,2) | (3,3):
            return "empate"
#Empieza el juego        
def juego():
    #iniciamos los puntos del usuario y de la maquina en 0
    puntos_usuario=0
    puntos_maquina=0
#Creamos un bucle while para que mientras los puntos del usuario ni de la maquina sean 3 el juego siga adelante, y cuando el primer llegue a 3 puntos el juego termina
    while puntos_usuario < 3 and puntos_maquina < 3:
        obtener_opcion_usuario = opcion_usuario()
        obtener_opcion_maquina = random.randint(1, 3)
     
        print(f"Tu elegiste: {eleccion(obtener_opcion_usuario)}")
        print(f"La maquina ha elegido: {eleccion(obtener_opcion_maquina)}")
#Muestra el resultado de cada ronda para saber si hemos perdido o ganado
        resultado= ganador(obtener_opcion_usuario,obtener_opcion_maquina)
        print("El resultado es: ",resultado)
#Vamos actualizando los puntos a traves del match
        match resultado:
            case "Ganaste":
                puntos_usuario +=1
            case  "Perdiste":
                puntos_maquina +=1
        print("Tu puntuacion es:",puntos_usuario, "Puntuacion de la maquina es: ",puntos_maquina)
#Establece un mensaje de animo o de felicitacion   
    if puntos_usuario == 3:
        print("Felicidades, has ganado el juego")
    else:
        print("Lo siento, has perdido. Intentalo de nuevo")
#Se ejecuta el juego
juego()