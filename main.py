import sys
import pygame as pg
import copy

class Snake:
    movement = 26
    
    def __init__(self,startingSpot):
        self.snakeHeadRect = startingSpot
        self.snakeHead = SnakeBlock(self.snakeHeadRect)
        self.wayToMove = self.moveRight
        
    def Draw(self,background):
        self.snakeHead.Draw(background)
        
    def Update(self):
        self.wayToMove()
        self.snakeHead.Update(self.snakeHeadRect)

    def moveRight(self):
        self.snakeHeadRect[0] += Snake.movement

    def moveLeft(self):
        self.snakeHeadRect[0] -= Snake.movement

    def moveUp(self):
        self.snakeHeadRect[1] -= Snake.movement

    def moveDown(self):
        self.snakeHeadRect[1] += Snake.movement

    def SetDirection(self, direction):
        if direction == pg.K_UP:
            self.wayToMove = self.moveUp
        if direction == pg.K_DOWN:
            self.wayToMove = self.moveDown
        if direction == pg.K_RIGHT:
            self.wayToMove = self.moveRight
        if direction == pg.K_LEFT:
            self.wayToMove = self.moveLeft

    def AddSegment(self):
        self.snakeHead.AddSegment()
        
class SnakeBlock:
    color = (255,0,0)
    
    def __init__(self,startingSpace):
        self.image = pg.Surface((25,25)).convert()
        self.rect = startingSpace # an array
        self.image.fill(SnakeBlock.color)
        self.nextBlock = None

    def Update(self, newPosition):
        if self.nextBlock:
            self.nextBlock.Update(copy.copy(self.rect))
        self.rect = newPosition
            
    def Draw(self,background):
        print(self.rect)
        background.blit(self.image, self.rect)
        if self.nextBlock:
            self.nextBlock.Draw(background)

    def AddSegment(self):
        if self.nextBlock:
            self.nextBlock.AddSegment()
        else:
            self.nextBlock = SnakeBlock(self.rect)

class Fruit:
    #TODO
        
def main():
    pg.init()
    screen_size = (521,521)
    screen = pg.display.set_mode(screen_size)
    color = (0,0,0)
    background = pg.Surface(screen.get_size()).convert()
    background.fill(color)
    pg.display.set_caption("Snake Game")
    clock = pg.time.Clock()
    inGame = True
    snake = Snake([1,1])
    counter = 0
    while inGame:
        clock.tick(8)
        #handle input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                inGame = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                inGame = False
            if event.type == pg.KEYDOWN:
                if event.key in (pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT):
                    snake.SetDirection(event.key)
        snake.Update()
        background.fill(color)
        snake.Draw(background)
        screen.blit(background, (0,0))
        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    main()
