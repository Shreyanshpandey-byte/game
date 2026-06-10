import pygame

wx=1280
wy=720
pygame.init()
screen = pygame.display.set_mode((wx,wy))
clock = pygame.time.Clock()
running = True

def point(x,y):
    pygame.draw.rect(screen,"red",(x+wx/2,y+wy/2,20,20))




while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    point(-100,-100)
    point(0,0)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()