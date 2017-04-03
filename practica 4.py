import pygame,random
from pygame.locals import *
xmax = 855   #ancho de la pantalla
ymax = 550     #alto de la pantalla

class Particle():
    def __init__(self, iniciox, inicioy):
        self.x = iniciox
        self.y = inicioy
        self.sx = iniciox
        self.sy = inicioy

    def move(self, d, mx, my):   #formato de movimiento
        cambio = d
        if random.random() < 0.5:
            cambio *= -1
        if random.random() < 0.5:
            self.y += cambio
            if self.y < 0:      
                self.y += my
            elif self.y > my:
                self.y -= my
        else:
            self.x += cambio
            if self.x < 0:
                self.x += mx
            elif self.x > mx:
                self.x -= mx
        

def main():  #declaracion de colores
    pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))
    fondo = (0, 0, 0) 
    gris = (170, 170, 170)
    rojo = (200, 0, 0)
    delta = 10

    clock=pygame.time.Clock()

    particulas = []
    for part in range(100):  #Cantidad de partículas     
        particulas.append( Particle(delta * random.randint(0, xmax//delta), delta * random.randint(0, ymax//delta)) ) #Ajuste de posicion inicial

    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(fondo)
        pos = []
        for p in particulas:
            p.move(delta, xmax, ymax)
            ubic = (p.x, p.y)
            col = gris
            if ubic not in pos:
                pos.append(ubic)
            else:
                col = rojo
            pygame.draw.circle(screen, col, (p.x, p.y), delta // 2 - 2)

        pygame.display.flip()
        clock.tick(12) #Ajuste del tiempo
    pygame.quit()

if __name__ == "__main__":
    main()
