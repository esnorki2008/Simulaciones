from Elementos import Entidad
class Depredador(Entidad.Entidad):
    def __init__(self,Vida,Limites):
        self.Vida =Vida
        self.Tipo="Depredador"
        self.Limites=Limites
    def EstaVivo(self):
        if self.Vida>0 :
            return True
        else:
            return False
    def DevolverTipo(self):
        return 3
    
    def BuscarAlimento(self):
       pass 

    def Mover(self):
       pass 