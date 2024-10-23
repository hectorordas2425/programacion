def menu(): #muestra las opciones del menú al usuario.
    print("1-cuadrado")
    print("2-rectángulo")
    print("3-salir")
    
#Creamos una funcion cuadrado para realizar las operaciones de area, perimetro y para mostrar la figura. 
def cuadrado():
    lado=int(input("ingresar lado del cuadrado"))
    if lado > 0:
        area= lado * lado
        perimetro= lado * 4
        print("el area del cuadrado es: ",area)
        print("el perimetro del cuadrado es: ",perimetro)
        for _ in range(lado):
            print('*'* lado)
    else:
        print("error")
        
#Creamos una funcion rectangulo para realizar las operaciones de area, perimetro y para mostrar la figura.         
def rectangulo():
    base=int(input("ingresar lado del rectangulo"))
    altura=int(input("ingresar altura del rectangulo"))
    if base and altura > 0:
        area= base * altura
        perimetro= base * 2 + altura * 2
        print("el area del rectangulo es: ",area)
        print("el perimetro del rectangulo es: ",perimetro)
        for _ in range(altura):
            print('*''*'* base)
    else:
        print("error")  
#Creamos una funcion salir para salir del programa.       
def salir():
    if opcion == 3:
        print("Saliendo del programa")
        
        
    
opcion=0
#Utilizamos el bucle while para que si el usuario introduce un numero distinto de 1,2,3 vuelva a introducir el numero.
while True:
    menu()
    opcion= int(input("ingresar una opcion: ")) #Solicitamos al usuario que eliga una opción.
    
    match opcion:
        case 1:  #si introduce la opcion 1 (cuadrado)
            cuadrado()
        case 2:  #Si introduce la opcion 2 (rectángulo)
            rectangulo()
        case 3:  #Si introduce la opcion 3 (salir) 
            salir()
            break
        case _:  #Si no introduce ninguna de las otras opciones
            print("opcion incorrecta")