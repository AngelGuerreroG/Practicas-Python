import pygame,random
from pygame.locals import *
from math import sqrt

xmax = 500    #ancho de la pantalla
ymax = 500     #alto de la pantalla

class Particle():
    def __init__(self, iniciox, inicioy):
        self.x = iniciox
        self.y = inicioy
        self.sx = iniciox
        self.sy = inicioy

    def move(self, d, mx, my): # tipo de movimiento 
        cambio = d
        if random.random() < 0.5: # condiciones de movimiento (en dona).
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

    clock=pygame.time.Clock()

    particulas = []
    tam = []# lista de tamaños de particula 
    delta = 10 # valores permitidos
    cant = 100 # cantidad de particulas
    top = 40 # Tamaño maximo para cambio de color
    red = (255,0,0)
    for part in range(cant):      
        particulas.append( Particle(delta * random.randint(0, xmax//delta), delta * random.randint(0, ymax//delta)) ) #Ajuste de posicion inicial
        tam.append(10)

    exitflag = False
    while cant > 0 and not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(fondo)
        colision = list() 
        for pi in range(cant):
            p = particulas[pi] # p son particulas iniciales 
            p.move(delta, xmax, ymax)

        for pi in range(cant - 1): 
            p1 = particulas[pi]
            for pj in range(pi, cant):
                p2 = particulas[pj]
                dist = sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)# Distancia euclidiana
                if dist < tam[pi] + tam[pj]: 
                   colision.append(pi)
                   colision.append(pj)

        vivos = []
        tv = []
        for pos in range(cant):# posicion de particula dependiendo de la cantidad de particulas 
            p = particulas[pos]
            aux = int(round(tam[pos]))  
            pygame.draw.circle(screen, (p.x % 255, p.y % 255, min(aux, 255)), (p.x, p.y), aux)
            if pos in set(colision):
                conteo = colision.count(pos)
                tam[pos] *= (1.0 + conteo * 0.005) # porsentaje de crecimiento dependiendo de la posicion de la particula
                if tam[pos] <= top:
                    vivos.append(p)
                    tv.append(tam[pos])
        particulas = vivos
        tam = tv
        cant = len(vivos)
        print(cant)

        pygame.display.flip()
        clock.tick(10) #Ajuste del tiempo
    pygame.quit()

if __name__ == "__main__":
    main()
