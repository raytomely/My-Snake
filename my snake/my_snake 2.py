import pygame,sys,random,math
from pygame.locals import *

pygame.init()

#Open Pygame window
screen = pygame.display.set_mode((640, 480),) #add RESIZABLE or FULLSCREEN
#Title
pygame.display.set_caption("my snake")
color=pygame.color.THECOLORS["black"]
font=pygame.font.SysFont('Arial', 30)  

step=20
up=(0,-step)
down=(0,step)
left=(-step,0)
right=(step,0)
direction=left
timer=0
speed_limiter=5
game_over=0
score=0

#make image
snake=pygame.Surface((20,20)).convert()
snake.set_colorkey(snake.get_at((0,0)))
pygame.draw.circle(snake,(0,255,0),(10,10),10)

snake_pos=[[320,240],[340,240],[360,240]]
colector=[snake_pos[0][0],snake_pos[0][1]]

apple=pygame.Surface((20,20)).convert()
apple.set_colorkey(apple.get_at((0,0)))
pygame.draw.circle(apple,(255,0,0),(10,10),10)
apple_pos=[120,240]


pygame.key.set_repeat(400, 30)

while True:
    #loop speed limitation
    #30 frames per second is enought
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():    #wait for events
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #keyboard movement commands
        if event.type == KEYDOWN:
            if event.key == K_UP:
             if [snake_pos[0][0],snake_pos[0][1]-20]!=snake_pos[1]:
               direction=up
            elif event.key == K_DOWN:
             if [snake_pos[0][0],snake_pos[0][1]+20]!=snake_pos[1]:
               direction=down
            elif event.key == K_LEFT:
             if [snake_pos[0][0]-20,snake_pos[0][1]]!=snake_pos[1]:
               direction=left
            elif event.key == K_RIGHT:
             if [snake_pos[0][0]+20,snake_pos[0][1]]!=snake_pos[1]:
               direction=right
        #mouse movement commands
        if event.type == MOUSEBUTTONDOWN:             
           if event.button == 1:
              if [snake_pos[0][0]-20,snake_pos[0][1]]!=snake_pos[1]:direction=left
           elif event.button == 3:
                if [snake_pos[0][0]+20,snake_pos[0][1]]!=snake_pos[1]:direction=right
           elif event.button == 4:   
                if [snake_pos[0][0],snake_pos[0][1]-20]!=snake_pos[1]:direction=up
           elif event.button == 5:
                if [snake_pos[0][0],snake_pos[0][1]+20]!=snake_pos[1]:direction=down
             
    #move snake
    timer+=1
    if timer==speed_limiter:
        timer=0
        snake_pos[0][0]+=direction[0]
        snake_pos[0][1]+=direction[1]
        for index in range(len(snake_pos)):
            if snake_pos[index]!=snake_pos[0]:
               snake_pos[index],colector=colector,snake_pos[index]
        colector=[snake_pos[0][0],snake_pos[0][1]]
    
    #if snake eat apple
    if snake_pos[0]==apple_pos :
       body_end=[snake_pos[len(snake_pos)-1][0],snake_pos[len(snake_pos)-1][1]]
       snake_pos.append([body_end[0],body_end[1]])
       x=math.floor(random.randint(0,620)/20)*20
       y=math.floor(random.randint(0,460)/20)*20
       apple_pos =[x,y]
       score+=1

    #if snake hit wall
    if snake_pos[0][0]<0 or snake_pos[0][1]>640 \
    or snake_pos[0][1]<0 or snake_pos[0][1]>480 :
       game_over=1
       
    #if snake bite herself  
    for index in range(len(snake_pos)):
        if index !=0 and snake_pos[0]==snake_pos[index]:game_over=1    
                   
    if game_over:
       snake_pos=[[320,240],[340,240],[360,240]]
       colector=[snake_pos[0][0],snake_pos[0][1]]
       apple_pos=[120,240]
       direction=left
       game_over=0
       
    #blit things and refresh screen   
    screen.fill(color)
    for x,y in snake_pos:
        screen.blit(snake,(x,y))
    screen.blit(apple,apple_pos)
    text=font.render(("score:"+str(score)), True, (250,250,250));screen.blit(text,(0,0))
    pygame.display.flip()            
