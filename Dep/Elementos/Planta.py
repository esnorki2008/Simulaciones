from Elementos import Entidad
class Planta(Entidad.Entidad):
    def __init__(self,Vida,Limites):
        self.Vida =Vida
        self.Tipo="Planta"
        self.Limites=Limites

    def EstaVivo(self):
        if self.Vida>0 :
            return True
        else:
            return False

    def DevolverTipo(self):
        return 1

    def BuscarAlimento(self):
       pass 

    def Mover(self):
        pass

    def Expandir(self,ListaPlanta):
       print(ListaPlanta)
   
    def Color(self):
       return (24,118,20)

    def Acciones(self):
       pass