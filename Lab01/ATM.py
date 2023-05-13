# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:46:29 2023
@author: LAB02 
"""

import os

from dotenv import load_dotenv

load_dotenv()
PASSWORD = int(os.getenv("PASSWORD"))
RETIRO_MAX = 3000
DEPOSITO_MAX = 10000


class Cajero:
    def __init__(self):
        self.continuar = True
        self.monto = 5000
        self.menu()

    def contraseña(self):
        contador = 1
        while contador <= 3:
            contraseña = int(input("ingrese su contraseña:"))
            if contraseña == PASSWORD:
                print("Contraseña Correcta")
                return self.continuar
            else:
                print(f"Contraseña Incorrecta, le quedan {3 - contador} intentos")
                if contador == 3:
                    print("No puede realizar operaciones.")
                    self.continuar = False
                contador += 1

        return self.continuar
    


    def menu(self):
        message = ""
        os.system("cls")  # esto es solo para windows
        if self.contraseña():
            opcion = 0
            while opcion != "4":
                os.system("cls") 
                print(
                    """ Bienvenido al cajero automatico
                ******Menú******
                1- Depositar
                2- Retirar
                3- Ver saldo
                4- Salir """
                )
                opcion = input("Su opción es: ")

                actions = {
                    "1": self.depositar,
                    "2": self.retiro,
                    "3": self.ver,
                    "4": self.salir
                }

                if opcion in actions:
                    action = actions.get(opcion)
                    action()

                if opcion not in "1234":
                    print("Imposible realizar esa operación")
                
                if opcion == "4":
                    continue
                
                if opcion == "":
                    print("No existe esa opción")
                
                
                os.system ('pause')

                # if self.continuar:
                #     if opcion == "1":
                    #         self.depositar()
                #     elif opcion == "2":
                #         self.retiro()

                #     elif opcion == "3":
                #         self.ver()

                #     elif opcion == "4":
                #         print("Programa finalizado")

                #     else:
                #         print("NO existe esa opción")

                # else:
                #     if opcion in "123":
                #         print("Imposible realizar esa operación")

                #     elif opcion == "4":
                #         print("Programa finalizado")

                #     else:
                #         print("No existe esa opción")

    def salir(self):
        print("Programa finalizado")
    def depositar(self):
        dep = int(input("Ingrese su monto a depositar:"))
        if not self.depositoMaximo(dep):
            print("El deposito excede el límite maximo permitido.")
            return
        print("Usted a depositado", dep)
        print(f"Su nuevo saldo es {self.monto + dep}")  
        self.monto += dep
        
    def retiro(self):
        retirar = int(input("¿Cuánto desea retirar? : "))
        if not self.retiroMaximo(retirar):
            print("El retiro excede el límite maximo permitido.")
            return
        print("Su monto actual es", self.monto)
        if self.monto >= retirar:
            print(
                f"Usted a retirado: {retirar} , su nuevo monto es {self.monto - retirar}"
            )
            self.monto -= retirar
        else:
            print("Imposible realizar el retiro, su monto es menor")

    def ver(self):
        print("Su saldo es: ", self.monto)

    def retiroMaximo(self,retirar):
        return  retirar <= RETIRO_MAX;
    
    def depositoMaximo(self,deposito):
        return  deposito <= DEPOSITO_MAX;

app = Cajero()
