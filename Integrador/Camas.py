from ManejadorMedicamentos import ManejadorMedicamentos

class Camas:
    __habitacion:0
    __estado:None
    __nya:''
    __diag:''
    __fechaInt:''
    __fechaAlta:''

    def __init__(self,hab,estado,nya=None,diag=None,fI=None,fA=None):
        self.__habitacion=hab
        self.__estado=estado
        self.__nya=nya
        self.__diag=diag
        self.__fechaInt=fI
        self.__fechaAlta=fA

    def getNya(self):
        return self.__nya

    def getDiag(self):
        return self.__diag

    def devolverDatos(self,indice):
        print("Paciente: {} -- Cama: {} -- Habitacion: {}".format(self.__nya,indice+1,self.__habitacion))
        print("Diagnostico: {} -- Fecha de internacion: {}".format(self.__diag, self.__fechaInt))
        print("Fecha de Alta: {}".format(self.__fechaAlta))
        print("Medicamento/monodroga -- Presentacion -- Cantidad -- Precio")
        manMedic=ManejadorMedicamentos()
        manMedic.datosMed(indice)

    def devolverDatos2(self,pos):
        print("Paciente: {} -- Cama: {} -- Habitacion: {}".format(self.__nya,pos+1,self.__habitacion))
        print("Fecha de internacion: {}".format(self.__fechaInt))










