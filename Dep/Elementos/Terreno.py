from Elementos import Entidad
class Terreno(Entidad.Entidad):
    def __init__(self,Vida,Limites):
        self.Vida =Vida
        self.Tipo="Terreno"
        self.Limites=Limites

    def EstaVivo(self):
        if self.Vida>0 :
            return True
        else:
            return False

    def DevolverTipo(self):
        return 0

    def BuscarAlimento(self):
       pass 