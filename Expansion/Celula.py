class Celula:
    Viva=False
    Turno=False
    screen=None
    Vecinos=0
    PosActual=(0,0)
    def __init__(self,PosActual,screen):
        self.PosActual=PosActual
        self.screen=screen

    def Interactuar(self,Lista,Limite):
        
       # if (not self.Turno)  :
        #    return
        self.Vecinos=0
        self.Vecinos+=self.Izquierda(self.PosActual,Lista,Limite)
        self.Vecinos+=self.Derecha(self.PosActual,Lista,Limite)
        self.Vecinos+=self.Arriba(self.PosActual,Lista,Limite)
        self.Vecinos+=self.Abajo(self.PosActual,Lista,Limite)

        self.Vecinos+=self.IzquierdaArriba(self.PosActual,Lista,Limite)
        self.Vecinos+=self.DerechaAbajo(self.PosActual,Lista,Limite)
        self.Vecinos+=self.IzquierdaArriba(self.PosActual,Lista,Limite)
        self.Vecinos+=self.IzquierdaAbajo(self.PosActual,Lista,Limite)

       
            
        
        self.Turno =False

    def Destino(self,Lista):
       

        if self.Vecinos == 3:
            Viva= True
            Lista.get(self.PosActual).Viva=True            
        elif self.Vecinos ==2 :
            Lista.get(self.PosActual).Viva=True
            Viva=True
        else:
            Lista.get(self.PosActual).Viva=False
            #print("Morir    "+str(self.Vecinos))
            Viva=False


    def LLamarVecina(self,PosVecina,Lista,Limite):
            #if not self.Viva :
            #    return 0

                
            Obj = Lista.get(PosVecina)
            #if(Obj==None):
               # print(PosVecina)
              #  return 0
            #if Obj.Viva==False:
             #   Obj.Turno=True    
            #else :
             #   return 0        
            #Obj.Interactuar(Lista,Limite)
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
        if self.PosActual[0]<Limite[0]-1:      
            return self.LLamarVecina((self.PosActual[0]+1,self.PosActual[1]),Lista,Limite)
        else:
            return 0

    def Arriba(self,PosActual,Lista,Limite):
        if  self.PosActual[1]>1:  
            return self.LLamarVecina((self.PosActual[0],self.PosActual[1]-1),Lista,Limite)
        else:
            return 0

    def Abajo(self,PosActual,Lista,Limite):
        if  self.PosActual[1]<Limite[1]-1:    
            return self.LLamarVecina((self.PosActual[0],self.PosActual[1]+1),Lista,Limite)
        else:
            return 0


    def IzquierdaAbajo(self,PosActual,Lista,Limite):
        if self.PosActual[1]<Limite[1]-1 and self.PosActual[0]>0:      
            return self.LLamarVecina((self.PosActual[0]-1,self.PosActual[1]+1),Lista,Limite)
        else:
            return 0

    def DerechaAbajo(self,PosActual,Lista,Limite):
        if self.PosActual[1]<Limite[1]-1 and self.PosActual[0]<Limite[0]-1:      
            return self.LLamarVecina((self.PosActual[0]+1,self.PosActual[1]+1),Lista,Limite)
        else:
            return 0
    
    def IzquierdaArriba(self,PosActual,Lista,Limite):
        if self.PosActual[1]>0 and self.PosActual[0]>0:      
            return self.LLamarVecina((self.PosActual[0]-1,self.PosActual[1]-1),Lista,Limite)
        else:
            return 0

    def DerechaArriba(self,PosActual,Lista,Limite):
        if self.PosActual[1]>0 and self.PosActual[0]<Limite[0]-1:      
            return self.LLamarVecina((self.PosActual[0]+1,self.PosActual[1]-1),Lista,Limite)
        else:
            return 0