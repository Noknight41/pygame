# 
import pygame
pygame.init()

# Screen
sw = 500
sh = 480
win = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("First Game")

asset = """Asset#1/"""
#Sprite
walkRight = [pygame.image.load(asset + 'R1.png'), pygame.image.load(asset + 'R2.png'), pygame.image.load(asset + 'R3.png'), pygame.image.load(asset + 'R4.png'), pygame.image.load(asset + 'R5.png'), pygame.image.load(asset + 'R6.png'), pygame.image.load(asset + 'R7.png'), pygame.image.load(asset + 'R8.png'), pygame.image.load(asset + 'R9.png')]
walkLeft = [pygame.image.load(asset + 'L1.png'), pygame.image.load(asset + 'L2.png'), pygame.image.load(asset + 'L3.png'), pygame.image.load(asset + 'L4.png'), pygame.image.load(asset + 'L5.png'), pygame.image.load(asset + 'L6.png'), pygame.image.load(asset + 'L7.png'), pygame.image.load(asset + 'L8.png'), pygame.image.load(asset + 'L9.png')]
bg = pygame.image.load(asset + 'bg.jpg')
char = pygame.image.load(asset + 'standing.png')

clock = pygame.time.Clock()
score = 0

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.airBorne = False
        self.left = False
        self.right = True
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 50)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 50)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    
    def moveLeft(self):
        self.x = self.x - self.vel
        self.left = True
        self.right = False
        self.standing = False
        
    def moveRight(self):
        self.x = self.x + self.vel
        self.left = False
        self.right = True
        self.standing = False
        
    def stand(self):
        self.walkCount = 0
        self.standing = True
    
    def jumpInit(self):
        self.airBorne = True
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

class enemy(object):
    walkRight = [pygame.image.load(asset + 'R1E.png'), pygame.image.load(asset + 'R2E.png'), pygame.image.load(asset + 'R3E.png'), pygame.image.load(asset + 'R4E.png'), pygame.image.load(asset + 'R5E.png'), pygame.image.load(asset + 'R6E.png'), pygame.image.load(asset + 'R7E.png'), pygame.image.load(asset + 'R8E.png'), pygame.image.load(asset + 'R9E.png'), pygame.image.load(asset + 'R10E.png'), pygame.image.load(asset + 'R11E.png')]
    walkLeft =  [pygame.image.load(asset + 'L1E.png'), pygame.image.load(asset + 'L2E.png'), pygame.image.load(asset + 'L3E.png'), pygame.image.load(asset + 'L4E.png'), pygame.image.load(asset + 'L5E.png'), pygame.image.load(asset + 'L6E.png'), pygame.image.load(asset + 'L7E.png'), pygame.image.load(asset + 'L8E.png'), pygame.image.load(asset + 'L9E.png'), pygame.image.load(asset + 'L10E.png'), pygame.image.load(asset + 'L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 36, 57)
        self.health = 10
        self.visible = True
    
    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 10, self.y, 40, 57)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 127, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (50 / 10) * (10 - self.health), 10))
            
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        
    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = - self.vel
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = - self.vel
                self.walkCount = 0
    
    def hit(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
            self.visible = False

class projectile(object):
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 8 * direction
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        
class bulletBar(object):
    def __init__(self, x, y, maxNo, radius, color, gap):
        self.x = x
        self.y = y
        self.number = maxNo
        self.maxNo = maxNo
        self.radius = radius
        self.color = color
        self.gap = gap

    def draw(self, win):
        for i in range(0, self.number):
            pygame.draw.circle(win, self.color, (self.x + i * self.gap, self.y), self.radius)
      
# Redraw
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    bb.draw(win)
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (340, 10))
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# Main Loop
font = pygame.font.SysFont('comicsans', 30, True) 
man = player(300, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
bullets = []
CD = 0
bb = bulletBar(20, 20, 5, 10, (0, 0, 0), 30)
run = True
while run:
    clock.tick(27)
    
    if CD > 0:
        CD += 1
    if CD > 5:
        CD = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
                bb.number += 1
        if bullet.x > 0 and bullet.x < 500:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            bb.number += 1
    
    keys = pygame.key.get_pressed()
    
    # Shooting bullets
    if keys[pygame.K_SPACE] and CD == 0:
        CD = 1
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bb.number -= 1
            bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0, 0, 0), facing))
        
    
    # Movement and Boundaries
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.moveLeft()
    elif keys[pygame.K_RIGHT] and man.x < sw - man.vel - man.width:
        man.moveRight()
    else:
        man.stand()
    if not(man.airBorne): # Disabled when jump
        if keys[pygame.K_UP]:
            man.jumpInit()
    else:
        man.jump()
    redrawGameWindow()

pygame.quit()