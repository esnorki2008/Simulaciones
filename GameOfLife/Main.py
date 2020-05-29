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
        CeluNueva = Celula.Celula((i,j))
        Lista[i,j]=CeluNueva
        
Cel = Lista.get((50,50))
Cel.Viva=True
Cel = Lista.get((51,50))
Cel.Viva=True
Cel = Lista.get((52,50))
Cel.Viva=True


def IniciarJogo():
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        pygame.time.wait(200)

        for i in range(100):
            for j in range(100):
                Celu=Lista.get((i,j))
                if Celu.Viva :
                    Celu.Turno=True
                    Celu.Interactuar(Lista,size)       
                    screen.set_at(Celu.PosActual, (255,255,255))
      
        pygame.display.update() 
       
        #pygame.draw.circle(screen, (255,255,255), (50,50), 0)
      
IniciarJogo()