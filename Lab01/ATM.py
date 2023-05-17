# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:46:29 2023
@author: LAB02 
"""

import os
import jwt

from dotenv import load_dotenv

load_dotenv()
PASSWORD = str(os.getenv("PASSWORD"))
RETIRO_MAX = 3000
DEPOSITO_MAX = 10000
SECRET_KEY = '7134743777217A25432A462D4A614E645267556B586E3272357538782F413F44'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub21icmUiOiJKb3NlIENhbm8iLCJzYWxkbyI6NTAwMH0.QfaNEvwxvq2wpRwymy4IHOWz-vBZGm7VXrS2k6cwBZQ'

class Cajero:
    def __init__(self):
        self.continuar = True
        self.monto = 5000
        

    def contraseña(self):
        intentos = 3
        while intentos > 0:
            contraseña = self.solicitar_contraseña()
            if self.validar_contraseña(contraseña):
                print("Contraseña Correcta")
                return self.continuar
            else:
                intentos -= 1
                print(f"Contraseña Incorrecta, le quedan {intentos} intentos")
                if intentos == 0:
                    print("No puede realizar operaciones.")
                    self.continuar = False

        return self.continuar
    


    def menu(self):
        os.system("cls")  # esto es solo para windows
        self.asd()
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

    
    def depositar(self):
        deposito = int(input("Ingrese su monto a depositar:"))
        if not self.deposito_minimo(deposito):
            print("El deposito minimo no puede ser menor a 1$.")
            return 
        if not self.deposito_maximo(deposito):
            print("El deposito excede el límite maximo permitido.")
            return
        print("Usted a depositado", deposito)
        print(f"Su nuevo saldo es {self.realizar_deposito(deposito)}")  
    
    def realizar_deposito(self, deposito):
        self.monto += deposito
        return self.monto
    
    def retiro(self):
        retirar = int(input("¿Cuánto desea retirar? : "))        
        if not self.retiro_minimo(retirar):
            print("El retiro no puede ser una cantidad menor o igual a 0.")
            return
        if not self.retiro_maximo(retirar):
            print("El retiro excede el límite maximo permitido.")
            return
        print("Su monto actual es", self.monto)
        if self.validar_retiro(retirar):
            print( f"Usted a retirado: {retirar} , su nuevo monto es {self.realizar_retiro(retirar)}" )
        else:
            print("Imposible realizar el retiro, su monto es menor")
    
    def retiro_minimo(self,retirar):
        return retirar > 0

    def validar_retiro(self,retirar):
        return self.monto >= retirar
    
    def realizar_retiro(self, retirar):
        self.monto -= retirar
        return self.monto
    
    def ver(self):
        print(f"Su saldo es: {self.obtener_saldo()}")
    
    def obtener_saldo(self):
        return self.monto

    def salir(self):
        print("Programa finalizado")

    def retiro_maximo(self,retirar):
        return  retirar <= RETIRO_MAX
    
    def deposito_minimo(self,deposito):
        return deposito > 1

    def deposito_maximo(self,deposito):
        return  deposito <= DEPOSITO_MAX
    
    def solicitar_contraseña(self):
        contraseña = input("Ingrese su contraseña: ")
        return contraseña
    
    def validar_contraseña(self, contraseña):
        
        if len(contraseña) <= 4 and contraseña.isdigit() and int(contraseña) >= 0:
            return contraseña == PASSWORD
        
        return False
    


    def validar_token(self,token):
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return decoded_token
        except:
            return None
    
    def asd(self):
        decoded_token = self.validar_token(TOKEN)
        if decoded_token:
            print("Token válido. Datos del usuario:")
            print(decoded_token)
        else:
            print("Token inválido")