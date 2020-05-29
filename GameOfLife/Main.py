import sys, pygame
pygame.init()
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)


def IniciarJogo():
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        pygame.time.wait(200)
        for Herbi in ListaHerbivoro:            
            screen.set_at((Herbi.PosActual[0]+135, Herbi.PosActual[1]+95), Herbi.Color())
            Herbi.Mover()

        for Planta in ListaPnlanta:            
            screen.set_at((Planta.PosActual[0]+135, Planta.PosActual[1]+95), Planta.Color())
            Planta.Expandir(ListaPnlanta,size)

        pygame.display.update() 
       
        #pygame.draw.circle(screen, (255,255,255), (50,50), 0)
      
IniciarJogo()