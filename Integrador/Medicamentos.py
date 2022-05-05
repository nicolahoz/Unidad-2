
class Medicamentos:
    __idCama:0
    __idMedicamento:0
    __nombreComercial:''
    __monodroga:''
    __presentacion:''
    __cantidadAplicada:''
    __precioTotal:0

    def __init__(self,idC,idM,nomC,monoD,pres,cantA,precio):
        self.__idCama=idC
        self.__idMedicamento=idM
        self.__nombreComercial=nomC
        self.__monodroga=monoD
        self.__presentacion=pres
        self.__cantidadAplicada=cantA
        self.__precioTotal=precio

    def getidCama(self):
        return self.__idCama

    def getidMed(self):
        return self.__idMedicamento

    def getnombreC(self):
        return self.__nombreComercial

    def getMonod(self):
        return self.__monodroga

    def getPres(self):
        return self.__presentacion

    def getCantidad(self):
        return self.__cantidadAplicada

    def getPrecio(self):
        return self.__precioTotal
    


