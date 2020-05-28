from Elementos import Entidad
class Presa(Entidad.Entidad):
    def __init__(self,Vida,Limites):
        self.Vida =Vida
        self.Tipo="Presa"
        self.Limites=Limites
    def EstaVivo(self):
        if self.Vida>0 :
            return True
        else:
            return False

    def DevolverTipo(self):
        return 2

    def BuscarAlimento(self):
       pass 

    def Mover(self):

        X=self.PosActual[0]
        Y=self.PosActual[1]

        if self.PosActual[0]>0 and self.PosActual[0]<self.Limites[0]:
            X+=1
        else:
            X-=1

        if self.PosActual[1]>0 and self.PosActual[1]<self.Limites[1]:
            Y+=1
        else:
            Y-=1
        

        self.PosActual=(X,Y)