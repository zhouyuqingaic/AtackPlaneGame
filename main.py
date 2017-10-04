
import pygame.locals as locals

import pygame
import time

class Bullet:
    def __init__(self,screen_temp,x,y):
        self.x=x+60
        self.y=y-60
        self.screen=screen_temp
        self.image=pygame.image.load("./images/bullet.jpg")
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y-=17
    def judge(self):
        if self.y<=0:
            return True
class EnemyBullet:
    def __init__(self,screen_temp,x,y):
        self.x=x+60
        self.y=y+60
        self.screen=screen_temp
        self.image=pygame.image.load("./images/bullet.jpg")
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y+=10
    def judge(self):
        if self.y>=850:
            return True

class PlayerPlane:
    def __init__(self,screen_temp):
        self.x=250
        self.y=700
        self.screen=screen_temp
        self.image=pygame.image.load("./images/spaceShip.jpeg")
        self.bullet_list=[]
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        print("Paly Bullet Len:{}".format(len(self.bullet_list)))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
    def move_left(self):
        if self.x>35:
            self.x-=35
    def move_right(self):
        if self.x<530:
            self.x+=35
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class EnemyPlane:
    def __init__(self,screen_temp):
        self.x=50
        self.y=90
        self.screen=screen_temp
        self.image=pygame.image.load("./images/EnemyPlane.jpg")
        self.bullet_list=[]
        self.direction="right"
        self.last_fire_time=None
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        print("Enemy Bullet Len:{}".format(len(self.bullet_list)))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5

    def move(self):
        if self.direction=="right":
            self.move_right()
        elif self.direction=="left":
            self.move_left()

        if self.x>(600-50):
            self.direction="left"
        elif self.x<(50):
            self.direction="right"

    def fire(self):
        if not self.last_fire_time:
            self.last_fire_time=int(time.time())
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
        #冷却时间 1 seconds
        elif self.last_fire_time<int(time.time()-1):
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
            self.last_fire_time=int(time.time())
        else:
            pass

def key_control(player_plane):
    for event in pygame.event.get():
        if event.type==locals.QUIT:
            print("EXIT GAME")
            exit()
        elif event.type==locals.KEYDOWN:
            if event.key==locals.K_a or event.key==locals.K_LEFT:
                print("<---left")
                player_plane.move_left()
            elif event.key==locals.K_d or event.key==locals.K_RIGHT:
                print("right-->")
                player_plane.move_right()
            elif event.key==locals.K_SPACE:
                print("--->SPACE<---")
                player_plane.fire()
            else:
                pass
        else:
            pass
def main():
    screen=pygame.display.set_mode((600,850),0,32)

    background=pygame.image.load("./images/BackGround_NASA_01.jpg")
    player_plane=PlayerPlane(screen)
    enemy_plane=EnemyPlane(screen)

    while True:
        screen.blit(background,(0,0))
        player_plane.display()
        enemy_plane.fire()
        enemy_plane.display()
        pygame.display.update()
        key_control(player_plane)
        enemy_plane.move()
        time.sleep(0.01)

if __name__=="__main__":
    main()
