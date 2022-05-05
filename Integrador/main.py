from ManejadorCamas import ManejadorCamas
from ManejadorMedicamentos import ManejadorMedicamentos

if __name__=="__main__":
    manCamas=ManejadorCamas()
    manMed=ManejadorMedicamentos()
    manCamas.cargarCamas()
    manMed.cargarMedicamentos()
    nombre=input("Ingrese nombre a consultar: ")
    indice=manCamas.buscarPaciente(nombre)
    if indice != -1:
        manCamas.datos(indice)
    else:
        print("No se encontro el nombre")
    diagnostico=input("Ingrese diagnostico: ")
    pos=manCamas.buscarDiag(diagnostico)
    if pos != -1:
        print("Informacion del paciente con diagnostico: {}".format(diagnostico))
        manCamas.datos2(pos)
    else:
        print("No hay paciente con ese diagnostico")
