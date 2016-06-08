import pygame


pygame.init()

screen = pygame.display.set_mode((600,600))

logo = pygame.image.load("images/system/icon.png").convert()
clock = pygame.time.Clock()
iconWID = 32
iconHEI = 32

 #fade in the logo
for i in range(255): 
    screen.fill((0,0,0))
    logo.set_alpha(i)
    logo2 = pygame.transform.smoothscale(logo, (iconWID+i, iconHEI+i))
    screen.blit(logo2, (0,0))
    pygame.display.update()
    clock.tick(200)

 #fade in the logo
for i in range(255): 
    screen.fill((0,0,0))
    logo2 = pygame.transform.smoothscale(logo, (32+255, 32+255))
    logo2.set_alpha(255-i)
    screen.blit(logo2, (0, 0))
    pygame.display.update()
    clock.tick(500)


##screen.blit(logo, (0, 0))
##pygame.display.update()
##
##pygame.time.delay(2000)
##
##pygame.transform.smoothscale(logo, (50, 50))
##pygame.display.update()


while 1:

    for event in pygame.event.get():

        #If the program is closed, exit:
        if event.type == pygame.QUIT:
            pygame.quit()


##
##
##bkg1 = pygame.Surface((500, 500))
##bkg2 = pygame.Surface((400, 400))
##
##
##bkg1.fill((255, 0, 0, 255))
##bkg2.fill((0, 0, 255, 255))
##
##bkg1.convert_alpha()
##bkg2.convert_alpha()
##
##bkg1.set_alpha(255)
##bkg2.set_alpha(255)
##
##screen.fill((0, 255, 0, 255))
##
##pygame.display.update()
##
##pygame.time.delay(2000)
##
##screen.blit(bkg1, (25, 25))
##
##pygame.display.update()
##
##pygame.time.delay(2000)
##
##screen.blit(bkg2, (50, 50))
##
##pygame.display.update()
##
##pygame.time.delay(2000)
##
##bkg2.set_alpha(0)
##
##print bkg2.get_alpha()
##
##screen.blit(bkg2, (50, 50))
##
##pygame.display.update()
