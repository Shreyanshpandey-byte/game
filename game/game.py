import pygame
import pygame.display
import time
from pytmx.util_pygame import load_pygame
from os.path import join
from random import randint


magic_data={"fire":{"cost":10,"location":"C:/python-pracities/game/image/fire.png"},
            "heal":{"cost":10,"location":"C:/python-pracities/game/image/heal.png"}}


class allsprites(pygame.sprite.Group):#use for crearing the camera
    def __init__(self):
        super().__init__()
        self.offset=pygame.Vector2()

    def draw(self, surface,target_postion):
        self.offset.x=-(target_postion[0]-wx/2)#to make the player at the center
        self.offset.y=-(target_postion[1]-wy/2)
        for sprite in self:
            surface.blit(sprite.image,sprite.rect.topleft+self.offset)


class player(pygame.sprite.Sprite):
    def __init__(self,group,collision):#group argymen is for the group we add
        super().__init__(group)#use in inheritance
        #loading and rescaling the image
        self.image=pygame.transform.scale(pygame.image.load("C:/python-pracities/game/image/ov.png").convert_alpha(),(100,100))
       #making the image into a frectangle and geting the postin to put it in
        self.rect=self.image.get_frect(center=(wx-500,wy+300))
        self.collision=collision
        self.max_healt=100
        self.healt=100
        self.max_exp=100
        self.exp=0
        self.max_magic=100
        self.magic=100
        self.mous=pygame.Vector2(pygame.mouse.get_pos())
        self.level=1

    def movement(self):#player movement
        play_direction=pygame.math.Vector2()
        self.play_direction=play_direction
        keys=pygame.key.get_pressed()
        play_direction.x=int(keys[pygame.K_d]-keys[pygame.K_a])#if the key is presswd we get true which is converted into int
        play_direction.y=int(keys[pygame.K_s]-keys[pygame.K_w])
        play_direction=play_direction.normalize()if play_direction else play_direction#if the vector is not(0,0)then normalize them
        self.rect.x += play_direction.x *7
        self.collision1('horizantal')#calling the function
        self.rect.y += play_direction.y *7
        self.collision1('vertical')

    def collision1(self,direction):
        for sprit in self.collision:
            if sprit.rect.colliderect(self.rect):
                if direction == 'horizantal':
                    if self.play_direction.x > 0:self.rect.right=sprit.rect.left
                    if self.play_direction.x < 0:self.rect.left=sprit.rect.right
                else:
                    if self.play_direction.y < 0:self.rect.top=sprit.rect.bottom
                    if self.play_direction.y > 0:self.rect.bottom=sprit.rect.top
    def bars(self):
        pygame.draw.rect(screen,"gray",(50,10,200,20))
        pygame.draw.rect(screen,"gray",(50,40,150,20))
        pygame.draw.rect(screen,"gray",(50,60,100,10))
        mp_ratio=self.magic/self.max_magic
        hp_ratio=self.healt/self.max_healt
        exp_ratio=self.exp/self.max_exp
        pygame.draw.rect(screen,"red",(50,10,200*hp_ratio,20))
        pygame.draw.rect(screen,"blue",(50,40,150*mp_ratio,20))
        pygame.draw.rect(screen,"yellow",(50,60,100*exp_ratio,10))
        font1=font.render(str(self.level),True,"white")
        font_rect=font1.get_frect()
        screen.blit(font1,(10,10))
        if self.exp>=100:
            self.exp=0
            self.level+=1
            self.max_healt+=40
            self.max_magic+=10
            self.healt=self.max_healt



    def spell(self):
        pos=self.rect.center
        keys=pygame.key.get_pressed()
        pygame.draw.rect(screen,"black",(50,620,80,80))
        magic_image=pygame.image.load(magic_data["fire"]["location"])
        magic_image_rect=magic_image.get_frect(topleft=(58,628))
        screen.blit(magic_image,magic_image_rect)
        pygame.draw.rect(screen,"black",(150,620,80,80))
        magic_image1=pygame.image.load(magic_data["heal"]["location"])
        magic_image_rect1=magic_image1.get_frect(topleft=(158,628))
        screen.blit(magic_image1,magic_image_rect1)
        if keys[pygame.K_r] and self.healt<100:
          self.magic-=10
          pygame.draw.rect(screen,"yellow",(150,620,80,80),width=5)

        
        if keys[pygame.K_e] and current_time - activ_time >= 600:
            self.magic-=10
            pygame.draw.rect(screen,"yellow",(50,620,80,80),width=5)
            p=power(pos,all_sprits,attack)
            spell.append(p)
            power.update(self)
            return True
    def damage(self):
        for e in en:
            if abs(self.rect.x-e.postion[0])<5 or abs(self.rect.y-e.postion[1])<5 :
                self.healt-=1





        



class enemy(pygame.sprite.Sprite):
        def __init__(self,pos,group,collision):
            super().__init__(group)
            self.image=pygame.image.load("C:/python-pracities/game/image/0.png").convert_alpha()
            self.rect=self.image.get_frect(center=pos)
            self.collision=collision
            self.hp=100
            self.postion=pygame.Vector2(self.rect.x,self.rect.y)
        
        def movement(self):
            self.direction=pygame.Vector2()
            self.direction.x=pl.rect.x-self.rect.x
            self.direction.y=pl.rect.y-self.rect.y

            self.direction=self.direction.normalize()



            self.rect.y += self.direction.y
            self.collision2("vertical")
            self.rect.x += self.direction.x
            self.collision2("horizantal")



        def collision2(self,direction):
            for sprit in self.collision:
                if sprit.rect.colliderect(self.rect):
                    if direction == "horizantal":
                        if self.direction.x > 0:self.rect.right=sprit.rect.left
                        if self.direction.x < 0:self.rect.left=sprit.rect.right
                    elif direction == "vertical":
                        if self.direction.y < 0:self.rect.top=sprit.rect.bottom
                        if self.direction.y > 0:self.rect.bottom=sprit.rect.top



    


class mapsprits(pygame.sprite.Sprite):#create the map
    def __init__(self,pos,surface,groups):
        super().__init__(groups)
        self.image=surface
        self.rect=self.image.get_frect(center=pos)

class power(pygame.sprite.Sprite):
    def __init__(self,pos,groups,attack):
        super().__init__(groups)
        self.image=pygame.image.load("C:/python-pracities/game/image/01.png")
        self.rect=self.image.get_frect(center=pos)
        self.mous=pygame.Vector2(pygame.mouse.get_pos())
        self.attack=attack

    def update(self):
        self.direction=pygame.Vector2()
        self.direction.x=wx/2- self.mous.x
        self.direction.y=wy/2- self.mous.y
        self.direction=-self.direction.normalize()
        self.rect.y += self.direction.y*3
        self.rect.x += self.direction.x*3
    def collision(self):
        for sprits in self.attack:
            if sprits.rect.colliderect(self.rect):
                sprits.hp=0






# pygame setup
activ_time=0
soot=False
wx=1280
wy=720
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((wx,wy))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
running = True
font=pygame.font.SysFont('arial',70)
spell=[]




all_sprits=allsprites()
collision_sprits=pygame.sprite.Group()
attack=pygame.sprite.Group()



tmx_data=load_pygame("C:/python-pracities/game/data/maps/world.tmx")#code for map tiles
jbhb=tmx_data.get_layer_by_name("ground")
for x,y,surf in jbhb.tiles():
    pos=(x*32,y*32)
    mapsprits(pos,surf,(all_sprits))
jbhb=tmx_data.get_layer_by_name("bolders")
for x,y,surf in jbhb.tiles():
    pos=(x*32,y*32)
    mapsprits(pos,surf,(all_sprits,collision_sprits))


pl=player(all_sprits,collision_sprits)#giving the player to all sprits 


jbh=tmx_data.get_layer_by_name("entity")#monster
en=[]
for i in jbh:
    pos=(i.x,i.y)
    e=enemy(pos,(all_sprits,attack),collision_sprits)
    en.append(e)
    



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
  
 
    screen.fill("black")
    pl.movement()#calling the movement
    all_sprits.draw(screen,pl.rect.center)#displaying player on the mainscreenww
    pl.bars()
    pl.damage()
    current_time=pygame.time.get_ticks()
    if pl.spell():
        activ_time=pygame.time.get_ticks()
    for e in en:
        if e.hp==0:
            en.pop(en.index(e))
            e.rect.center=(-1000,0)
            pl.exp=pl.exp+25
        e.movement()
    for i in spell:
        i.update()
        i.collision()
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()