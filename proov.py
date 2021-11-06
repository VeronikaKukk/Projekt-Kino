import pygame
import os
#https://www.youtube.com/watch?v=jO6qQDNa2UY õpetus siit
WIDTH, HEIGHT = 500,500 #akna suurus
WIN = pygame.display.set_mode((WIDTH,HEIGHT))#teeb akna nende suurustega
pygame.display.set_caption("Kass ja hiir")#lehe nimi
GRIDSIZE = 25
GRID_WIDTH = HEIGHT // GRIDSIZE
GRID_HEIGHT = WIDTH // GRIDSIZE

VALGE = (255, 255, 255)

FPS = 60 #kui kiirelt mäng updateb pilti
VEL = 3 #kui kiirelt hiir liigub

KASS_IMAGE = pygame.image.load(os.path.join("kass.png"))
KASS = pygame.transform.scale(KASS_IMAGE,(50,50))#kassi pildi suurus
HIIR_IMAGE = pygame.image.load(os.path.join("hiir.png"))
HIIR = pygame.transform.scale(HIIR_IMAGE,(25,25))#hiire pildi suurus

def drawGrid(surface):
    for y in range(0, GRID_HEIGHT):
        for x in range(0,GRID_WIDTH):
            if (x+y)%2==0:
                r = pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface,(255,255,224),r)
            else:
                rr = pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface,(236,183,83),rr)

def hiire_liigutamine(keys_pressed,hiir):
    if keys_pressed[pygame.K_a] and hiir.x -VEL > 0: #vasak
        hiir.x -= VEL
    if keys_pressed[pygame.K_d] and hiir.x +VEL + 75 < WIDTH: #parem
        hiir.x += VEL
    if keys_pressed[pygame.K_w] and hiir.y -VEL > 0: #üles
        hiir.y -= VEL
    if keys_pressed[pygame.K_s] and hiir.y + VEL + 35 < HEIGHT: #alla
        hiir.y += VEL

def kassi_liigutamine(keys_pressed,kass):
    if keys_pressed[pygame.K_LEFT] and kass.x -VEL > 0: #vasak
        kass.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and kass.x +VEL + 75 < WIDTH: #parem
        kass.x += VEL
    if keys_pressed[pygame.K_UP] and kass.y -VEL > 0: #üles
        kass.y -= VEL
    if keys_pressed[pygame.K_DOWN] and kass.y + VEL + 35 < HEIGHT: #alla
        kass.y += VEL

def draw_window(hiir,kass):
    WIN.fill(VALGE)#peab olema esimesena, sest muidu joonistaks valge teised asjad üle
    drawGrid(WIN)
    WIN.blit(KASS,(kass.x,kass.y))#joonistad pildi ekraanile, pilt tuleb vasakust nurgast
    WIN.blit(HIIR,(hiir.x,hiir.y))
    pygame.display.update()#peale muutust pead updatema, muidu ei muuda ekraani sisu

def main():
    hiir = pygame.Rect(100, 300, 25, 25)#ristkülik, milles on hiirepilt ja saab lugeda kordinaate
    kass = pygame.Rect(300, 100, 50, 50)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #kontrollid, mis eventid olid
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()#ütleb mis nupud praegu vajutatud
        hiire_liigutamine(keys_pressed,hiir)
        kassi_liigutamine(keys_pressed,kass)
        draw_window(hiir,kass)
    pygame.quit()

if __name__ == "__main__":
    main()
