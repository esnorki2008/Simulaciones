from Elementos import Presa,Entidad,Depredador,Planta,Terreno
import sys, pygame
pygame.init()
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)



Tor=[]
Tor.append((25,50))
Tor.append((40,40))
#Tor.sort()

#print(Tor[0]==(2,2))

Herbi1= Presa.Presa(3,size)
Herbi1.PosActual=Tor[0]
Herbi2= Presa.Presa(3,size)
Herbi2.PosActual=Tor[1]
ListaHerbivoro=[Herbi1,Herbi2]




def IniciarJogo():
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        pygame.time.wait(200)
        for Herbi in ListaHerbivoro:            
            screen.set_at((Herbi.PosActual[0], Herbi.PosActual[1]), (255,255,255))
            Herbi.Mover()

        pygame.display.update() 
       
        #pygame.draw.circle(screen, (255,255,255), (50,50), 0)
      
IniciarJogo()