import pygame,sys

pygame.init()
size=width,height=500,500
screen=pygame.display.set_mode(size)
color_b=(255,255,255)
background=pygame.Surface(screen.get_size())
game=True
clock=pygame.time.Clock()
print(type(screen))
counter=0
FPS=clock.tick(10)
pygame.display.set_caption("Mój licznik")
print(FPS)
font=pygame.font.Font(None,40)
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    
    background.fill(color_b)
    background=background.convert()
    screen.blit(background,(0,0))
    counter=counter+FPS/1000
    text=font.render("Timer: "+"{0:.2f}".format(counter) ,0,(55, 127, 4)).convert()
    screen.blit(text,(300,250))
    text=font.render("FPS: "+str(FPS),0,(55, 127, 4)).convert()
    screen.blit(text,(50,250))
    clock.tick(10)
    pygame.display.flip()

pygame.quit()
sys.exit()
