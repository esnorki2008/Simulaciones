from Elementos import Entidad
import random
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
    


    def Expandir(self,ListaPlanta,Limites):
        
        if self.Vida>5 :
            NuevaPlanta=Planta(2,Limites)           
            X=int(random.randrange(2))
            Y=int(random.randrange(2))
            NuevaPlanta.PosActual=(self.PosActual[0]+X,self.PosActual[1]+Y)
            if NuevaPlanta.PosActual[0]>0 and NuevaPlanta.PosActual[0]<Limites[0] :                
                ListaPlanta.append(NuevaPlanta)

            self.Vida=int(random.randrange(1))
        else:
            self.Vida+=1
   
    def Color(self):
       return (24,118,20)

    def Acciones(self):
       pass