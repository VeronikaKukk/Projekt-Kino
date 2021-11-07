import pygame
import os
import random
import sys

pygame.init()
#https://www.youtube.com/watch?v=jO6qQDNa2UY õpetus siit
WIDTH, HEIGHT = 500,500 #akna suurus
WIN = pygame.display.set_mode((WIDTH,HEIGHT))#teeb akna nende suurustega
pygame.display.set_caption("Kass ja hiir")#lehe pealkiri
GRIDSIZE = 25
GRID_WIDTH = HEIGHT // GRIDSIZE
GRID_HEIGHT = WIDTH // GRIDSIZE

meiefont = pygame.font.SysFont("impact",16) #skoori lugeja font

FPS = 60 #kui kiirelt mäng updateb pilti

KASS_IMAGE = pygame.image.load(os.path.join("kass.png"))
KASS = pygame.transform.scale(KASS_IMAGE,(50,50))#kassi suurus

HIIR_IMAGE = pygame.image.load(os.path.join("hiir.png"))
HIIR = pygame.transform.scale(HIIR_IMAGE,(25,25))#hiire suurus

#hiire suunad
HIIR_PAREM = pygame.transform.rotate(HIIR, 0)
HIIR_VASAK = pygame.transform.flip(HIIR, True, False)
HIIR_ALLA = pygame.transform.flip(pygame.transform.rotate(HIIR, 90), False, True)
HIIR_ÜLES = pygame.transform.rotate(HIIR, 90)


JUUST_IMAGE = pygame.image.load(os.path.join("juust.png"))
JUUST = pygame.transform.scale(JUUST_IMAGE,(25,25))


def drawGrid(WIN):#mõmsu koodist
    for y in range(0, GRID_HEIGHT):
        for x in range(0,GRID_WIDTH):
            if (x+y)%2==0:
                r = pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(WIN,(255,255,224),r)
            else:
                rr = pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(WIN,(236,183,83),rr)

# def kassi_liigutamine(keys_pressed,kass):

def draw_window(hiir,kass,juust,lastKey,counter):
    drawGrid(WIN)
    if lastKey == pygame.K_a:
        WIN.blit(HIIR_VASAK,hiir)
    elif lastKey == pygame.K_d:
        WIN.blit(HIIR_PAREM,hiir)
    elif lastKey == pygame.K_w:
        WIN.blit(HIIR_ÜLES,hiir)
    elif lastKey == pygame.K_s:
        WIN.blit(HIIR_ALLA,hiir)
    
    WIN.blit(JUUST,juust)
    WIN.blit(KASS,kass)
    WIN.blit(counter,(5,10))
    pygame.display.update()#peale muutust pead updatema, muidu ei muuda ekraani sisu

# def kas_püütud(hiir,kass):
#     return pygame.Rect.colliderect(hiir,kass)
# 
# def kas_juust(hiir,juust):
#     return pygame.Rect.colliderect(hiir,juust)

def main():
    hiir = pygame.Rect(300, 100, 25, 25)#ristkülik, milles on pilt ja saab lugeda koordinaate
    kass = pygame.Rect(300, 100, 50, 50)
    juust = pygame.Rect(random.randrange(0,WIDTH, 25),random.randrange(0, HEIGHT, 25),25,25) #suvaline juustu asukoht
    skoor = 0
    
    lastKey = 0 #viimati vajutatud nupp
    clock = pygame.time.Clock()
    
    
    run = True
    while run:
        clock.tick(10)
        if hiir.x == juust.x and hiir.y == juust.y:
            juust = juust = pygame.Rect(random.randrange(0,WIDTH, 25),random.randrange(0, HEIGHT, 25),25,25)
            skoor += 1
            

        for event in pygame.event.get():
            #kontrollid, mis eventid olid
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                lastKey = event.key
        if lastKey == pygame.K_a and hiir.x - 25 >= 0: #vasak
            hiir.x -=25
        if lastKey == pygame.K_d and hiir.x + 25 < WIDTH: #parem
            hiir.x += 25
        if lastKey == pygame.K_w and hiir.y - 25 >= 0: #üles
            hiir.y -= 25
        if lastKey == pygame.K_s and hiir.y + 25 < HEIGHT: #alla
            hiir.y += 25
        
        
        
        
        pygame.display.update()

#         kassi_liigutamine(keys_pressed,kass)
        counter = meiefont.render("Skoor: {0}".format(skoor),1,(0,0,0)) #skoori lugeja
        draw_window(hiir,kass,juust,lastKey,counter)
    
    pygame.quit()

if __name__ == "__main__":
    main()