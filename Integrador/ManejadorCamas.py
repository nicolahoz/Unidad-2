from Camas import Camas
import csv
import numpy as np

class ManejadorCamas:
    __array=None

    def cargarCamas(self):
        archivo = open('camas.csv')
        reader=csv.reader(archivo, delimiter=';')
        bandera=True
        ArrayX = np.array([Camas]*30)
        for linea in reader:
            if bandera:
                bandera=not bandera
            else:
                indice=int(linea[0])
                hab=int(linea[1])
                estado=bool(linea[2])
                nya=str(linea[3])
                diag=str(linea[4])
                fI=str(linea[5])
                fA=str(linea[6])
                objeto=Camas(hab,estado,nya,diag,fI,fA)
                ArrayX[(indice-1)]=objeto
        self.__array=ArrayX


    def buscarPaciente(self,nombre):
        i=0
        while i<30 and self.__array[i].getNya() != nombre:
            i+=1
        if i==30:
            pos=-1
        else:
            pos=i
        return pos


    def buscarDiag(self,diag):
        i=0
        while i<30 and self.__array[i].getDiag() != diag:
            i+=1
        if i==30:
            pos=-1
        else:
            pos=i
        return pos

    def datos(self,indice):
        self.__array[indice].devolverDatos(indice)

    def datos2(self,pos):
        self.__array[pos].devolverDatos2(pos)

