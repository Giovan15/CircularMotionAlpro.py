import pygame
import math
pygame.init() 
import csv

with open('AU.csv') as file:
	read_csv = csv.reader(file)
	data_list = list(read_csv)
for row in data_list:
	print(row)

lebar = 800
tinggi= 800
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

font=pygame.font.SysFont("comicsans",16)

class Planet  :
    AU= 
    G=6.67428e-11
    SCALE=200/AU 
    TIMESTEP=3600*24
    
    def __init__(self,x,y,radius,color,mass):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.mass=mass

        self.orbit=[]
        self.matahari=False
        self.distance_to_sun=0

        self.x_vel=0
        self.y_vel=0

    def draw(self,window):
        x=self.x*self.SCALE+lebar/2
        y=self.y*self.SCALE+tinggi/2

        if len(self.orbit)>2:
            updated_points=[]
            for point in self.orbit:
                x,y=point
                x=x*self.SCALE+lebar/2  
                y=y*self.SCALE+tinggi/2
                updated_points.append((x,y))

            pygame.draw.lines(window,self.color,False,updated_points,2)

        pygame.draw.circle(window,self.color,(x,y),self.radius)
        if not self.matahari:
            distance_text=font.render(f"{round(self.distance_to_matahari/1000,1)}km",1,putih)
            window.blit(distance_text,(x - distance_text.get_width()/2,y - distance_text.get_height()/2))

    def attraction(self,other):
        other_x,other_y=other.x,other.y
        distance_x=other_x - self.x
        distance_y=other_y - self.y
        distance=math.sqrt(distance_x**2 + distance_y**2)

        if other.matahari:
            self.distance_to_matahari=distance
        
        force=self.G*self.mass*other.mass/distance**2
        theta=math.atan2(distance_y,distance_x)
        force_x=math.cos(theta)*force
        force_y=math.sin(theta)*force
        return force_x, force_y

    def update_position(self,planets):
        total_fx=total_fy=0
        for planet in planets:
            if self==planet:
                continue

            fx,fy=self.attraction(planet)
            total_fx+=fx
            total_fy+=fy

        self.x_vel+=total_fx/self.mass*self.TIMESTEP
        self.y_vel+=total_fy/self.mass*self.TIMESTEP

        self.x+=self.x_vel*self.TIMESTEP
        self.y+=self.y_vel*self.TIMESTEP
        self.orbit.append((self.x,self.y))

 
def main():
    run=True
    clock=pygame.time.Clock()

    matahari=Planet(0,0,30,kuning,1.98892*10**30)
    matahari.matahari=True

    bumi=Planet(-1*Planet.AU,0,16,biru,5.9742*10**24)
    bumi.y_vel=29.783*1000

    mars=Planet(-1.524*Planet.AU,0,12,merah,6.39*10**23)
    mars.y_vel=24.077*1000

    merkurius=Planet(0.387*Planet.AU,0,8,abu,3.30*10**23)
    merkurius.y_vel=-47.4*1000

    venus=Planet(0.723*Planet.AU,0,14,putih,4.8685*10**24)
    venus.y_vel=-35.02*1000

    jupiter=Planet(5.2*Planet.AU,0,16,coklat,1.89813*(10**27))
    jupiter.y_vel=-13.06*1000

    saturnus=Planet(9.5*Planet.AU,0,13,cream,5.683*10**26)
    saturnus.y_vel=-9.67*1000

    uranus=Planet(-19.8*Planet.AU,0,14,pale,8.68103*10**25)
    uranus.y_vel=6.79*1000

    neptunus=Planet(-30*Planet.AU,0,15,cyan,1.024*10**26)
    neptunus.y_vel=5.45*1000

    planets=[matahari,bumi,mars,merkurius,venus,jupiter,saturnus,uranus,neptunus]

    while run :
        clock.tick(60)
        window.fill((0,0,0))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        
        for planet in planets:
            planet.update_position(planets)
            planet.draw(window)

        pygame.display.update()

    pygame.quit() 

main()
