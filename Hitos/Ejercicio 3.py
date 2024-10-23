
while True:
    saldo=float(input("ingresar saldo de su cuenta: "))
    if saldo < 0:
        print("Error, el saldo no puede ser negativo")
    else:
        break

ingresos=0
retiros=0

while True:
    def menu():
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo")
        print("4. Estadísticas")
        print("5. Salir")
    while True:
        opcion=int(input("Seleccionar una opcion: "))   
        if 1 <= opcion <=5:
            break
        else:
            print("Error, introduzca una opción válida")


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

    elif opcion == 3:
        print("Tu saldo actual es: ",saldo)
   
    elif opcion == 4:
        print(" Los ingresos realizados son: ", ingresos, "Los retiros realizados son: ",retiros)      
    elif opcion == 5:
        print("Saliendo del programa") 
        break