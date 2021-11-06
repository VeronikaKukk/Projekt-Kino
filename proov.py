import pygame
import os
#https://www.youtube.com/watch?v=jO6qQDNa2UY õpetus siit
WIDTH, HEIGHT = 500,500 #akna suurus
WIN = pygame.display.set_mode((WIDTH,HEIGHT))#teeb akna nende suurustega
pygame.display.set_caption("Kass ja hiir")#lehe pealkiri
GRIDSIZE = 25
GRID_WIDTH = HEIGHT // GRIDSIZE
GRID_HEIGHT = WIDTH // GRIDSIZE

FPS = 60 #kui kiirelt mäng updateb pilti

KASS_IMAGE = pygame.image.load(os.path.join("kass.png"))
KASS = pygame.transform.scale(KASS_IMAGE,(50,50))#kassi suurus
HIIR_IMAGE = pygame.image.load(os.path.join("hiir.png"))
HIIR = pygame.transform.scale(HIIR_IMAGE,(25,25))#hiire suurus
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

def hiire_liigutamine(keys_pressed,hiir):
    if keys_pressed[pygame.K_a] and hiir.x - 1 > 0: #vasak
        hiir.x -= 1
    if keys_pressed[pygame.K_d] and hiir.x + 1 + 25 < WIDTH: #parem
        hiir.x += 1
    if keys_pressed[pygame.K_w] and hiir.y - 1 > 0: #üles
        hiir.y -= 1
    if keys_pressed[pygame.K_s] and hiir.y + 1 + 25 < HEIGHT: #alla
        hiir.y += 1

def kassi_liigutamine(keys_pressed,kass):
    if keys_pressed[pygame.K_LEFT] and kass.x -1 > 0: #vasak
        kass.x -= 1
    if keys_pressed[pygame.K_RIGHT] and kass.x + 1 + 50 < WIDTH: #parem
        kass.x += 1
    if keys_pressed[pygame.K_UP] and kass.y - 1 > 0: #üles
        kass.y -= 1
    if keys_pressed[pygame.K_DOWN] and kass.y + 1 + 50 < HEIGHT: #alla
        kass.y += 1

def draw_window(hiir,kass,juust):
    drawGrid(WIN)
    WIN.blit(JUUST,juust)
    WIN.blit(KASS,kass)
    WIN.blit(HIIR,hiir)
    pygame.display.update()#peale muutust pead updatema, muidu ei muuda ekraani sisu

def kas_püütud(hiir,kass):
    return pygame.Rect.colliderect(hiir,kass)

def kas_juust(hiir,juust):
    return pygame.Rect.colliderect(hiir,juust)

def main():
    hiir = pygame.Rect(300, 100, 25, 25)#ristkülik, milles on pilt ja saab lugeda koordinaate
    kass = pygame.Rect(300, 100, 50, 50)
    juust = pygame.Rect(0,0,25,25)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #kontrollid, mis eventid olid
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()#ütleb, mis nupud praegu vajutatud
        if kas_püütud(hiir,kass) == True:
            print("Söödud")
        else:
            print("Ei ole söödud")
        if kas_juust(hiir,juust) == True:
            print("Oled juustu peal")
        hiire_liigutamine(keys_pressed,hiir)
        kassi_liigutamine(keys_pressed,kass)
        draw_window(hiir,kass,juust)
    
    pygame.quit()

if __name__ == "__main__":
    main()
