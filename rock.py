import pygame
import sys

class BrickGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bricks = []
        sizex = 20
        sizey = 20
        boxs = [(100,250),(300,450),(500,650),(700,850)]
        for a,b in boxs:
            for x in range(a-75, b-75, 25):
                for y in range(400, 500, 30 ):
                    self.bricks.append(pygame.Rect(x, y, sizex, sizey))


    def draw_bricks(self):
        for brick in self.bricks:
            pygame.draw.rect(self.screen, (255, 0, 0), brick)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.draw_bricks()
            pygame.display.flip()

if __name__ == "__main__":
    BrickGame().run()
