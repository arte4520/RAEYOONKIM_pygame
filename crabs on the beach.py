import os
import random
import pygame
import time
from pygame.locals import *

pygame.mixer.init()
pygame.init()

class Tennis():
    def __init__(self):
        self.width = 20
        self.height = 20
        self.x = 500
        self.y = 400
        self.change_x = 10
        self.change_y = 10
        self.score = 0

    def draw(self):
        self.image = pygame.image.load('tennis.png')
        screen.blit(self.image, (self.x, self.y))


    def mv(self):
        self.x += self.change_x
        self.y += self.change_y

    def update(self):
            if self.y <= 0:
                self.change_y *= -1
            elif self.y >= 690:
                self.change_y *= -1

            if self.x <= 70 and self.x >= 50 and self.y >= mine.y and self.y < (mine.y + mine.height):
                self.change_x *= -1
                self.score += 1
            elif self.x >= 890 and self.x <= 900 and self.y >= com.y and self.y < (com.y + com.height):
                self.change_x *= -1

            if self.x <= 0 and com.score != 4:
                losescore.play()
                com.score += 1
                self.x = 500
                self.y = 400
                self.change_x *= -1

            if self.x >= 1000 and mine.score != 4:
                winscore.play()
                mine.score += 1
                self.x = 500
                self.y = 400
                self.change_x *= -1

            if mine.score == 4:
                win.play()

            if com.score == 4:
                lose.play()


class crab():
    def __init__(self):
        self.width = 20
        self.height = 150
        self.x = 0
        self.y = 10
        self.color = white
        self.score = 0

    def draw1(self):
        self.image = pygame.image.load('crab1.png')
        screen.blit(self.image, (self.x, self.y))

    def draw2(self):
        self.image = pygame.image.load('crab2.png')
        screen.blit(self.image, (self.x, self.y))


def drawobj(obj, x, y):
    screen.blit(obj, (x, y))

def reset():
      stage = 0
      ball.x = 440
      ball.y = 340
      mine.score = 0
      com.score = 0

def result(re, minescore, comscore):
    result = font80.render(re,True,blue)
    finaltext = font30.render(str(mine.score) + ":" + str(com.score),True,black)
    screen.blit(finaltext,(400,200))
    screen.blit(result,(400,300))

def startprint():
    title = font80.render("Crabs on the beach", True, red)
    howto = font70.render("Press the space bar", True, kaki)
    screen.blit(title, [100, 100])
    screen.blit(howto, [150, 200])

def endprint():
    endt = font20.render("Try again !", True, kaki)
    endp = font30.render("Press the space bar", True, red)
    screen.blit(endp, [50, 600])
    screen.blit(endt, [50, 650])


def stageprint(n):
    stages = ['STAGE 1','STAGE 2','STAGE 3','LAST STAGE']
    st = font70.render(stages[n-1], True, kaki)
    screen.blit(st, [350, 350])

size=(1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Crabs on the beach')
pygame.key.set_repeat(1, 1)
bg = pygame.image.load("beach.png")
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
blue = (0, 0, 150)
kaki = (148, 139, 111)
red = (150, 0, 0)

font20 = pygame.font.Font("SSShinb7Regular.ttf",20)
font30 = pygame.font.Font("SSShinb7Regular.ttf",30)
font70 = pygame.font.Font("SSShinb7Regular.ttf",70)
font80 = pygame.font.Font("SSShinb7Regular.ttf",80)

text_0= font80.render("0", True, kaki)
text_1= font80.render("1", True, kaki)
text_2 = font80.render("2", True, kaki)
text_3 = font80.render("3", True, kaki)

ball = Tennis()
mine = crab()
mine.x = 40
com = crab()
com.x = 900

waterwave = pygame.mixer.Sound("waterwave.wav")
waterwave.set_volume(0.1)
waterwave.play(-1)
bgm = pygame.mixer.Sound("bgm.wav")
bgm.set_volume(0.05)
bgm.play(-1)

winscore = pygame.mixer.Sound("winscore.wav")
losescore = pygame.mixer.Sound("losescore.wav")
win = pygame.mixer.Sound("win.wav")
lose = pygame.mixer.Sound("lose.wav")
winscore.set_volume(0.1)
win.set_volume(0.1)
losescore.set_volume(0.1)
lose.set_volume(0.1)

stage = 0

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if stage == 0:
                    stage = 1
                elif stage == 2:
                    reset()
                    stage = 1
                else:
                    reset()
                    stage == 1

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    drawobj(bg, 0, 0)

    if stage == 0:
        startprint()

    elif stage == 1:

        if mine.score == 0:
            screen.blit(text_0, [370, 30])
            stageprint(1)
            crabmove = random.randrange(1,33)

        elif mine.score == 1:
            screen.blit(text_1, [370, 30])
            stageprint(2)
            crabmove = random.randrange(1,27)

        elif mine.score == 2:
            screen.blit(text_2, [370, 30])
            stageprint(3)
            crabmove = random.randrange(1,21)
        elif mine.score == 3:
            screen.blit(text_3, [370, 30])
            stageprint(4)
            crabmove = random.randrange(1,15)

        elif mine.score == 4:
            stage = 2

        if com.score == 0:
            screen.blit(text_0, [570, 30])

        elif com.score == 1:
            screen.blit(text_1, [570, 30])

        elif com.score == 2:
            screen.blit(text_2, [570, 30])

        elif com.score == 3:
            screen.blit(text_3, [570, 30])

        elif com.score == 4:
            stage = 2

        ball.draw()
        ball.mv()
        ball.update()

        mine.draw1()
        mine.y = mouse_y - 75

        com.draw2()
        com.y = ball.y - 130 - crabmove

    elif stage == 2:
        if mine.score == 4:
            re = "WIN"

        if com.score == 4:
            re = "LOSE"

        result(re, mine.score, com.score)
        endprint()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
