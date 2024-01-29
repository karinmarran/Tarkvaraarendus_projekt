import pygame   # impordib mängu pygame
pygame.init()   # käivitab pygame

screen=pygame.display.set_mode([300,300])   # seame akna suuruse ja avame
pygame.display.set_caption("Lumemees - Karin Marran")   # akna nimi
screen.fill([0,0,0])    # taustavärv

pygame.draw.circle(screen, [255,255,255], [150,75], 30, 0)  # lumepall nr1.
pygame.draw.circle(screen, [0,0,0], [140,70], 5, 0)     # esimene silm
pygame.draw.circle(screen, [0,0,0], [160,70], 5, 0)     # teine silm
pygame.draw.polygon(screen, [255,0,0], [[145,80], [155,80],[150,95],[145,80]], 0)   # porgandi nina

pygame.draw.circle(screen, [255,255,255], [150,140], 40, 0)     # lumepall nr2
pygame.draw.circle(screen, [255,255,255], [150,225], 50, 0)     # lumepall nr3
pygame.display.flip()   # ekraani värskendus

running = True  # selleks, et avatav aken ka lahti jääks kuniks ise selle lugen, on vastav kood
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False