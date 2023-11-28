# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:25:28 2023

@author: dfern
"""

class Ruta:
    def __init__(self, origen, destino, costo_base):
        self.origen = origen
        self.destino = destino
        self.costo_base = costo_base

class Autobus:
    def __init__(self, tipo, ponderacion):
        self.tipo = tipo
        self.ponderacion = ponderacion

class Viaje:
    def __init__(self, origen, destino, autobus, boletos):
        self.origen = origen
        self.destino = destino
        self.autobus = autobus
        self.boletos = boletos

    def cotizar(self):
        cotizacion = Cotizacion(self.origen, self.destino, self.autobus, self.boletos)
        cotizacion.mostrar_resultados()

class Cotizacion:
    def __init__(self, origen, destino, autobus, boletos):
        self.ruta = Ruta(origen, destino, self.obtener_costo_base(origen, destino))
        self.autobus = autobus
        self.boletos = boletos

    def obtener_costo_base(self, origen, destino):
        costos_base = {
            ('Mex', 'Mex'): 0.0,
            ('Mex', 'Cva'): 300.0,
            ('Mex', 'Igu'): 400.0,
            ('Mex', 'Aca'): 783.0,
            ('Cva', 'Mex'): 300.0,
            ('Cva', 'Cva'): 0.0,
            ('Cva', 'Igu'): 200.0,
            ('Cva', 'Aca'): 583.0,
            ('Aca', 'Mex'): 783.0,
            ('Aca', 'Cva'): 583.0,
            ('Aca', 'Igu'): 323.0,
            ('Aca', 'Aca'): 0.0,
        }
        return costos_base.get((origen, destino), 0.0)

    def calcular_subtotal(self):
        return self.ruta.costo_base * self.autobus.ponderacion * self.boletos

    def calcular_iva(self):
        return self.calcular_subtotal() * 0.16

    def calcular_total(self):
        return self.calcular_subtotal() + self.calcular_iva()

    def mostrar_resultados(self):
        print("Cotización:")
        print(f"Ruta: {self.ruta.origen}-{self.ruta.destino}")
        print(f"Autobús: {self.autobus.tipo}")
        print(f"Boletos: {self.boletos}")
        print(f"Costo Base: ${self.ruta.costo_base}")
        print(f"Ponderación Autobús: {self.autobus.ponderacion}")
        print(f"Subtotal: ${self.calcular_subtotal():,.2f}")
        print(f"Iva (16%): ${self.calcular_iva():,.2f}")
        print(f"Total: ${self.calcular_total():,.2f}")

# Solicitar información al usuario
print("Bienvenido al sistema de cotización de viajes TinyToons.")
origen = input("Ingrese el origen del viaje (Mex, Cva, Aca): ").capitalize()
destino = input("Ingrese el destino del viaje (Mex, Cva, Igu, Aca): ").capitalize()
tipo_autobus = input("Ingrese el tipo de autobús (Platino, Turístico, Básico): ").capitalize()
boletos = int(input("Ingrese la cantidad de boletos: "))

# Crear objetos para Autobus y Viaje
autobus = Autobus(tipo=tipo_autobus, ponderacion=2.0 if tipo_autobus == "Platino" else 1.5 if tipo_autobus == "Turístico" else 1.0)
viaje = Viaje(origen=origen, destino=destino, autobus=autobus, boletos=boletos)

# Obtener la cotización y mostrar resultados
viaje.cotizar()

