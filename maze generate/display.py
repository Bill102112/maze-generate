import pygame
import sys
import maze
l = maze.l
alist = maze.alist
a = maze.a
b = maze.b
pygame.init()
pygame.display.set_icon(pygame.image.load("迷宮.png"))
screen=pygame.display.Info()
screen = pygame.display.set_mode((l*(2*a+1),l*(2*b+1)))
pygame.display.set_caption('maze')
screen.fill("white")
c = pygame.Surface((l, l), flags=pygame.HWSURFACE)
c.fill(color='white')
d = pygame.Surface((l, l), flags=pygame.HWSURFACE)
d.fill(color='black')
f = pygame.Surface((l, l), flags=pygame.HWSURFACE)
f.fill(color='white')
for i in range(2*a+1):
    for j in range(2*b+1):
        if alist[i][j]==0:
            screen.blit(c, (i*l, j*l))
        elif alist[i][j]==1:
            screen.blit(d, (i*l, j*l))
        else:
            screen.blit(f,(i*l, j*l))
pygame.display.flip()
aaaaaaa = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
            pygame.display.flip()
            
pygame.display.flip()

