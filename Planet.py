import pygame
import math
pygame.init() 

lebar = float(input('Masukkan Lebar Layar:'))
tinggi= float(input('Masukkan Tinggi Layar:'))
window=pygame.display.set_mode((lebar,tinggi))
pygame.display.set_caption("Planet Simulation")

putih=(255,255,255)
kuning=(255,255,0)
biru=(100,149,237)
merah=(188,39,50)
abu=(80,78,81)
coklat=(255,234,91)
cream=(255,255,153)
cyan=(0,128,255)
pale=(153,204,255)

class Planet  :
    AU=149.6e6*1000
    G=6.67428e-11
    SCALE=250/AU 
    TIMESTEP=3600*24
    
    def __init__(self,x,y,radius,color,mass):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.mass=mass

        self.orbit=[]
        self.sun=False
        self.distance_to_sun=0

        self.x_vel=0
        self.y_vel=0

    def draw(self,window):
        x=self.x*self.SCALE+lebar/2
        y=self.y*self.SCALE+tinggi/2
        pygame.draw.circle(window,self.color,(x,y),self.radius)

def main():
    run=True
    clock=pygame.time.Clock()

    matahari=Planet(0,0,20,kuning,1.98892*10**30)
    matahari.matahari=True

    bumi=Planet(-0.6*Planet.AU,0,11,biru,5.9742*10**24)

    mars=Planet(-0.8*Planet.AU,0,8,merah,6.39*10**23)

    merkurius=Planet(0.2*Planet.AU,0,6,abu,3.30*10**23)

    venus=Planet(0.4*Planet.AU,0,7,putih,4.8685*10**24)

    jupiter=Planet(1*Planet.AU,0,16,coklat,1.89813*(10**27))

    saturnus=Planet(1.2*Planet.AU,0,13,cream,5.683*10**26)

    uranus=Planet(-1.4*Planet.AU,0,14,pale,8.68103*10**25)

    neptunus=Planet(-1.6*Planet.AU,0,15,cyan,1.024*10**26)

    planets=[matahari,bumi,mars,merkurius,venus,jupiter,saturnus,uranus,neptunus]

    while run :
        clock.tick(60)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        
        for planet in planets:
            planet.draw(window)

        pygame.display.update()

    pygame.quit() 

main()
