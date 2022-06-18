import os
import pygame
from pathlib import Path

SCREEN_HEIGHT = 1536
SCREEN_WIDTH = 864
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("practice screen")
print(WIN.get_size())


def main():
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
                if(button_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    pygame.quit() #quit
                    exit() #terminate

       
        draw_bg(WHITE) 
        draw_image(background_image, (0,0))
        draw_image(button_image, button_xy)
      #  draw_rect()
      #  draw_line()
        
        pygame.display.flip()#This updates the screen to show all changes     
        
    pygame.quit()
    
#__name__ prevents python from running file whenever it is imported by other files
if __name__ == "__main__":
    main()