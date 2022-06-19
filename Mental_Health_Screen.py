import pygame
from pygame import display, draw, image
from jentry import Jentry

pygame.init()

SCREEN_HEIGHT = 864
SCREEN_WIDTH = 1536
WIN = display.set_mode((0,0), pygame.FULLSCREEN)
display.set_caption("mental health screen")
cozyfont = pygame.font.Font('resource\CooperFiveOpti-Black.otf',  36)

WHITE = (255,255,255)
FPS = 60

background_image = pygame.image.load("resource\\background.png") #load an image as a surface
text_bg = pygame.image.load("resource\\text_background.png").convert_alpha() #load an image, convert alpha preserves transparency

# {MIND_BUTTON}
mind_button_image = pygame.image.load("resource\\tab_mind_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
mind_button_xy = (40,30)
mind_button = mind_button_image.get_rect(topleft = mind_button_xy)

# {BODY_BUTTON}
body_button_image = pygame.image.load("resource\\tab_body_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
body_button_xy = (540,30)
body_button = body_button_image.get_rect(topleft = body_button_xy)

# {JOURNAL_BUTTON}
journal_button_image = pygame.image.load("resource\\tab_journal_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
journal_button_xy = (1040,30)
journal_button = journal_button_image.get_rect(topleft = journal_button_xy)

# {ROW IDENTIFIERS}
social_image = pygame.image.load("resource\\icon_social_unselected.png").convert_alpha()
social_logo_xy = (40,240)
energy_image = pygame.image.load("resource\\icon_energy_unselected.png").convert_alpha()
energy_logo_xy = (40,440)
time_image = pygame.image.load("resource\\icon_time_unselected.png").convert_alpha()
time_logo_xy = (40,640)

########################################################
#               Number buttons here                    #
########################################################

social_buttons = []
social_xy = []
energy_buttons = []
energy_xy = []
time_buttons = []
time_xy = []

button_images_up = []
button_images_down = []

# {BUTTON UP GRAPHICS}
button_images_up.append(image.load("resource\\button_0_unselected.png").convert_alpha())
button_images_up.append(image.load("resource\\button_1_unselected.png").convert_alpha())
button_images_up.append(image.load("resource\\button_2_unselected.png").convert_alpha())
button_images_up.append(image.load("resource\\button_3_unselected.png").convert_alpha())

button_images_down.append(image.load("resource\\button_0_selected.png").convert_alpha())
button_images_down.append(image.load("resource\\button_1_selected.png").convert_alpha())
button_images_down.append(image.load("resource\\button_2_selected.png").convert_alpha())
button_images_down.append(image.load("resource\\button_3_selected.png").convert_alpha())

# {SOCIAL BUTTONS [x] = 810, 990, 1170, 1350 --> [y] = 236 }
social_xy.append((810,236))
social_buttons.append(button_images_up[0].get_rect(topleft = social_xy[0]))
social_xy.append((990,236))
social_buttons.append(button_images_up[1].get_rect(topleft = social_xy[1]))
social_xy.append((1170,236))
social_buttons.append(button_images_up[2].get_rect(topleft = social_xy[2]))
social_xy.append((1350,236))
social_buttons.append(button_images_up[3].get_rect(topleft = social_xy[3]))

# {ENERGY BUTTONS [x] = 810, 990, 1170, 1350 --> [y] = 436 }
energy_xy.append((810,436))
energy_buttons.append(button_images_up[0].get_rect(topleft = energy_xy[0]))
energy_xy.append((990,436))
energy_buttons.append(button_images_up[1].get_rect(topleft = energy_xy[1]))
energy_xy.append((1170,436))
energy_buttons.append(button_images_up[2].get_rect(topleft = energy_xy[2]))
energy_xy.append((1350,436))
energy_buttons.append(button_images_up[3].get_rect(topleft = energy_xy[3]))

# {TIME BUTTONS [x] = 810, 990, 1170, 1350 --> [y] = 636 }
time_xy.append((810,636))
time_buttons.append(button_images_up[0].get_rect(topleft = time_xy[0]))
time_xy.append((990,636))
time_buttons.append(button_images_up[1].get_rect(topleft = time_xy[1]))
time_xy.append((1170,636))
time_buttons.append(button_images_up[2].get_rect(topleft = time_xy[2]))
time_xy.append((1350,636))
time_buttons.append(button_images_up[3].get_rect(topleft = time_xy[3]))

# {BACK_BUTTON}
# back_button_image = pygame.image.load("resource\\icon_back_arrow.png").convert_alpha()
# back_button_xy = (1389,18)
# back_button = back_button_image.get_rect(topleft = back_button_xy)


def draw_image(image, xy):
    WIN.blit(image, xy) #Screen.blit(image, (x,y))


def draw_bg(color):
    WIN.fill(color) #fill the window with color, color is a tuple variable (R,G,B)
        

def display_health_screen(today_jentry):
    clock = pygame.time.Clock()
    run = True
    social_selection = False
    energy_selection = False
    time_selection = False
    social_value = 0

    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frame
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running

            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_1): #If the player clicks X button, or presses keyboard 1 (the 1 key)
                pygame.quit() #quit
                exit() #terminate

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    if(social_buttons[i].collidepoint(event.pos)):
                        social_selection = True
                        social_value = i
                        print("Social: " + str(i))
                        today_jentry.set_value("Social", i)

                for i in range(4):
                    if(energy_buttons[i].collidepoint(event.pos)):
                        energy_selection = True
                        energy_value = i
                        print("Energy: " + str(i))
                        today_jentry.set_value("Energy", i)

                for i in range(4):
                    if(time_buttons[i].collidepoint(event.pos)):
                        time_selection = True
                        time_value = i
                        print("Time: " + str(i))
                        today_jentry.set_value("Time", i)

            # if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked 
            #     if(back_button_image.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
            #         return

            # --->    [[[today_jentry_to_update.set_value("Energy", 2)]]]


        draw_image(background_image, (0,0))
        draw_image(mind_button_image, mind_button_xy)
        draw_image(body_button_image, body_button_xy)
        draw_image(journal_button_image, journal_button_xy)

        # draw social
        for i in range(4):
            draw_image(button_images_up[i], social_xy[i])

        #draw energy
        for i in range(4):
            draw_image(button_images_up[i], energy_xy[i])
        
        #draw time
        for i in range(4):
            draw_image(button_images_up[i], time_xy[i])

        #draw social button pressed
        if (social_selection):
            draw_image(button_images_down[social_value], social_xy[social_value])

        #draw energy button pressed
        if (energy_selection):
            draw_image(button_images_down[energy_value], energy_xy[energy_value])

        #draw time button pressed
        if (time_selection):
            draw_image(button_images_down[time_value], time_xy[time_value])

        draw_image(social_image, social_logo_xy)
        draw_image(energy_image, energy_logo_xy)
        draw_image(time_image, time_logo_xy)
        #draw_image(back_button_image, back_button_xy)
        
        pygame.display.flip() # This updates the screen to show all changes     
        
    pygame.quit()

if __name__ == "__main__":
    display_health_screen()