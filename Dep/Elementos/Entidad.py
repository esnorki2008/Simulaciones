from abc import ABC, abstractmethod

class Entidad(ABC):
   Vida=0
   Tipo=None
   PosActual=0,0
   Limites=0,0
   @abstractmethod
   def __init__(self,Vida,Limites):
        pass
        
   @abstractmethod
   def Mover(self):
       pass      
   @abstractmethod
   def EstaVivo(self):
       pass 

   @abstractmethod
   def BuscarAlimento(self):
       pass 
  
   @abstractmethod
   def DevolverTipo(self):
       pass 

   def Ruido(self):
        print("Soy De Tipo " +str(self.Tipo))
   
   def VidaActual(self):
        print("Vida " +str(self.Vida))

   @abstractmethod
   def Expandir(self,*args):
       pass
   
   @abstractmethod
   def Color(self):
       pass

   @abstractmethod
   def Acciones(self):
       pass