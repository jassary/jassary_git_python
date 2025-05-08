#4. Diseña una clase 'CuentaBancaria' con métodos para depositar, retirar y mostrar el saldo.

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado ${monto}.")
        else:
            print("El monto a depositar debe ser mayor que 0.")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes.")
        elif monto <= 0:
            print("El monto a retirar debe ser mayor que 0.")
        else:
            self.saldo -= monto
            print(f"Has retirado ${monto}.")

    def mostrar_saldo(self):
        print(f"Saldo actual: ${self.saldo}")

# Ejemplo de uso
cuenta = CuentaBancaria()

cuenta.depositar(100)
cuenta.retirar(30)
cuenta.mostrar_saldo()



