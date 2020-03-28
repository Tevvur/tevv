import pygame
size = wight, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.init()
screen.fill((255, 255, 255))
for point in range(0,501,100):# range(start, stop, step)
   pygame.draw.line(screen, (point/2,point/2,point/2), (point, 0), (point, 500), 100)
for point in range(0,641,64): # range(start, stop, step)
   pygame.draw.line(screen, (255,0,255), (0,0), (500, point), 1)
   pygame.draw.line(screen, (255,0,255), (500,0), (0, point), 1)
   pygame.draw.line(screen, (255, 0, 255), (0, 500), (500, point), 1)
   pygame.draw.line(screen, (255, 0, 255), (500, 500), (0, point), 1)
pygame.draw.circle(screen, (255,20,147), (250, 250), 150)
pygame.draw.polygon(screen, (0,180,0), ((255,105),(289,205),(395,205),(311,269),(345,375),(255,310),(165,375),(199,269),(115,205),(221,205)))
pygame.draw.polygon(screen, (255,20,147),((224,209),(286,209),(306,267),(255,305),(204,267)))
pygame.draw.polygon(screen, (255,20,147),((255,112),(285,205),(225,205)))
pygame.draw.polygon(screen, (255,20,147),((291,209),(385,209),(310,265)))
pygame.draw.polygon(screen, (255,20,147),((219,209),(125,209),(200,265)))
pygame.draw.polygon(screen, (255,20,147),((259,309),(308,273),(339,365)))
pygame.draw.polygon(screen, (255,20,147),((251,309),(202,273),(171,365)))
pygame.draw.arc(screen, (0,255,0),(0,0,500,500),4.71, 0) 
clock = pygame.time.Clock()
mainloop = True
FPS = 30 
playtime = 0.0
while mainloop:
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False 
    pygame.display.set_caption("Frame rate: {:0.2f} frames per second." 
                               " Playtime: {:.2} seconds".format(
                               clock.get_fps(),playtime))
    pygame.display.flip()      
print("this 'game' was played for %.2f seconds" % playtime)