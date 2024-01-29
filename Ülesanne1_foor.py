import pygame   # impordib mängu pygame
pygame.init()   # käivitab pygame

screen=pygame.display.set_mode([300,300])   # sean akna suuruseks 300x300
pygame.display.set_caption("Foor - Karin Marran")   # sean akna nime
screen.fill([0,0,0])    # taustavärv

pygame.draw.circle(screen, [255,0,0], [150,65], 40, 0)  # joonistan punase ringi
pygame.draw.circle(screen, [255,255,0], [150,150], 40, 0)   # joonistan kollase ringi
pygame.draw.circle(screen, [0,255,1], [150,235], 40, 0)     # joonistan rohelise ringi

pygame.draw.rect(screen, [134,132,133], [100,15,100,270], 2)    # joonistan ristküliku ümber ringide

pygame.display.flip()   # värskendab ekraani

running = True  # selleks, et avatav aken ka lahti jääks kuniks ise selle lugen, on vastav kood
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False