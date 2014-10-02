#-------------------------------------------------------------------------------
# Name:        Froggy
# Purpose: Creates a game which is a simulation of the game Frogger.
#
# Author:      Sabastian Mugazambi
#
# Created:     28/05/2014
# Copyright:   (c) Sabastian Mugazambi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Note the use of the word Bullets to represent Cars.
import math
import time
import random
import sys
import pygame
import interfaces
import button
from pygame.locals import *

class Froggy:
    """This initiates the frog which the player is going to be moving around the screen. It also has all the capabilities of the frog."""

    def __init__(self,screen,back):
        self.back = back
        self.screen = screen
        self.frog= pygame.image.load("2frog.gif")
        self.frogrect = self.frog.get_rect().move(280,620)
        screen.blit(self.frog,self.frogrect)
        pygame.display.flip()

    def move(self,speed):
        #this function moves the frog according to the speed given and it also chacks if the frog is at the boundaries of the screen or not.
        if self.frogrect.bottom > 700:
             speed[1] = -speed[1]
        if self.frogrect.left < 0:
             speed[0] = -speed[0]
        if self.frogrect.right > 640 :
             speed[0] = -speed[0]
        self.screen.blit(self.back,self.frogrect,self.frogrect)
        pygame.display.flip()
        self.frogrect = self.frogrect.move(speed)
        self.screen.blit(self.back,self.frogrect,self.frogrect)
        self.screen.blit(self.frog,self.frogrect)
        pygame.display.flip()
        return self.frogrect

    def get_rect(self):
        #returns the rectange of the frog and will be used latter to check for certain conditions.
        return self.frogrect

    def player(self):
        #returns the image itself for manipulation and blitting latter.
        return self.frog

##    def hop(self):


class Bullets:
    """Cars == Bullets  : initially I thought of using bullets but I am now using cars, since the cars kill, I will keep the name bullet"""
    """This Bullets initiate all the cars being fired from all ends of the screen. It creates the cars by randomly
    choosing the car from a list of cars given. The list chosen depends on whether the cars are supposed to be going to the right or left."""

    def __init__(self,screen,back,x,y):
        self.screen = screen
        self.back = back

        if y == 530 or y == 370:
          items = ["1car.png","2car2.gif","4car4.gif","5car5.gif","8car8.gif","9car9.gif","10car10.gif","11car11.gif","12car12.gif","car1.gif","car3.gif","car13.gif","car7.gif"]
        else:
          items = ["1car1.gif","3car3.gif","car.png","car2.gif","car4.gif","car5.gif","car6.gif","car8.gif","car9.gif","car10.gif","car11.gif","car12.gif","13car13.gif"]

        ran = random.randrange(0,len(items))
        self.bullet = pygame.image.load(items[ran])
        self.bulletrect = self.bullet.get_rect().move(x,y)
        self.screen.blit(self.bullet,self.bulletrect)
        pygame.display.flip()

    def move(self,level):
        #moving the cars=bullets on the screen.
        speed = [-3*level,0]
        old_bulletrect = self.bulletrect
        self.bulletrect = self.bulletrect.move(speed)
        self.screen.blit(self.back,old_bulletrect,self.bulletrect)
        self.screen.blit(self.bullet,self.bulletrect)
        pygame.display.flip()


    def get_rect(self):
        #returns the rectangel of each car for future use.
        return self.bulletrect

    def bullet(self):
        #returns the image of the car itsself for latter purposes.
        return self.bullet


class Log:
    """This class initiates the logs that are flowing in the river. It also gives the logs capabilities to clip the frog when it gets in the same area."""

    def __init__(self,screen,back,x,y):
        self.screen = screen
        self.back = back
        self.log = pygame.image.load("log.png")
        self.logrect = self.log.get_rect().move(x,y)
        screen.blit(self.log,self.logrect)
        pygame.display.flip()

    def move(self,speed_log):
        #moves the logs from screen end to the other end as well
        old_logrect = self.logrect
        self.logrect = self.logrect.move(speed_log)
        self.screen.blit(self.back,old_logrect,self.logrect)
        self.screen.blit(self.log,self.logrect)
        pygame.display.flip()

    def get_rect(self):
        #returns the rectangle of the log for latter use
        return self.logrect

    def bullet(self):
        #returns the image of the log itsself.
        return self.log


def looped(level):
    """This function is the main loop of the game, it also creates images everytime so as to have cars contantly running through."""
    pygame.init()
    width, height = 640 , 700
    size = (width,height)
    screen = pygame.display.set_mode(size)

    back = pygame.image.load("Background.jpg")
    screen.blit(back,(0,0))
    pygame.display.flip()
    s = 0

    #creating instance objects of the frog and the cars and the logs
    player = Froggy(screen,back)

    bullet = Bullets(screen,back,200,530)
    bullet1 = Bullets(screen,back,410,530)
    bullet2 = Bullets(screen,back,620,530)
    bullet2_2 = Bullets(screen,back,830,530)

    bullet3_3 = Bullets(screen,back,-210,450)
    bullet3 = Bullets(screen,back,0,450)
    bullet4 = Bullets(screen,back,210,450)
    bullet5 = Bullets(screen,back,420,450)

    bullet6 = Bullets(screen,back,100,370)
    bullet7 = Bullets(screen,back,310,370)
    bullet8 = Bullets(screen,back,520,370)

    bullet9 = Bullets(screen,back,300,250)
    bullet10 = Bullets(screen,back,510,250)
    bullet11 = Bullets(screen,back,720,250)

    log1 = Log(screen,back,0,150)
    log2 = Log(screen,back,128,150)
    log3 = Log(screen,back,256,150)
    log4 = Log(screen,back,384,150)

    log5 = Log(screen,back,196,90)
    log6 = Log(screen,back,324,90)
    log7 = Log(screen,back,452,90)
    log8= Log(screen,back,580,90)


    speed = [0,-1*level]
    speed_log = [2*level,0]
    speed_log2 = [-2*level,0]

    while True:
    #Main while loop of the game that runs the game and constanty checks for various states. .
      log1.move(speed_log)
      log2.move(speed_log)
      log3.move(speed_log)
      log4.move(speed_log)
      log5.move(speed_log2)
      log6.move(speed_log2)
      log7.move(speed_log2)
      log8.move(speed_log2)


      bullet.move(level)
      bullet1.move(level)
      bullet2.move(level)
      bullet2_2.move(level)

      bullet3_3.move(-level)
      bullet3.move(-level)
      bullet4.move(-level)
      bullet5.move(-level)

      bullet6.move(level)
      bullet7.move(level)
      bullet8.move(level)

      bullet9.move(-level)
      bullet10.move(-level)
      bullet11.move(-level)

      if bullet2_2.get_rect().right < 0:
        #checking if the last car leaves the screen so as to fire another line of cars.

        bullet = Bullets(screen,back,640,530)
        bullet1 = Bullets(screen,back,850,530)
        bullet2 = Bullets(screen,back,1060,530)
        bullet2_2 = Bullets(screen,back,1270,530)

        bullet.move(level)
        bullet1.move(level)
        bullet2.move(level)
        bullet2_2.move(level)

      if bullet3_3.get_rect().left > 640:

        bullet3 = Bullets(screen,back,-420,450)
        bullet4 = Bullets(screen,back,-210,450)
        bullet5 = Bullets(screen,back,0,450)
        bullet3_3 = Bullets(screen,back,-630,450)

        bullet3_3.move(-level)
        bullet3.move(-level)
        bullet4.move(-level)
        bullet5.move(-level)

      if bullet8.get_rect().right < 0:

        bullet6 = Bullets(screen,back,640,370)
        bullet7 = Bullets(screen,back,850,370)
        bullet8 = Bullets(screen,back,1060,370)

        bullet6.move(level)
        bullet7.move(level)
        bullet8.move(level)

      if bullet9.get_rect().left > 640:

        bullet9 = Bullets(screen,back,-420,250)
        bullet10 = Bullets(screen,back,-210,250)
        bullet11 = Bullets(screen,back,0,250)

        bullet9.move(-level)
        bullet10.move(-level)
        bullet11.move(-level)

      if log4.get_rect().right >640 or log1.get_rect().left < 0:
        #bouncing the logs from screen to screen.
        speed_log[0] = -speed_log[0]
        log1.move(speed_log)
        log2.move(speed_log)
        log3.move(speed_log)
        log4.move(speed_log)

      if log8.get_rect().right > 640 or log5.get_rect().left < 0:
        speed_log2[0] = -speed_log2[0]
        log5.move(speed_log2)
        log6.move(speed_log2)
        log7.move(speed_log2)
        log8.move(speed_log2)

      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == KEYDOWN:
            if event.key == K_q:
               pygame.quit()
               sys.exit()
            elif event.key == K_UP :
               speed[1] -= level
               speed[0] = 0
               s += 10
            elif event.key == K_DOWN :
               speed[1] += level
               speed[0] = 0
               s += 10
            elif event.key == K_LEFT :
                speed[0] -= level
                speed[1] = 0
                s +=10
            elif event.key == K_RIGHT :
                speed[0] += level
                speed[1] = 0
                s += 10

      #ending the game if the frog and any of the cars collide.
      if player.get_rect().colliderect(bullet.get_rect()) or player.get_rect().colliderect(bullet1.get_rect()) or player.get_rect().colliderect(bullet2.get_rect()) or player.get_rect().colliderect(bullet3.get_rect()) or player.get_rect().colliderect(bullet3_3.get_rect()) or player.get_rect().colliderect(bullet4.get_rect()):
        over = pygame.image.load("over.gif")
        screen.blit(over,(0,0))
        pygame.display.flip()
        return False


      if player.get_rect().colliderect(bullet5.get_rect()) or player.get_rect().colliderect(bullet6.get_rect()) or player.get_rect().colliderect(bullet7.get_rect()) or player.get_rect().colliderect(bullet8.get_rect()):
        over = pygame.image.load("over.gif")
        screen.blit(over,(0,0))
        pygame.display.flip()
        return False


      if player.get_rect().colliderect(bullet9.get_rect()) or player.get_rect().colliderect(bullet10.get_rect()) or player.get_rect().colliderect(bullet11.get_rect()) or player.get_rect().colliderect(bullet2_2.get_rect()) or player.get_rect().colliderect(bullet3_3.get_rect())  :
        over = pygame.image.load("over.gif")
        screen.blit(over,(0,0))
        pygame.display.flip()
        return False

      if player.get_rect().top <= 200:
          #getting the frog into hopping mode where it hopes on to the log when up button is clicked.
          speed = [0,0]
        #Main while loop of the game that runs the game and constanty checks for various states. .
          log1.move(speed_log)
          log2.move(speed_log)
          log3.move(speed_log)
          log4.move(speed_log)
          log5.move(speed_log2)
          log6.move(speed_log2)
          log7.move(speed_log2)
          log8.move(speed_log2)


          bullet.move(level)
          bullet1.move(level)
          bullet2.move(level)
          bullet2_2.move(level)

          bullet3_3.move(-level)
          bullet3.move(-level)
          bullet4.move(-level)
          bullet5.move(-level)

          bullet6.move(level)
          bullet7.move(level)
          bullet8.move(level)

          bullet9.move(-level)
          bullet10.move(-level)
          bullet11.move(-level)

          if bullet2_2.get_rect().right < 0:
            #checking if the last car leaves the screen so as to fire another line of cars.

            bullet = Bullets(screen,back,640,530)
            bullet1 = Bullets(screen,back,850,530)
            bullet2 = Bullets(screen,back,1060,530)
            bullet2_2 = Bullets(screen,back,1270,530)

            bullet.move(level)
            bullet1.move(level)
            bullet2.move(level)
            bullet2_2.move(level)

          if bullet3_3.get_rect().left > 650:

            bullet3 = Bullets(screen,back,-420,450)
            bullet4 = Bullets(screen,back,-210,450)
            bullet5 = Bullets(screen,back,0,450)
            bullet3_3 = Bullets(screen,back,-630,450)

            bullet3_3.move(-level)
            bullet3.move(-level)
            bullet4.move(-level)
            bullet5.move(-level)

          if bullet8.get_rect().right < 0:

            bullet6 = Bullets(screen,back,640,370)
            bullet7 = Bullets(screen,back,850,370)
            bullet8 = Bullets(screen,back,1060,370)

            bullet6.move(level)
            bullet7.move(level)
            bullet8.move(level)

          if bullet9.get_rect().left > 640:

            bullet9 = Bullets(screen,back,-420,250)
            bullet10 = Bullets(screen,back,-210,250)
            bullet11 = Bullets(screen,back,0,250)

            bullet9.move(-level)
            bullet10.move(-level)
            bullet11.move(-level)

          if log4.get_rect().right >640 or log1.get_rect().left < 0:
            #bouncing the logs from screen to screen.
            speed_log[0] = -speed_log[0]
            log1.move(speed_log)
            log2.move(speed_log)
            log3.move(speed_log)
            log4.move(speed_log)

          if log8.get_rect().right > 640 or log5.get_rect().left < 0:
            speed_log2[0] = -speed_log2[0]
            log5.move(speed_log2)
            log6.move(speed_log2)
            log7.move(speed_log2)
            log8.move(speed_log2)

          for event in pygame.event.get():
             if event.type == QUIT:
                pygame.quit()
                sys.exit()
             elif event.type == KEYDOWN:
                if event.key == K_q:
                   pygame.quit()
                   sys.exit()
                elif event.key == K_UP :
                   speed[1] = -50
                   speed[0] = 0
                   s += 10
                elif event.key == K_DOWN :
                   speed[1] = +50
                   speed[0] = 0
                   s += 10
                elif event.key == K_LEFT :
                    speed[0] = -level*10
                    speed[1] = 0
                    s +=10
                elif event.key == K_RIGHT :
                    speed[0] = level*10
                    speed[1] = 0
                    s += 10

          if player.get_rect().top < 0 :
            print "You win"
            s += 2000
            winner = pygame.image.load("winner-b2.png")
            screen.blit(winner,(0,0))
            pygame.display.flip()
            return True


      player.move(speed)


def main():
    pygame.init()
    width, height = 640 , 700
    size = (width,height)
    screen = pygame.display.set_mode(size)
    back = pygame.image.load("start.png")
    screen.blit(back,(0,0))
    pygame.display.flip()

    time.sleep(2)

    level = 1
    previous = looped(level)

    #checking whether the player has lost or won the game then entering a new level or retrying from level one.
    while True:
        if previous == False:
          for event in pygame.event.get():
             if event.type == QUIT:
                pygame.quit()
                sys.exit()
             elif event.type == KEYDOWN:
                if event.key == K_q:
                   pygame.quit()
                   sys.exit()
                if event.key == K_r:
                    main()

        else:
           for event in pygame.event.get():
                 if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                 elif event.type == KEYDOWN:
                    if event.key == K_q:
                       pygame.quit()
                       sys.exit()
                    if event.key == K_c:
                        level += 1
                        looped(level)
                    if event.key == K_r:
                        main()














if __name__ == '__main__':
    main()
