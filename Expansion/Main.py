import sys, pygame
import Celula
pygame.init()
size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

Lista ={}
for i in range(100):
    for j in range(100):
        CeluNueva = Celula.Celula((i,j),screen)
        Lista[i,j]=CeluNueva
        
Cel = Lista.get((49,50))
Cel.Viva=True
Cel = Lista.get((50,50))
Cel.Viva=True
Cel = Lista.get((50,51))
Cel.Viva=True

Cel = Lista.get((55,49))
Cel.Viva=True
Cel = Lista.get((55,51))
Cel.Viva=True
Cel = Lista.get((54,51))
Cel.Viva=True
Cel = Lista.get((56,51))
Cel.Viva=True

def IniciarJogo():
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        
        size=(100,100)
        for i in range(100):
            for j in range(100):
                Celu=Lista.get((i,j))
                Celu.Interactuar(Lista,size)
                if Lista.get((i,j)).Viva :
                    #Celu.Turno=True                         
                    Dibujar(Celu.PosActual[0],Celu.PosActual[1], (255,255,255))                                        
                else :
                    Dibujar(Celu.PosActual[0],Celu.PosActual[1], (0,0,0))            

        for i in range(100):
            for j in range(100):
                Celu=Lista.get((i,j))                
                Celu.Destino(Lista)
                             
                 
      
        pygame.display.update() 
        pygame.time.wait(1000) 
        #pygame.draw.circle(screen, (255,255,255), (50,50), 0)
def Dibujar(X,Y,Color):
    screen.set_at((X*4, Y*4),Color)
    screen.set_at((X*4+1, Y*4+1),Color)
    screen.set_at((X*4+1, Y*4+0),Color)
    screen.set_at((X*4+0, Y*4+1),Color)      
def Otro():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        pygame.time.wait(300)
        Dibujar(50,50,(255,255,255))
        Dibujar(49,50,(255,255,255))
        Dibujar(51,50,(255,255,255))
        Dibujar(50,49,(255,255,255))
        Dibujar(50,51,(255,255,255))
                 
      
        pygame.display.update() 
       
#Otro()
IniciarJogo()