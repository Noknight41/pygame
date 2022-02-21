# 
import pygame
pygame.init()

# Screen
sw = 500
sh = 500
win = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("First Game")

asset = """Asset#1/"""
#Sprite
walkRight = [pygame.image.load(asset + 'R1.png'), pygame.image.load(asset + 'R2.png'), pygame.image.load(asset + 'R3.png'), pygame.image.load(asset + 'R4.png'), pygame.image.load(asset + 'R5.png'), pygame.image.load(asset + 'R6.png'), pygame.image.load(asset + 'R7.png'), pygame.image.load(asset + 'R8.png'), pygame.image.load(asset + 'R9.png')]
walkLeft = [pygame.image.load(asset + 'L1.png'), pygame.image.load(asset + 'L2.png'), pygame.image.load(asset + 'L3.png'), pygame.image.load(asset + 'L4.png'), pygame.image.load(asset + 'L5.png'), pygame.image.load(asset + 'L6.png'), pygame.image.load(asset + 'L7.png'), pygame.image.load(asset + 'L8.png'), pygame.image.load(asset + 'L9.png')]
bg = pygame.image.load(asset + 'bg.jpg')
char = pygame.image.load(asset + 'standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.airBorne = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    
    def moveLeft(self):
        self.x = self.x - self.vel
        self.left = True
        self.right = False
        
    def moveRight(self):
        self.x = self.x + self.vel
        self.left = False
        self.right = True
        
    def stand(self):
        self.right = False
        self.left = False
        self.walkCount = 0
    
    def jumpInit(self):
        self.airBorne = True
        self.right = False
        self.left = False
        self.walkCount = 0
    
    def jump(self):
        if self.jumpCount >= -10:
            neg = 1
            if self.jumpCount < 0:
                neg = -1
            self.y = self.y - neg * (self.jumpCount ** 2) * 0.5
            self.jumpCount = self.jumpCount - 1
        else:
            self.airBorne = False
            self.jumpCount = 10
            
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))
        
# Redraw
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    pygame.display.update()

# Main Loop
man = player(300, 410, 64, 64)
run = True
while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    # Movement and Boundaries
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.moveLeft()
    elif keys[pygame.K_RIGHT] and man.x < sw - man.vel - man.width:
        man.moveRight()
    else:
        man.stand()
    if not(man.airBorne): # Disabled when jump
        if keys[pygame.K_SPACE]:
            man.jumpInit()
    else:
        man.jump()
    redrawGameWindow()

pygame.quit()