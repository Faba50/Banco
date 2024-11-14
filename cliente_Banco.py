class Cliente:
    def __init__(self, nombre, cash=0):
        self.nombre = nombre
        self.cash = cash

    def depositar(self):
        monto_deposito = int(input("Ingrese la cantidad que desea depositar: "))
        self.cash += monto_deposito
        print(f"Se ha depositado {monto_deposito} pesos. Nuevo saldo: {self.cash}")

    def __str__(self):
        return f"Cliente: {self.nombre}. Saldo actual: {self.cash} pesos."


class ILBA:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def calcular_total_depositado(self):
        total_depositado = sum(cliente.cash for cliente in self.clientes)
        return total_depositado

    def __str__(self):
        return f"Banco ILBA con {len(self.clientes)} clientes."


# Crear la instancia del banco
Banco = ILBA()

# Crear clientes
cliente1 = Cliente("Brad Pitt", 173156)
cliente2 = Cliente("Maria Elena Walsh", 23419)
cliente3 = Cliente("Pedro Pedro Pe", 77777)

# Agregar clientes al banco
Banco.agregar_cliente(cliente1)
Banco.agregar_cliente(cliente2)
Banco.agregar_cliente(cliente3)



