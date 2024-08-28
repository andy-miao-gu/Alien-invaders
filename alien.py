# after interval of seocn move alien left and right
import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, speed,img_add):
        super().__init__()
        self.image = pygame.image.load(img_add)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.speed = speed


    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.speed *= -1
    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    x_locations = [100,200,300,400,500,600]
    aliens  = []
    alien_group = pygame.sprite.Group()
    for x in x_locations:
        alien = Alien(x, 100, 5,"alien.png")
        aliens.append(alien)
        alien_group.add(alien)
    for x in x_locations:
        alien = Alien(x, 200, 5,"alien2.png")
        aliens.append(alien)
        alien_group.add(alien)
    for x in x_locations:
        alien = Alien(x, 300, 5,"alien3.png")
        alien_group.add(alien)
        aliens.append(alien)
        
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        alien_group.draw(screen)
        alien_group.update()
        pygame.display.flip()
        clock.tick(60)
