from __future__ import annotations


class ViajeroFrecuente:
    __num_viajero:int = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum: int =0

    def __init__(self, num_viajero:int, dni, nombre, apellido, millas_acum:int):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def getnumero(self):
        return self.__num_viajero

    def muestra(self):
        return f'Numero: {self.__num_viajero} DNI:{self.__dni}  -{self.__nombre} {self.__apellido}- Millas: {self.__millas_acum}'

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def acumularMillas(self, cantrecorrida):
        self.__millas_acum += cantrecorrida
        return self.__millas_acum

    def canjerarMillas(self, millascanje):
        if millascanje <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - millascanje
            print('Millas canjeadas'.center(30, '-'))
            return self.__millas_acum
        else:
            print('Error de Operacion'.center(30, '-'))
            return self.__millas_acum

    def __gt_(self, otro):
        return self.__millas_acum > otro

    def __add__(self, otro):
        self.__millas_acum = self.__millas_acum + otro
        return self

    def __sub__(self, otro):
        self.__millas_acum = self.__millas_acum - otro
        return self

    def __eq__(self,otro: ViajeroFrecuente|object|int):
        return self.__millas_acum == otro

    def __req__(self,otro):
        return otro == self.__millas_acum

    def __radd__(self, otro):
        self.__millas_acum = otro + self.__millas_acum
        return self

    def __rsub__(self, otro):
        self.__millas_acum = self.__millas_acum - otro
        return self
