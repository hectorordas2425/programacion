#Pedimos al usuario atraves de un while que ingrese su saldo y que le de error si su saldo es negativo para que le vuelva a preguntar
while True:
    saldo=float(input("ingresar saldo de su cuenta: "))
    if saldo < 0:
        print("Error, el saldo no puede ser negativo")
    else:
        break
#Iniciamos el numero de ingresos y de retiros en 0
ingresos=0
retiros=0
#Creamos otro bucle while donde creamos una funcion para que nos muestre el menu
while True:
    def menu():
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo")
        print("4. Estadísticas")
        print("5. Salir")
#Pedimos al usuario que eliga una opcion, y que si esta entre el 1 y el 5 se salga del buchle while
    while True:
        opcion=int(input("Seleccionar una opcion: "))   
        if 1 <= opcion <=5:
            break
        else:
            print("Error, introduzca una opción válida")

#Si el usuario elige la opcion 1, le pedirá la cantidad que quiere ingresar y le mostrara el saldo final que tenga
    if opcion == 1:
        while True:
            cantidad=float(input("Ingresar cantidad de dinero: "))
            if cantidad < 0:
                print("No se pueden añadir cantidades negativas")
            else:
                saldo +=cantidad
                ingresos += 1
                print(f"Has ingresadoo: {cantidad}. Saldo actual: {saldo}")
            break
#Si el usuario elige la opcion 2, le pedirá la cantidad que desea retirar de su saldo. 
#La cantidad que desea retirar no puede ser mayor que el saldo que tenga, sino le dará error. 
#La canntidad que introduzca se restará a su saldo
    elif opcion == 2:
        while True:
            cantidad=float(input("Ingresar cantidad de dinero: "))
            if cantidad < 0:
                print("No se pueden añadir cantidades negativas")
            elif cantidad > saldo:
                print("No se puede retirar una cantidad mayor a la que tienes")
            else:
                saldo -=cantidad
                retiros += 1
                print(f"Has retirado: {cantidad}. Saldo actual: {saldo}")
                break
#Si el usuario elige la opcion 3, le mostrará el saldo actual que tenga
    elif opcion == 3:
        print("Tu saldo actual es: ",saldo)
#Si el usuario elige a opcion 4, le mostrará los ingresos y retiros totales realizados 
    elif opcion == 4:
        print(" Los ingresos realizados son: ", ingresos, "Los retiros realizados son: ",retiros)      
#Si el usuario elige la opcion 5, se saldra del prgrama
    elif opcion == 5:
        print("Saliendo del programa") 
        break