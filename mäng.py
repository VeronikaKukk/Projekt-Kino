import pygame
import os
import random 
import sys #self jaoks jne
#https://www.youtube.com/watch?v=jO6qQDNa2UY õpetus siit
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800 
GRIDSIZE =  25
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)#teeb akna nende suurustega
pygame.display.set_caption("Kass ja hiir")#lehe nimi

hiirImg = pygame.image.load(os.path.join("hiir.png"))
hiir = hiirImg.get_rect() 

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

VALGE = (255, 255, 255)

FPS = 60 #kui kiirelt mäng updateb pilti
VEL = 3 #kui kiirelt hiir liigub



class Hiir():
    def __init__(self): #hiire atribuudid
        self.length = 1 #mdea kuidas see välja näeb, needs testing
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.image = pygame.image.load(os.path.join("hiir.png")).convert()
        self.rect = self.image.get_rect() #pmst seda recti peaks vist kasutama, et imageit liigutada aga ma täpselt ei saanud aru, kuidas
        self.score = 0 #mitu juustu söödud
        self.direction = random.choice([up,down,left,right])
    
   
    
    def hiire_liigutamine(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
                elif event.key == pygame.K_x:
                    pygame.quit()

    def turn(self,point):
        self.direction = point

    def hiire_positsioon(self):
        return self.positions[0]
                
    def liikumine(self): #copy-paste, veel ei saa aru kuidas see töötab :D
        prq = self.hiire_positsioon()
        x,y = self.direction
        uuspos = (((prq[0]+(x*GRIDSIZE))%SCREEN_WIDTH), (prq[1]+(y*GRIDSIZE)))
        self.positions.insert(0,uuspos)


    def draw(self,taust):
        WIN.blit(self.image,self.rect)

    
class Kass():
    def __init__(self): #kassi atribuudid
        self.length = 2
        #self.positions =  ..
        self.image = pygame.image.load(os.path.join("kass.png"))

    #def draw(self,taust):

class Juust():
    def __init__(self): #juustu atribuudid
        self.position = (0,0)
        self.image = pygame.image.load(os.path.join("cheese.png"))
        self.suvaline()

    def suvaline(self):
        self.position = (random.randint(0,GRID_WIDTH), random.randint(0,GRID_HEIGHT))
        
    #def draw(self,taust):
'''
def draw_window(taust):
        WIN.fill(VALGE)#peab olema esimesena, sest muidu joonistaks valge teised asjad üle

        WIN.blit(Kass,(300,100))#joonistad pildi ekraanile, pilt tuleb vasakust ülevalt nurgast
        WIN.blit(H,(hiir.x,hiir.y))
        pygame.display.update()#peale muutust pead updatema, muidu ei muuda ekraani sisu
'''
def drawGrid(taust): #teeb halli-valge ruudustiku
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(taust,(255,255,255), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(taust, (224,224,224), rr)

def main():
    pygame.init() #alustab mängu
    
    hiir = Hiir()
    kass = Kass()
    juust = Juust()
    

    
    taust = pygame.Surface(WIN.get_size())
    taust = taust.convert()
    drawGrid(taust)
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        hiir.hiire_liigutamine()
        hiir.liikumine()
        WIN.blit(taust,(0,0))
        drawGrid(taust)
        hiir.draw(taust)
        #kass.draw(taust)
        #juust.draw(taust)
        for event in pygame.event.get():
            #kontrollid, mis eventid olid
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        
        #keys_pressed = pygame.key.get_pressed()#ütleb mis nupud praegu vajutatud
        #hiire_liigutamine(keys_pressed,hiir)
        #need vist pole vajalikud uue meetodiga?
    

        pygame.display.update()
        pygame.display.flip() #toob muutused ekraanile
    pygame.display.quit()
    pygame.quit()
    sys.exit


if __name__ == "__main__":
    main()
