import csv
from Medicamentos import Medicamentos

class ManejadorMedicamentos:
    __lista = []

    def cargarMedicamentos(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idC = int(fila[0])
                idM = int(fila[1])
                nomC = str(fila[2])
                mono = str(fila[3])
                pres = str(fila[4])
                cant = int(fila[5])
                prec = float(fila[6])
                med = Medicamentos(idC, idM, nomC, mono, pres, cant, prec)
                self.__lista.append(med)


    def datosMed(self,idCama):
        total=0
        for i in range(len(self.__lista)):
            if (idCama+1) == self.__lista[i].getidCama():
                print("{}/{}     --     {}     --     {}     --     ${}".format(self.__lista[i].getidMed(), self.__lista[i].getMonod(), self.__lista[i].getPres(), self.__lista[i].getCantidad(), self.__lista[i].getPrecio()))
                total+=self.__lista[i].getPrecio()
        print("Total adeudado:                                            ${}".format(total))




