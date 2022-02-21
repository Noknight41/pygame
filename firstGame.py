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

#Variable
x = 50
y = 400
width = 64
height = 64
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

# Redraw
def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
    pygame.display.update()

# Main Loop
run = True
while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    # Movement and Boundaries
    if keys[pygame.K_LEFT] and x > vel:
        x = x - vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < sw - vel - width:
        x = x + vel
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump): # Disabled when jump
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y = y - neg * (jumpCount ** 2) * 0.5
            jumpCount = jumpCount - 1
        else:
            isJump = False
            jumpCount = 10
    redrawGameWindow()

pygame.quit()