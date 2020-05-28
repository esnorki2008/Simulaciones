from Elementos import Terreno
class Planta(Terreno.Terreno):
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