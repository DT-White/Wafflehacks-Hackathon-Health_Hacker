from tkinter import W
import pygame
from pygame import display, image

pygame.init()
SCREEN_HEIGHT = 864
SCREEN_WIDTH = 1536
WIN = display.set_mode((0,0), pygame.FULLSCREEN)
display.set_caption("practice screen")

WHITE = (255,255,255)
FPS = 60

background_image = image.load("resource\\background.png") #load an image as a surface

 #load an image, convert alpha preserves transparency
 # {CHECK_BUTTON}
check_image = pygame.image.load("resource\\button_mood_submit.png").convert_alpha()
confirm_button_xy = (645,550)
button_confirm = check_image.get_rect(topleft = confirm_button_xy)

# {MOOD_BAR}
mood_bar_image = pygame.image.load("resource\\bar_mood.png").convert_alpha()
mood_bar_xy = (140,290)

button_list = []
button_xy_list = []
button_image_list = []

# {MOOD_BUTTONS}
button_image_list.append(pygame.image.load("resource\\button_mood_1.png").convert_alpha())
button_xy_list.append((175,331))
button_list.append(button_image_list[0].get_rect(topleft = button_xy_list[0]))

button_image_list.append(pygame.image.load("resource\\button_mood_2.png").convert_alpha())
button_xy_list.append((304,331))
button_list.append(button_image_list[1].get_rect(topleft = button_xy_list[1]))

button_image_list.append(pygame.image.load("resource\\button_mood_3.png").convert_alpha())
button_xy_list.append((433,331))
button_list.append(button_image_list[2].get_rect(topleft = button_xy_list[2]))

button_image_list.append(pygame.image.load("resource\\button_mood_4.png").convert_alpha())
button_xy_list.append((562,331))
button_list.append(button_image_list[3].get_rect(topleft = button_xy_list[3]))

button_image_list.append(pygame.image.load("resource\\button_mood_5.png").convert_alpha())
button_xy_list.append((691,331))
button_list.append(button_image_list[4].get_rect(topleft = button_xy_list[4]))

button_image_list.append(pygame.image.load("resource\\button_mood_6.png").convert_alpha())
button_xy_list.append((820,331))
button_list.append(button_image_list[5].get_rect(topleft = button_xy_list[5]))

button_image_list.append(pygame.image.load("resource\\button_mood_7.png").convert_alpha())
button_xy_list.append((949,331))
button_list.append(button_image_list[6].get_rect(topleft = button_xy_list[6]))

button_image_list.append(pygame.image.load("resource\\button_mood_8.png").convert_alpha())
button_xy_list.append((1078,331))
button_list.append(button_image_list[7].get_rect(topleft = button_xy_list[7]))

button_image_list.append(pygame.image.load("resource\\button_mood_9.png").convert_alpha())
button_xy_list.append((1207,331))
button_list.append(button_image_list[8].get_rect(topleft = button_xy_list[8]))

button_image_list.append(pygame.image.load("resource\\button_mood_10.png").convert_alpha())
button_xy_list.append((1336,331))
button_list.append(button_image_list[9].get_rect(topleft = button_xy_list[9]))

def draw_image(image, xy):
    WIN.blit(image, xy) #Screen.blit(image, (x,y))


def draw_bg(color):
    WIN.fill(color) #fill the window with color, color is a tuple variable (R,G,B)


def main():
    clock = pygame.time.Clock()
    run = True
    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frame
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running

            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_1): #If the player clicks X button, or presses keyboard 1 (the 1 key)
                pygame.quit() #quit
                exit() #terminate

            if event.type == pygame.MOUSEMOTION:
                for i in range(10):
                    if(button_list[i].collidepoint(pygame.mouse.get_pos())):
                        print("mouse is over button " + str(i))

            if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked 
                for i in range(10):
                    if(button_list[i].collidepoint(event.pos)):
                        print(i + 1)
                        return(i + 1)

                if(button_confirm.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    pygame.quit() #quit
                    exit() #terminate

       
        draw_bg(WHITE)
        draw_image(background_image, (0,0))
        draw_image(check_image, confirm_button_xy)
        draw_image(mood_bar_image, mood_bar_xy)

        for i in range(10):
            draw_image(button_image_list[i], button_xy_list[i])

        pygame.display.flip()#This updates the screen to show all changes     
        
    pygame.quit()

#__name__ prevents python from running file whenever it is imported by other files
if __name__ == "__main__":
    main()