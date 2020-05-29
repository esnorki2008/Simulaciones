from Elementos import Presa,Entidad,Depredador,Planta,Terreno
import sys, pygame

pygame.init()
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)




#print(Tor[0]==(2,2))
size=25,10
Herbi1= Presa.Presa(3,size)
Herbi1.PosActual=(11,3)
Herbi2= Presa.Presa(3,size)
Herbi2.PosActual=(10,5)
Planta1=Planta.Planta(1,size)
Planta1.PosActual=(15,4)
Planta2=Planta.Planta(1,size)
Planta2.PosActual=(15,2)


ListaHerbivoro=[]#[Herbi1,Herbi2]
ListaPnlanta=[Planta1,Planta2]


def IniciarJogo():
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        pygame.time.wait(300)
        for Herbi in ListaHerbivoro:            
            screen.set_at((Herbi.PosActual[0], Herbi.PosActual[1]), Herbi.Color())
            Herbi.Mover()

        for Planta in ListaPnlanta:            
            Dibujar(Planta.PosActual[0], Planta.PosActual[1], Planta.Color())
            Planta.Expandir(ListaPnlanta,size)

        pygame.display.update() 
       
        #pygame.draw.circle(screen, (255,255,255), (50,50), 0)

def Dibujar(X,Y,Color):
    screen.set_at((X*5, Y*5),Color)
    screen.set_at((X*5+1, Y*5+1),Color)
    screen.set_at((X*5+1, Y*5+0),Color)
    screen.set_at((X*5+0, Y*5+1),Color)


IniciarJogo()