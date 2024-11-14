from cliente_banco import Banco, Cliente  # Importamos la instancia Banco y la clase Cliente

def realizar_deposito():
    nombre_cliente = input("Ingrese el nombre del cliente que desea depositar dinero: ")
    nombre_cliente = nombre_cliente.capitalize()
    for cliente in Banco.clientes:
        if cliente.nombre == nombre_cliente:
            cliente.depositar()
            return
    print("Cliente no encontrado.")

def calcular_total():
    total_depositado = Banco.calcular_total_depositado()
    print(f"Total de dinero depositado en el Banco ILBA: {total_depositado} pesos.")

def menu():
    while True:
        print("\nMenú de Operaciones Banco ILBA:")
        print("1. Realizar depósito")
        print("2. Calcular monto depositado en el banco")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            realizar_deposito()

        elif opcion == "2":
            calcular_total()

        elif opcion == "3":
            print("Gracias por utilizar los servicios del Banco ILBA. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 3.")

# Ejecutar el menú
menu()
