import pygame
import os
import random
import sys

pygame.init()
#pygame-s mängu tegemise õpetuse saime siit https://youtu.be/jO6qQDNa2UY ja siit https://www.youtube.com/watch?v=AY9MnQ4x3zk

#ekraan
WIDTH, HEIGHT = 560, 560
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Kass ja hiir")
GRIDSIZE = 35
GRID_WIDTH = HEIGHT // GRIDSIZE
GRID_HEIGHT = WIDTH // GRIDSIZE

#pildid
KASS_IMAGE = pygame.image.load(os.path.join("pildid/kass.png"))
KASS = pygame.transform.scale(KASS_IMAGE,(70, 70))
HIIR_IMAGE = pygame.image.load(os.path.join("pildid/hiir.png"))
HIIR = pygame.transform.scale(HIIR_IMAGE,(35, 35))
JUUST_IMAGE = pygame.image.load(os.path.join("pildid/juust.png"))
JUUST = pygame.transform.scale(JUUST_IMAGE,(35, 35))

#hiire suunad
HIIR_PAREM = pygame.transform.rotate(HIIR, -90)
HIIR_VASAK = pygame.transform.rotate(HIIR, 90)
HIIR_ALLA = pygame.transform.flip(HIIR, False, True)
HIIR_ÜLES = pygame.transform.rotate(HIIR, 0)

#heli 
#juustu ja mängulõpu heli saadud siit lehelt https://mixkit.co/
JUUSTU_HELI = pygame.mixer.Sound(os.path.join("heli/juustuheli.wav"))
MANGULOPP_HELI = pygame.mixer.Sound(os.path.join("heli/mangulopp.wav"))
# taustamuusika tehtud siin https://www.beepbox.co/
pygame.mixer.music.load("heli/muusika.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


#font
meiefont_tekst = pygame.font.SysFont("impact", 16)
meiefont_pikktekst = pygame.font.SysFont("impact", 22) 
meiefont_kiri = pygame.font.SysFont("impact", 30)
meiefont_pealkiri = pygame.font.SysFont("impact", 35)

#intro ja gameover ekraanid
mängunimi_tekst = meiefont_pealkiri.render(" Projekt Kino: Kassi ja hiire mäng ", 1,(255, 255, 255),(80, 79, 84))
mängunimi = mängunimi_tekst.get_rect(center=(280, 100))
start_tekst = meiefont_kiri.render(" Start ", 1,(255, 255, 255),(80, 79, 84))
start = start_tekst.get_rect(center=(280, 260))
raskusaste_tekst = meiefont_pikktekst.render(" Keerukus: Vajuta 0- kerge, 1- keskmine, 2- raske ",1,(255,255,255),(80,79,84))
raskusaste = raskusaste_tekst.get_rect(center=(280, 440))
gameover_tekst = meiefont_kiri.render(" Uuesti mängimiseks vajuta tühikut ", 1,(255, 255, 255),(80, 79, 84))
gameover = gameover_tekst.get_rect(center=(280, 330))

howtoplay_tekst = meiefont_kiri.render(" Mängujuhend ", 1,(255, 255, 255),(80, 79, 84))
howtoplay = howtoplay_tekst.get_rect(center=(280, 350))
juhendid1_tekst = meiefont_kiri.render("Liigu nuppudega WASD.", 1,(255, 255, 255))
juhendid2_tekst = meiefont_kiri.render("Kogu juustu ja hoia kassist eemale.", 1,(255, 255, 255))
juhendid3_tekst = meiefont_kiri.render(" tagasi: vajuta x", 1,(255, 255, 255))
juhendid1 = juhendid1_tekst.get_rect(center=(280, 320))
juhendid2 = juhendid2_tekst.get_rect(center=(280, 360))
juhendid3 = juhendid3_tekst.get_rect(center=(280, 400))

intro_pilt = pygame.image.load(os.path.join("pildid/taust.png"))
intro_pilt_rect = intro_pilt.get_rect(center=(280, 280))

#funktsioonid
def drawGrid(WIN):
    for y in range(0, GRID_HEIGHT):
        for x in range(0, GRID_WIDTH):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE),(GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(WIN,(255, 255, 224), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE),(GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(WIN,(236, 183, 83), rr)


def draw_window(hiir, kass, juust, lastKey, counter):
    drawGrid(WIN)
    WIN.blit(JUUST,juust)
    #hiire pildi pööramine
    if lastKey == 0:
        WIN.blit(HIIR_PAREM, hiir)
    if lastKey == pygame.K_a:
        WIN.blit(HIIR_VASAK, hiir)
    elif lastKey == pygame.K_d:
        WIN.blit(HIIR_PAREM, hiir)
    elif lastKey == pygame.K_w:
        WIN.blit(HIIR_ÜLES, hiir)
    elif lastKey == pygame.K_s:
        WIN.blit(HIIR_ALLA, hiir)
    
    WIN.blit(KASS, kass)
    WIN.blit(counter,(5, 10))
    pygame.display.update()

def kas_püütud(hiir,kass):
    if pygame.Rect.colliderect(hiir, kass) == True:
        MANGULOPP_HELI.play()
        return False
    else:
        return True

hiir = pygame.Rect(70, 70, 35, 35)
kass = pygame.Rect(490, 490, 70, 70)
juust = pygame.Rect(random.randrange(0, WIDTH, 35),random.randrange(0, HEIGHT, 35), 35, 35) #suvaline juustu asukoht

clock = pygame.time.Clock()
skoor = 0
lastKey = 0
run = True
juhend = False
game_active = False
keerukus = 17.5

while run:
    #juustu kogumine
    if hiir.x == juust.x and hiir.y == juust.y: 
        JUUSTU_HELI.play()
        juust = juust = pygame.Rect(random.randrange(0, WIDTH, 35),random.randrange(0, HEIGHT, 35), 35, 35)
        skoor += 1
    #nupuvajutused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_w or event.key == pygame.K_d:
                    lastKey = event.key
        else:
            #keerukus
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    keerukus = 13
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    keerukus = 17.5
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    keerukus = 22
            #mängu algus
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                hiir = pygame.Rect(70, 70, 35, 35)
                kass = pygame.Rect(490, 490, 70, 70)
                skoor = 0
                lastKey = 0
     
    if game_active:
        #hiire liikumine
        if lastKey == pygame.K_a and hiir.x - 35 >= 0: #vasak
            hiir.x -= 35
        if lastKey == pygame.K_d and hiir.x + 35 < WIDTH: #parem
            hiir.x += 35
        if lastKey == pygame.K_w and hiir.y - 35 >= 0: #üles
            hiir.y -= 35
        if lastKey == pygame.K_s and hiir.y + 35 < HEIGHT: #alla
            hiir.y += 35
        
        #kassi liikumine   
        x1 = hiir.x - kass.x
        y1 = hiir.y - kass.y
        if abs(x1) >= abs(y1):
            if x1 > 0 and kass.x + keerukus < WIDTH:
                kass.x += keerukus
            elif x1 < 0 and kass.x - keerukus >= 0:
                kass.x -= keerukus
        else:
            if y1 > 0 and kass.y + keerukus < HEIGHT:
                kass.y += keerukus
            elif y1 < 0 and kass.y - keerukus >= 0:
                kass.y -= keerukus
        
        counter = meiefont_tekst.render("Skoor: {0}".format(skoor), 1,(0, 0, 0)) #skoori lugeja
        draw_window(hiir,kass,juust,lastKey,counter)#joonista aknasse
        game_active = kas_püütud(hiir,kass) #kui kass puudutab hiirt, siis game_active on false   
    
    else:
        #intro ja gameover screenid
        WIN.blit(intro_pilt, intro_pilt_rect)
        skoori_näit_tekst = meiefont_kiri.render(" Said skooriks: "+str(skoor), 1,(255, 255, 255),(80, 79, 84))
        skoori_näit = skoori_näit_tekst.get_rect(center=(280, 280))
        WIN.blit(mängunimi_tekst,mängunimi)
        if skoor == 0:
            WIN.blit(start_tekst,start)
            WIN.blit(howtoplay_tekst,howtoplay)
            WIN.blit(raskusaste_tekst,raskusaste)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            #start nupp reaktsioon
            if click[0] == 1 and 245 <= mouse[0] <= 316 and 242 <= mouse[1] <= 279:
                game_active = True
                hiir = pygame.Rect(70, 70, 35, 35)
                kass = pygame.Rect(490, 490, 70, 70)
                skoor = 0
                lastKey = 0
            #juhend nupp reaktsioon
            elif click[0]==1 and 189 <= mouse[0] <= 371 and 332 <= mouse[1] <= 369:
                juhend = True
            while juhend:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        juhend = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                        juhend = False
                pygame.draw.rect(WIN,(80, 79, 84),[55, 235, 450, 250])
                WIN.blit(juhendid1_tekst, juhendid1)
                WIN.blit(juhendid2_tekst, juhendid2)
                WIN.blit(juhendid3_tekst, juhendid3)
                pygame.display.update()

        else:
            WIN.blit(skoori_näit_tekst, skoori_näit)
            WIN.blit(gameover_tekst, gameover)
            WIN.blit(raskusaste_tekst,raskusaste)
            #keerukus
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        keerukus = 13
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        keerukus = 17.5
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        keerukus = 22
            
    pygame.display.update()
    clock.tick(10)

pygame.quit()