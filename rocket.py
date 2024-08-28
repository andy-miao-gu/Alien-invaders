import pygame

class AndyRocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [400, 300]

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def move(self, direction):
        if direction == "up":
            self.rect.y -= 5
        elif direction == "down":
            self.rect.y += 5
        elif direction == "left":
            self.rect.x -= 5
        elif direction == "right":
            self.rect.x += 5

    def update(self, keys):
        if keys[pygame.K_UP]:
            self.move("up")
        if keys[pygame.K_DOWN]:
            self.move("down")
        if keys[pygame.K_LEFT]:
            self.move("left")
        if keys[pygame.K_RIGHT]:
            self.move("right")

    def fire_bullet(self):
        

    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    rocket = AndyRocket()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        rocket.update(keys)

        screen.fill((255, 255, 255))
        rocket.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
