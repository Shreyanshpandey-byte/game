import pygame

wx=1280
wy=720
pygame.init()
screen = pygame.display.set_mode((wx,wy))
clock = pygame.time.Clock()
running = True

def point(x,y):
    pygame.draw.rect(screen,"red",(x+wx/2,y+wy/2,20,20))
class cude():
    def __init__(self,lis):
        self.p0=lis[0]
        self.p1=lis[1]
        self.p2=lis[2]
        self.p3=lis[3]
        self.p4=lis[4]
        self.p5=lis[5]
        self.p6=lis[6]
        self.p7=lis[7] 


        self.p0[0]=self.p0[0]/self.p0[2]
        self.p1[0]=self.p1[0]/self.p1[2]
        self.p2[0]=self.p2[0]/self.p2[2]
        self.p3[0]=self.p3[0]/self.p3[2]
        self.p4[0]=self.p4[0]/self.p4[2]
        self.p5[0]=self.p5[0]/self.p5[2]
        self.p6[0]=self.p6[0]/self.p6[2]
        self.p7[0]=self.p7[0]/self.p7[2]

        self.p0[1]=self.p0[1]/self.p0[2]
        self.p1[1]=self.p1[1]/self.p1[2]
        self.p2[1]=self.p2[1]/self.p2[2]
        self.p3[1]=self.p3[1]/self.p3[2]
        self.p4[1]=self.p4[1]/self.p4[2]
        self.p5[1]=self.p5[1]/self.p5[2]
        self.p6[1]=self.p6[1]/self.p6[2]
        self.p7[1]=self.p7[1]/self.p7[2]
    def draw(self):


        pygame.draw.line(screen,"red",(self.p0[0]+wx/2, self.p0[1]+wy/2),(self.p1[0]+wx/2, self.p1[1]+wy/2),10)
        pygame.draw.line(screen,"red",(self.p1[0]+wx/2, self.p1[1]+wy/2),(self.p3[0]+wx/2, self.p3[1]+wy/2),10)
        pygame.draw.line(screen,"red",(self.p2[0]+wx/2, self.p2[1]+wy/2),(self.p0[0]+wx/2, self.p0[1]+wy/2),10)
        pygame.draw.line(screen,"red",(self.p3[0]+wx/2, self.p3[1]+wy/2),(self.p2[0]+wx/2, self.p2[1]+wy/2),10)

        pygame.draw.line(screen,"red",(self.p4[0]+wx/2, self.p4[1]+wy/2),(self.p5[0]+wx/2, self.p5[1]+wy/2),10)
        pygame.draw.line(screen,"red",(self.p5[0]+wx/2, self.p5[1]+wy/2),(self.p7[0]+wx/2, self.p7[1]+wy/2),10)
        pygame.draw.line(screen,"red",(self.p6[0]+wx/2, self.p6[1]+wy/2),(self.p4[0]+wx/2, self.p4[1]+wy/2),10)
        pygame.draw.line(screen,"red",(self.p7[0]+wx/2, self.p7[1]+wy/2),(self.p6[0]+wx/2, self.p6[1]+wy/2),10)


        pygame.draw.line(screen,"red",(self.p0[0]+wx/2, self.p0[1]+wy/2),(self.p4[0]+wx/2, self.p4[1]+wy/2),10)
        pygame.draw.line(screen,"red",(self.p1[0]+wx/2, self.p1[1]+wy/2),(self.p5[0]+wx/2, self.p5[1]+wy/2),10)
        pygame.draw.line(screen,"red",(self.p2[0]+wx/2, self.p2[1]+wy/2),(self.p6[0]+wx/2, self.p6[1]+wy/2),10)
        pygame.draw.line(screen,"red",(self.p3[0]+wx/2, self.p3[1]+wy/2),(self.p7[0]+wx/2, self.p7[1]+wy/2),10)



xo=1.5
yo=1

lis=[
    [100,100,xo],
    [200,100,xo],
    [100,200,xo],
    [200,200,xo],
    [100,100,yo],
    [200,100,yo],
    [100,200,yo],
    [200,200,yo]
]

cu=cude(lis)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    cude.draw(cu)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()