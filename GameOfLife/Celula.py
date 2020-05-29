class Celula:
    Viva=False
    Turno=False
    PosActual=(0,0)
    def __init__(self,PosActual):
        self.PosActual=PosActual

    def Interactuar(self,Lista,Limite):
        if (not self.Turno) and True :
            return

        Vecinos=0
        Vecinos+=self.Izquierda(self.PosActual,Lista,Limite)
        Vecinos+=self.Derecha(self.PosActual,Lista,Limite)
        Vecinos+=self.Arriba(self.PosActual,Lista,Limite)
        Vecinos+=self.Abajo(self.PosActual,Lista,Limite)

        Vecinos+=self.IzquierdaArriba(self.PosActual,Lista,Limite)
        Vecinos+=self.DerechaAbajo(self.PosActual,Lista,Limite)
        Vecinos+=self.IzquierdaArriba(self.PosActual,Lista,Limite)
        Vecinos+=self.IzquierdaAbajo(self.PosActual,Lista,Limite)

        if Vecinos == 3:
            Viva= True
        elif Vecinos ==2 and (not Viva) :
            Viva=True
        if Vecinos > 3 or Vecinos < 2:
            Viva=False
        
        self.Turno =False


    def LLamarVecina(self,PosVecina,Lista,Limite):
            if not self.Viva :
                return 0
            Obj = Lista.get(PosVecina)            
            Obj.Interactuar(Lista,Limite)
            if Obj.Viva :
                return 1
            else :
                return 0


    def Izquierda(self,PosActual,Lista,Limite):
        if self.PosActual[0]>1:      
            return self.LLamarVecina((self.PosActual[0]-1,self.PosActual[1]),Lista,Limite)
        else:
            return 0

    def Derecha(self,PosActual,Lista,Limite):
        if self.PosActual[0]<Limite[0]:      
            return self.LLamarVecina((self.PosActual[0]+1,self.PosActual[1]),Lista,Limite)
        else:
            return 0

    def Arriba(self,PosActual,Lista,Limite):
        if self.PosActual[1]<Limite[1]:      
            return self.LLamarVecina((self.PosActual[0],self.PosActual[1]+1),Lista,Limite)
        else:
            return 0

    def Abajo(self,PosActual,Lista,Limite):
        if self.PosActual[1]>1:      
            return self.LLamarVecina((self.PosActual[0],self.PosActual[1]-1),Lista,Limite)
        else:
            return 0


    def IzquierdaArriba(self,PosActual,Lista,Limite):
        if self.PosActual[1]<Limite[1] and self.PosActual[0]>0:      
            return self.LLamarVecina((self.PosActual[0]-1,self.PosActual[1]+1),Lista,Limite)
        else:
            return 0

    def DerechaArriba(self,PosActual,Lista,Limite):
        if self.PosActual[1]<Limite[1] and self.PosActual[0]<Limite[0]:      
            return self.LLamarVecina((self.PosActual[0]+1,self.PosActual[1]+1),Lista,Limite)
        else:
            return 0
    
    def IzquierdaAbajo(self,PosActual,Lista,Limite):
        if self.PosActual[1]>0 and self.PosActual[0]>0:      
            return self.LLamarVecina((self.PosActual[0]-1,self.PosActual[1]-1),Lista,Limite)
        else:
            return 0

    def DerechaAbajo(self,PosActual,Lista,Limite):
        if self.PosActual[1]>0 and self.PosActual[0]<Limite[0]:      
            return self.LLamarVecina((self.PosActual[0]+1,self.PosActual[1]-1),Lista,Limite)
        else:
            return 0