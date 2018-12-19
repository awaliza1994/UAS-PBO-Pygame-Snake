import pygame
import sys
import random
import time

class Snake():
    def __init__(self):
        self.posotion = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def changeDirTo(self,dir): #perubahan gerak agar tidak kembali arah yang berjalan
        if dir=="RIGHT" and not self.direction=="LEFT":
            self.direction = "RIGHT"
        if dir=="LEFT" and not self.direction=="RIGHT":
            self.direction = "LEFT"
        if dir=="UP" and not self.direction=="DOWN":
            self.direction = "UP"
        if dir=="DOWN" and not self.direction=="UP":
            self.direction = "DOWN"

    def move(self,foodPos): #loncatan ular dan tubih ular yang mrngikuti
        if self.direction == "RIGHT":
            self.posotion[0] += 10
        if self.direction == "LEFT":
            self.posotion[0] -= 10
        if self.direction == "UP":
            self.posotion[1] -= 10
        if self.direction == "DOWN":
            self.posotion[1] += 10
        self.body.insert(0,list(self.posotion))
        if self.posotion ==foodPos:
            return 1
        else:
            self.body.pop()
            return 0

    def checkCollision(self): #posisi ular keluar ruang
        if self.posotion[0] > 490 or self.posotion[0]< 0:
            return 1
        elif self.posotion[1] > 490 or self.posotion[1]<0:
            return 1
        for bodyPart in self.body[1:]:
            if self.posotion[0] == bodyPart:
                return 1
            return 0

    def getHeadPos(self):
        return  self.posotion
    def getBody(self):
        return  self.body


class FoodSpawer(): #untuk makanannya, kecepatan gerak, kondisi game berakhir dll
    def __init__(self):
        self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,50) * 10, random.randrange(1,50)*10]
            self.isFoodOnScreen = True
        return self.position
    def setFoodOnScreen(self,b):
        self.isFoodOnScreen = b

#tampilan pixel kecepatan gerak
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Ular Memanjang")
fps = pygame.time.Clock()
score = 0 #score
snake = Snake()
foodSpawner =FoodSpawer()

def gameOver(): #game berakhir 
    pygame.quit()
    sys.exit()

while True: #jika memakan tambah memanjang, fungsi gerak, penepatan kecepatan FPS
    FoodPos = foodSpawner.spawnFood()
    if(snake.move(FoodPos)== 1):
        score += 1 #tambah score
        foodSpawner.setFoodOnScreen(False)

    window.fill(pygame.Color(200,225,225))
    for pos in snake.getBody():
        pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(window, pygame.Color(225,0, 0), pygame.Rect(FoodPos[0],FoodPos[1], 10, 10))
    if(snake.checkCollision()== 1):
        gameOver()
    pygame.display.set_caption("Ular Memanjang | Score :"+str(score)) #tampilan score
    pygame.display.flip()
    fps.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver();
        elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
            snake.changeDirTo("RIGHT")
           if event.key == pygame.K_UP:
            snake.changeDirTo("UP")
           if event.key == pygame.K_DOWN:
            snake.changeDirTo('DOWN')
           if event.key == pygame.K_LEFT:
            snake.changeDirTo('LEFT')
