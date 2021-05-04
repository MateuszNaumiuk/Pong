import pygame
from charact import Rat
from ball import Ball
pygame.init()

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#scores
scoreA = 0
scoreB = 0
 
# main settings
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

#characters
charact1 = Rat(WHITE, 2, 100)
charact1.rect.x = 20
charact1.rect.y = 200
charact2 = Rat(WHITE, 2, 100)
charact2.rect.x = 770
charact2.rect.y = 200
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

#sprites
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(charact1)
all_sprites_list.add(charact2)
all_sprites_list.add(ball)



#start main game loop
MAINLOOP = True
while MAINLOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              MAINLOOP = False

    #backplan
    screen.fill(BLACK)
    for i in range(0, 600, 20):
        pygame.draw.line(screen, WHITE, [400, i+10], [400, i], 1)

    #ball bounce from playermodels
    if pygame.sprite.collide_mask(ball, charact1) or pygame.sprite.collide_mask(ball, charact2):
        ball.bounce()

    #scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (255,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (525,10))

    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        charact1.movePlus(5)
    elif keys[pygame.K_s]:
        charact1.moveMinus(5)
    if keys[pygame.K_UP]:
        charact2.movePlus(5)
    elif keys[pygame.K_DOWN]:
        charact2.moveMinus(5)    
 
    all_sprites_list.update()
 
    #ball move
    if ball.rect.x>=790:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 

    all_sprites_list.draw(screen) 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()