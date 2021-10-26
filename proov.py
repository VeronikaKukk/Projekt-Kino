import pygame
import os
#https://www.youtube.com/watch?v=jO6qQDNa2UY õpetus siit
WIDTH, HEIGHT = 900,500 #akna suurus
WIN = pygame.display.set_mode((WIDTH,HEIGHT))#teeb akna nende suurustega
pygame.display.set_caption("Kass ja hiir")#lehe nimi

VALGE = (255, 255, 255)

FPS = 60 #kui kiirelt mäng updateb pilti
VEL = 3 #kui kiirelt hiir liigub

KASS_IMAGE = pygame.image.load(os.path.join("kass.png"))
KASS = pygame.transform.scale(KASS_IMAGE,(120,121))#kassi pildi suurus
HIIR_IMAGE = pygame.image.load(os.path.join("hiir.png"))
HIIR = pygame.transform.scale(HIIR_IMAGE,(75,35))#hiire pildi suurus

def hiire_liigutamine(keys_pressed,hiir):
    if keys_pressed[pygame.K_a] and hiir.x -VEL > 0: #vasak
        hiir.x -= VEL
    if keys_pressed[pygame.K_d] and hiir.x +VEL + 75 < WIDTH: #parem
        hiir.x += VEL
    if keys_pressed[pygame.K_w] and hiir.y -VEL > 0: #üles
        hiir.y -= VEL
    if keys_pressed[pygame.K_s] and hiir.y + VEL + 35 < HEIGHT: #alla
        hiir.y += VEL

def draw_window(hiir):
    WIN.fill(VALGE)#peab olema esimesena, sest muidu joonistaks valge teised asjad üle
    
    WIN.blit(KASS,(300,100))#joonistad pildi ekraanile, pilt tuleb vasakust nurgast
    WIN.blit(HIIR,(hiir.x,hiir.y))
    pygame.display.update()#peale muutust pead updatema, muidu ei muuda ekraani sisu

def main():
    hiir = pygame.Rect(100, 300, 75, 35)#riskülik, milles on hiirepilt ja saab lugeda kordinaate
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
        draw_window(hiir)
    pygame.quit()

if __name__ == "__main__":
    main()
