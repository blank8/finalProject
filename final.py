from pygame.locals import *
import pygame

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16,)

    def move(self, dx, dy):
        
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: 
                    self.rect.right = wall.rect.left
                if dx < 0: 
                    self.rect.left = wall.rect.right
                if dy > 0: 
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

class Wall(object):
    def __init__(self, pos):
       walls.append(self)
       self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

pygame.init()

pygame.display.set_caption("FinalProject")
screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()
walls = []
player = Player()

level = [
"                    ",
"WWWWWWWWWWWWWWWWW  W",
"W        WWWE      W",
"W WW  WW   WWW  WWWW",
"W  WW        W  WWWW",
"WW  WW  WWWWWWW    W",
"W   WWW    WWW      ",
"WW  WWWWWW    WWW  W",
"WW  WW   WW WWWW   W",
"WWW WWWW         WWW",
"WWW    WWWWW  W   WW",
"WW  WWWWWWW   WWWWWW",
"W    WWWWWWWW    WWW",
]

x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
        
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
        
    if key[pygame.K_UP]:
        player.move(0, -2)
        
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    if player.rect.colliderect(end_rect):
        raise SystemExit; "You win!"
    
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.flip()

if __name__ == "__main__":
    App = App()
    App.on_execute()
