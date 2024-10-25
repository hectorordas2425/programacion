import random
#Creamos una funcion para buscar el menu
def opciones():
    print("1-piedra")
    print("2-papel")
    print("3-tijera")
    
#Creamos una funcion para relacionar 1 = piedra, 2 = papel y 3 = tijera
def eleccion(eleccion):
    match eleccion:
        case 1: 
            return "piedra"
        case 2:
            return "papel"
        case 3:
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
    
def casosPiedra(eleccionJugador, eleccionMaquina):
    if eleccionJugador == 1 and eleccionMaquina == 3:
        return "ganaste"
    elif eleccionJugador == 1 and eleccionMaquina == 2:
        return "perdiste"
    else:
        return "empate"
    
def casosPapel(eleccionJugador, eleccionMaquina):
    if eleccionJugador == 2 and eleccionMaquina == 1:
        return "ganaste"
    elif eleccionJugador == 2 and eleccionMaquina == 3:
        return "perdiste"
    else:
        return "empate"

def casosTijera(eleccionJugador, eleccionMaquina):
    if eleccionJugador == 3 and eleccionMaquina == 2:
        return "ganaste"
    elif eleccionJugador == 3 and eleccionMaquina == 1:
        return "perdiste"
    else:
        return "empate"        
    
def juego():
#iniciamos los puntos del usuario y de la maquina en 0
    puntos_usuario=0
    puntos_maquina=0

#Creamos un bucle while para que mientras los puntos del usuario ni de la maquina sean 3 el juego siga adelante, y cuando el primer llegue a 3 puntos el juego termina
    while puntos_usuario < 3 and puntos_maquina < 3: # puntos_maquina == 3 or puntos_usuario == 3 
        obtener_opcion_usuario = opcion_usuario()
        obtener_opcion_maquina = random.randint(1, 3)
        
        print("Tu elegiste: ", eleccion(obtener_opcion_usuario))
        print("La maquina ha elegido: ", eleccion(obtener_opcion_maquina))
        
 #Muestra el resultado de cada ronda para saber si hemos perdido o ganado
       
        match obtener_opcion_usuario:
            case 1:
                resultado = casosPiedra(obtener_opcion_usuario, obtener_opcion_maquina)
            case 2:
                resultado = casosPapel(obtener_opcion_usuario, obtener_opcion_maquina)
            case 3:
                resultado = casosTijera(obtener_opcion_usuario, obtener_opcion_maquina)
                
        print("El resultado es: ",resultado)#Para mostrar si hemos ganado o perdido
        match resultado:
            case "ganaste":
                puntos_usuario +=1
            case "perdiste":
                puntos_maquina +=1
            case "empate":
                puntos_usuario=0
        print("Tu puntuacion es:",puntos_usuario, "Puntuacion de la maquina es:",puntos_maquina)
#Establece un mensaje de animo o de felicitacion
    if puntos_usuario == 3:
            print("Felicidades, has ganado el juego")
    else:
            print("Lo siento, has perdido. Intentalo de nuevo")

#Se ejecuta el juego
juego()