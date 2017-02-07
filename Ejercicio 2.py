import pygame,random
from pygame.locals import *

xmax = 850    #ancho de la pantalla
ymax = 600     #alto de la pantalla

class Particle():
    def __init__(self, iniciox, inicioy, col):
        self.x = iniciox
        self.y = random.randint(0, inicioy)
        self.col = col
        self.sx = iniciox
        self.sy = inicioy

    def move(self):
        if self.y < 0:
            self.x=self.sx
            self.y=self.sy

        else:
            self.y-=1

        self.x+=random.randint(-5, 5) #Valores permitidos en el eje X

def main():  #declaracion de colores
    pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))
    white = (255, 255, 255) 
    black = (0,0,0)
    grey = (128,128,128)

    clock=pygame.time.Clock()

    particulas = []
    for part in range(300):  #Cantidad de partículas
        if part % 2 > 0: col = black
        else: col = grey
        particulas.append( Particle(210, 550, col) ) #Ajuste de posicion inicial

    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(white)
        for p in particulas:
            p.move()
            pygame.draw.circle(screen, p.col, (p.x, p.y), 2)

        pygame.display.flip()
        clock.tick(55) #Ajuste del tiempo
    pygame.quit()

if __name__ == "__main__":
    main()
