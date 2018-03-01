# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()
pygame.mixer.pre_init() 

# Window
SIZE = (800, 600)
TITLE = "Animation test"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
top_speed = 10
acceleration = 0.04
deceleration = 2 
vel = [0,0]
vel[0] = 0 

#background and pufferfish
backdrop = pygame.image.load('background.png')
pufferfish_right = pygame.image.load('puffer_fish.png')
pufferfish_left = pygame.transform.flip(pufferfish_right, True, False) 
#idle animation
'''idle_1 = pygame.image.load('idle/1.png')
idle_2 = pygame.image.load('idle/2.png')
idle_3 = pygame.image.load('idle/3.png')
idle_4 = pygame.image.load('idle/4.png')
idle_5 = pygame.image.load('idle/5.png')
idle_6 = pygame.image.load('idle/6.png')
idle_7 = pygame.image.load('idle/7.png')
idle_8 = pygame.image.load('idle/8.png')
idle_9 = pygame.image.load('idle/9.png')
idle_10 = pygame.image.load('idle/10.png')
idle_11 = pygame.image.load('idle/11.png')
idle_12 = pygame.image.load('idle/12.png')
idle_13 = pygame.image.load('idle/13.png')
idle_14 = pygame.image.load('idle/14.png')
idle_15 = pygame.image.load('idle/15.png')
idle_16 = pygame.image.load('idle/16.png')
idle_17 = pygame.image.load('idle/17.png')
idle_18 = pygame.image.load('idle/18.png')
idle_19 = pygame.image.load('idle/19.png')
idle_20 = pygame.image.load('idle/20.png')
idle_21 = pygame.image.load('idle/21.png')
idle_22 = pygame.image.load('idle/22.png')
idle_23 = pygame.image.load('idle/23.png')
sonic_idle = [idle_1, idle_2, idle_3, idle_4, idle_5, idle_6, idle_7, idle_8, idle_9, idle_10, idle_11, idle_12, idle_13, idle_14, idle_15, idle_16, idle_17, idle_18, idle_19, idle_20, idle_21, idle_22, idle_23]

#walking
walking_1 = pygame.image.load('walking/1.png')
walking_2 = pygame.image.load('walking/2.png')
walking_3 = pygame.image.load('walking/3.png')
walking_4 = pygame.image.load('walking/4.png')
walking_5 = pygame.image.load('walking/5.png')
walking_6 = pygame.image.load('walking/6.png')
walking_7 = pygame.image.load('walking/7.png')
walking_8 = pygame.image.load('walking/8.png')
sonic_walking = [walking_1, walking_2, walking_3, walking_4, walking_5, walking_6, walking_7, walking_8] 

#jogging
jogging_1 = pygame.image.load('jogging/1.png')
jogging_2 = pygame.image.load('jogging/2.png')
jogging_3 = pygame.image.load('jogging/3.png')
jogging_4 = pygame.image.load('jogging/4.png')
jogging_5 = pygame.image.load('jogging/5.png')
jogging_6 = pygame.image.load('jogging/6.png')
jogging_7 = pygame.image.load('jogging/7.png')
jogging_8 = pygame.image.load('jogging/8.png')
jogging_9 = pygame.image.load('jogging/9.png')
jogging_10 = pygame.image.load('jogging/10.png')
jogging_11 = pygame.image.load('jogging/11.png')
jogging_12 = pygame.image.load('jogging/12.png')
jogging_13 = pygame.image.load('jogging/13.png')
jogging_14 = pygame.image.load('jogging/14.png')
jogging_15 = pygame.image.load('jogging/15.png')
jogging_16 = pygame.image.load('jogging/16.png')
jogging_17 = pygame.image.load('jogging/17.png')
jogging_18 = pygame.image.load('jogging/18.png')
jogging_19 = pygame.image.load('jogging/19.png')
jogging_20 = pygame.image.load('jogging/20.png')
jogging_21 = pygame.image.load('jogging/21.png')
jogging_22 = pygame.image.load('jogging/22.png')
jogging_23 = pygame.image.load('jogging/23.png')
jogging_24 = pygame.image.load('jogging/24.png')
sonic_jogging = [jogging_1, jogging_2, jogging_3, jogging_4, jogging_5, jogging_6, jogging_7, jogging_8, jogging_9, jogging_10, jogging_11, jogging_12, jogging_13, jogging_14, jogging_15, jogging_16, jogging_17, jogging_18, jogging_19, jogging_20, jogging_21, jogging_22, jogging_23, jogging_24] 
'''
# running
running_1 = pygame.image.load('running/1.png')
running_2 = pygame.image.load('running/2.png')
running_3 = pygame.image.load('running/3.png')
running_4 = pygame.image.load('running/4.png')
running_5 = pygame.image.load('running/5.png')
running_6 = pygame.image.load('running/6.png')
running_7 = pygame.image.load('running/7.png')

sonic_running = [running_1, running_2, running_3, running_4, running_5, running_6, running_7]

#sonic_frames = [sonic_idle[] , sonic_walking[], sonic_jogging[], sonic_running[]]

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 200)
BLUE = (75, 200, 255)

#directional logic
direction = "left" 
sonic_left = sonic_running   
sonic_right = []
for s in sonic_left:
    sonic_right.append(pygame.transform.flip(s, True, False))

#puffers
def draw_pufferfish(p_loc, direction):
    if direction == "right": 
        screen.blit(pufferfish_right, (p_loc)) 
        x = p_loc[0]
        y = p_loc[1]

    elif direction == "left":
        screen.blit(pufferfish_left, (p_loc)) 
        x = p_loc[0]
        y = p_loc[1]


#sonic

def draw_background(x, y):
    screen.blit(backdrop, (x,y))
    
def sonic(x,y):
    sonic = random.randrange(0,400) 
    x = loc[0]
    y = loc[1]
                
def draw_sonic(loc, direction, frame):
    x = loc[0]
    y = loc[1]
    if direction == "left":
        screen.blit(sonic_left[frame] , (x, y))

    elif direction == "right": 
        screen.blit(sonic_right[frame] , (x, y))
    
    

"""make sonic(s)"""
num_hedgehogs = 1
hedgehogs = []
for i in range(num_hedgehogs):
    if direction == "left": 
        x = 400 
        y = 365
        loc = [x, y]
    if direction == "right": 
        x = 400
        y = 365 
        loc = [x, y]

    

    hedgehogs.append(loc)

''' make pufferfish '''


num_puffers = 10

puffers = [] 
for i in range(num_puffers):
         x = random.randrange(0, 900)
         y = random.randrange(30, 200)
         p_loc = [x, y]
         
         puffers.append(p_loc)

#Sounds
song1 = "marble_garden1.wav"
song2 = "marble_garden2.wav"
songs = [song1, song2]
current_song = 0 


def start_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)

start_music(songs[current_song])
    
# Game loop
pygame.mixer.music.play(-1)    

done = False
ticks = 0
frame = 0 
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_song = (current_song +1)% len(songs)
                start_music(songs[current_song]) 
        

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        vel[0] += -1* acceleration
        
    elif pressed[pygame.K_RIGHT]:
        vel[0] += acceleration
        

    else:
        if direction == "right":
            if (vel[0] > 0.05):
                vel[0] -= acceleration
            elif (vel[0] < 0.05):
                vel[0] = 0
        elif direction == "left":
            if (vel[0] < -0.05):
                vel[0] += acceleration
            elif (vel[0] > - 0.05):
                vel[0] = 0
        

            
            
                
        
    

#Game logic
    #Sonic movement 
    if vel[0] > 0:
        direction = "right"
    elif vel[0] < 0:
        direction = "left" 

    if direction == "right":
        top_speed = 10
        if vel[0] >= top_speed:
            vel[0] = top_speed
            
    elif direction == "left":
        top_speed = -10
        if vel[0] <= top_speed:
            vel[0] = top_speed 
        
    ticks += 1 
    if ticks%4 == 0:
        frame +=1
        if frame > 6:
            frame = 0
            
    if direction == "right":         
        loc[0] += vel[0]
    elif direction == "left":
        loc[0] +=  vel[0]

    for h in hedgehogs:
        if direction == "left": 
             h[0] += vel[0] 

             if direction == "left" and h[0] < -100:
                h[0] = 900
                h[1] = 365

        elif direction == "right": 
                h[0] += vel[0] 

                if direction == "right" and h[0] > 900:
                    h[0] = -100
                    h[1] = 365
                    
#Pufferfish movement
    for p in puffers:
        if direction == "right": 
            p[0] += 2
            if p[0]> 900:
                p[0] = random.randrange(-800,-100)
                p[1] = random.randrange(30, 200)

        elif direction == "left": 
            p[0] -= 2
            if p[0]< -100:
                p[0] = random.randrange(900, 1600)
                p[1] = random.randrange(30, 200) 


    

    # Drawing code

    ''' grass ''' 
    draw_background(0, 0) 
 

    ''' moon '''
    #pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' sonic '''
    for h in hedgehogs:
        draw_sonic(h, direction, frame)


    ''' pufferfish'''
    for p in puffers:
        draw_pufferfish(p, direction)  


   




    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
