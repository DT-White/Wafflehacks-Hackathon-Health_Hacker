import os
import pygame

SCREEN_HEIGHT = 864
SCREEN_WIDTH = 1536
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("main menu screen")


WHITE = (255,255,255)
FPS = 60

background_image = pygame.image.load(os.path.join('resource', 'mockup.png')) #load an image as a surface

button_analyze = pygame.image.load(os.path.join('resource', 'button_analyze.png')).convert_alpha() #load an image, convert alpha preserves transparency
button_analyze_xy = (130,630)
button_analyze_rect = button_analyze.get_rect(topleft = button_analyze_xy)

button_journal = pygame.image.load(os.path.join('resource', 'button_journal.png')).convert_alpha() #load an image, convert alpha preserves transparency
button_journal_xy = (600,630)
button_journal_rect = button_analyze.get_rect(topleft = button_journal_xy)

button_quit = pygame.image.load(os.path.join('resource', 'button_back.png')).convert_alpha() #load an image, convert alpha preserves transparency
button_quit_xy = (1070,630)
button_quit_rect = button_analyze.get_rect(topleft = button_quit_xy)



def draw_image(image, xy):
    WIN.blit(image, xy) #Screen.blit(image, (x,y))


def draw_bg(color):
    WIN.fill(color) #fill the window with color, color is a tuple variable (R,G,B)


def draw_rect(color, rectangle):
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(WIN, color, rectangle)
    

def draw_line():
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.line(WIN, (0,0,0), (0,0), (600,100), 6)
    


def display_main_menu_screen():
    clock = pygame.time.Clock()
    run = True
    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frane
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running
            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_1): #If the player clicks X button, or presses keyboard 1 (the 1 key)
                pygame.quit() #quit
                exit() #terminate
            if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked 
                if(button_analyze_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    return ("analyze")

       
        draw_bg(WHITE) 
        draw_image(background_image, (0,0))
        draw_image(button_analyze, button_analyze_xy)
        draw_image(button_journal, button_journal_xy)
        draw_image(button_quit, button_quit_xy)
        draw_rect((100,100,100), pygame.Rect(150,100,1200,150))
        draw_rect((100,100,100), pygame.Rect(150,350,1200,150))
        #draw_line()
        
        pygame.display.flip()#This updates the screen to show all changes     
        
    pygame.quit()

#__name__ prevents python from running file whenever it is imported by other files
if __name__ == "__main__":
    display_main_menu_screen()