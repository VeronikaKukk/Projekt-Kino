import pygame
import os
import random
import sys

pygame.init()
#pygame-s mängu tegemise õpetuse saime siit https://youtu.be/jO6qQDNa2UY
WIDTH, HEIGHT = 560,560 #akna suurus
WIN = pygame.display.set_mode((WIDTH,HEIGHT))#teeb akna nende suurustega
pygame.display.set_caption("Kass ja hiir")#lehe pealkiri
GRIDSIZE = 35
GRID_WIDTH = HEIGHT // GRIDSIZE
GRID_HEIGHT = WIDTH // GRIDSIZE
game_active = False

meiefont_tekst = pygame.font.SysFont("impact",16) #skoori lugeja font
meiefont_pealkiri = pygame.font.SysFont("impact",24)


KASS_IMAGE = pygame.image.load(os.path.join("kass.png"))
KASS = pygame.transform.scale(KASS_IMAGE,(70,70))#kassi suurus

HIIR_IMAGE = pygame.image.load(os.path.join("hiir.png"))#pilt pole enda tehtud allikas:http://pixelartmaker.com/art/3d272b1bf180b60
HIIR = pygame.transform.scale(HIIR_IMAGE,(35,35))#hiire suurus

#hiire suunad
HIIR_PAREM = pygame.transform.rotate(HIIR, 0)
HIIR_VASAK = pygame.transform.flip(HIIR, True, False)
HIIR_ALLA = pygame.transform.flip(pygame.transform.rotate(HIIR, 90), False, True)
HIIR_ÜLES = pygame.transform.rotate(HIIR, 90)

#heli saadud siit lehelt https://mixkit.co/
JUUSTU_HELI = pygame.mixer.Sound(os.path.join("juustuheli.wav"))
MANGULOPP_HELI = pygame.mixer.Sound(os.path.join("mangulopp.wav"))

JUUST_IMAGE = pygame.image.load(os.path.join("juust.png"))
JUUST = pygame.transform.scale(JUUST_IMAGE,(35,35))#juustu suurus

#intro ja gameover ekraanid
algus_tekst = meiefont_tekst.render("Liigu nuppudega WASD. Vajuta tühikut, et alustada!",1,(0,0,0))
algus = algus_tekst.get_rect(center=(250,350))

mängunimi_tekst = meiefont_pealkiri.render("Projekt Kino: Kassi ja hiire mäng",1,(0,0,0))
mängunimi = mängunimi_tekst.get_rect(center=(250,150))

intro_pilt = pygame.image.load(os.path.join("pilt.png"))
intro_pilt_rect = intro_pilt.get_rect(center=(250,250))

def drawGrid(WIN):
    for y in range(0, GRID_HEIGHT):
        for x in range(0,GRID_WIDTH):
            if (x+y)%2==0:
                r = pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(WIN,(255,255,224),r)
            else:
                rr = pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(WIN,(236,183,83),rr)


def draw_window(hiir,kass,juust,lastKey,counter):
    drawGrid(WIN)
    WIN.blit(JUUST,juust)
    #hiire pildi pööramine
    if lastKey == 0:
        WIN.blit(HIIR_PAREM,hiir)
    if lastKey == pygame.K_a:
        WIN.blit(HIIR_VASAK,hiir)
    elif lastKey == pygame.K_d:
        WIN.blit(HIIR_PAREM,hiir)
    elif lastKey == pygame.K_w:
        WIN.blit(HIIR_ÜLES,hiir)
    elif lastKey == pygame.K_s:
        WIN.blit(HIIR_ALLA,hiir)
    
    WIN.blit(KASS,kass)
    WIN.blit(counter,(5,10))
    pygame.display.update()#peale muutust pead updatema, muidu ei muuda ekraani sisu

def kas_püütud(hiir,kass):
    if pygame.Rect.colliderect(hiir,kass) == True:
        MANGULOPP_HELI.play()
        return False
    else:
        return True

hiir = pygame.Rect(70, 70, 35, 35)#ristkülik, milles on pilt ja saab lugeda koordinaate
kass = pygame.Rect(490, 490, 70, 70)
juust = pygame.Rect(random.randrange(0,WIDTH, 35),random.randrange(0, HEIGHT, 35),35,35) #suvaline juustu asukoht
clock = pygame.time.Clock()
skoor = 0
counter = meiefont_tekst.render("Skoor: {0}".format(skoor),1,(0,0,0)) #skoori lugeja
lastKey = 0
draw_window(hiir,kass,juust,lastKey,counter)
run = True
while run:
    
    #juustu kogumine
    if hiir.x == juust.x and hiir.y == juust.y: 
        JUUSTU_HELI.play()
        juust = juust = pygame.Rect(random.randrange(0, WIDTH, 35),random.randrange(0, HEIGHT, 35),35,35)
        skoor += 1
    

    for event in pygame.event.get():
        #kontrollid, mis eventid olid
        if event.type == pygame.QUIT:
            run = False
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_w or event.key == pygame.K_d:
                    lastKey = event.key
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                hiir = pygame.Rect(70, 70, 35, 35)#ristkülik, milles on pilt ja saab lugeda koordinaate
                kass = pygame.Rect(490, 490, 70, 70)
                skoor = 0
                lastKey = 0 #viimati vajutatud nupp
    #kassi liikumine    
    if game_active:
        x1 = hiir.x - kass.x
        y1 = hiir.y - kass.y
        if abs(x1) >= abs(y1):
            if x1 > 0 and kass.x + 17.5 < WIDTH:
                kass.x += 17.5
            elif x1 < 0 and kass.x - 17.5 >= 0:
                kass.x -= 17.5
        else:
            if y1 > 0 and kass.y + 17.5 < HEIGHT:
                kass.y += 17.5
            elif y1 < 0 and kass.y - 17.5 >= 0:
                kass.y -= 17.5
    #hiire liikumine
    if game_active:
        if lastKey == pygame.K_a and hiir.x - 35 >= 0: #vasak
            hiir.x -= 35
        if lastKey == pygame.K_d and hiir.x + 35 < WIDTH: #parem
            hiir.x += 35
        if lastKey == pygame.K_w and hiir.y - 35 >= 0: #üles
            hiir.y -= 35
        if lastKey == pygame.K_s and hiir.y + 35 < HEIGHT: #alla
            hiir.y += 35
        
        counter = meiefont_tekst.render("Skoor: {0}".format(skoor),1,(0,0,0)) #skoori lugeja
        draw_window(hiir,kass,juust,lastKey,counter)#joonista aknasse
        game_active = kas_püütud(hiir,kass) #kui kass puudutab hiirt, siis game_active on false   
    
    else:
        WIN.fill((135,206,250))
        skoori_näit_tekst = meiefont_tekst.render("Said skooriks: "+str(skoor),1,(0,0,0))
        skoori_näit = skoori_näit_tekst.get_rect(center=(250,350))
        WIN.blit(mängunimi_tekst,mängunimi)
        WIN.blit(intro_pilt,intro_pilt_rect)
        if skoor == 0:
            WIN.blit(algus_tekst, algus)
        
        else:
            WIN.blit(skoori_näit_tekst,skoori_näit)
    pygame.display.update()
    clock.tick(10)

pygame.quit()