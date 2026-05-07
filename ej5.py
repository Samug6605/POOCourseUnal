from enum import Enum


class TipoCuenta(Enum):
    """Tipos de cuenta bancaria disponibles."""
    AHORROS = 1
    CORRIENTE = 2


class CuentaBancaria:
    """Modelo de una cuenta bancaria con operaciones básicas de depósito y retiro."""

    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        """Inicializa la cuenta con saldo cero."""
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self):
        """Muestra en pantalla todos los atributos de la cuenta."""
        print("\n----- DATOS DE LA CUENTA -----")
        print("Nombres del titular  =", self.nombres_titular)
        print("Apellidos del titular =", self.apellidos_titular)
        print("Número de cuenta     =", self.numero_cuenta)
        print("Tipo de cuenta       =", self.tipo_cuenta.name)
        print("Saldo                =", self.saldo)

    def consultar_saldo(self):
        """Muestra el saldo actual de la cuenta."""
        print("El saldo actual es =", self.saldo)

    def consignar(self, valor):
        """Deposita un valor positivo en la cuenta y actualiza el saldo."""
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor} en la cuenta.")
            print("El nuevo saldo es $", self.saldo)
        else:
            print("El valor a consignar debe ser mayor que cero.")

    def retirar(self, valor):
        """Retira un valor de la cuenta si no supera el saldo disponible."""
        if valor <= 0:
            print("El valor a retirar debe ser mayor que cero.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        else:
            self.saldo -= valor
            print(f"Se ha retirado ${valor} de la cuenta.")
            print("El nuevo saldo es $", self.saldo)


nombres = input("Ingrese nombres del titular: ")
apellidos = input("Ingrese apellidos del titular: ")
numero = int(input("Ingrese número de cuenta: "))

print("Seleccione tipo de cuenta:\n1. AHORROS\n2. CORRIENTE")
tipo = TipoCuenta.AHORROS if int(input()) == 1 else TipoCuenta.CORRIENTE

cuenta = CuentaBancaria(nombres, apellidos, numero, tipo)
cuenta.imprimir()

cuenta.consignar(float(input("\nIngrese valor a consignar: ")))
cuenta.retirar(float(input("Ingrese valor a retirar: ")))
cuenta.consultar_saldo()
