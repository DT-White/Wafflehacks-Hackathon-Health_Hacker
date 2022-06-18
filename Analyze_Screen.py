import os
import pygame
from jentry import Jentry
from pathlib import Path

pygame.init()

SCREEN_HEIGHT = 864
SCREEN_WIDTH = 1536
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("main menu screen")
cozyfont = pygame.font.Font('resource\CooperFiveOpti-Black.otf',  36)

WHITE = (255,255,255)
FPS = 60

#testJentry = Jentry(mood, social, energy, freetime, exercise, diet, sleep, menstruation, journal)

testJentry = Jentry(3, 3, 3, 3,3,3,3,False,"This Jentry is for testing")

background_image = pygame.image.load("resource\\background.png") #load an image as a surface

img_axis = pygame.image.load("resource\\axis_week.png").convert_alpha() #load an image, convert alpha preserves transparency
axis_xy = (113,79)

icon_period_s = pygame.image.load("resource\\icon_period_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_period_u = pygame.image.load("resource\\icon_period_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_period_xy = (1250,0)
icon_period_rect = icon_period_u.get_rect(topleft = icon_period_xy)

icon_back_arrow = pygame.image.load("resource\\icon_back_arrow.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_back_arrow_xy = (1394,0)
icon_back_arrow_rect = icon_back_arrow.get_rect(topleft = icon_back_arrow_xy)

icon_social_s = pygame.image.load("resource\\icon_social_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_social_u = pygame.image.load("resource\\icon_social_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_social_xy = (1250,144)
icon_social_rect = icon_social_u.get_rect(topleft = icon_social_xy)

icon_exercise_s = pygame.image.load("resource\\icon_exercise_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_exercise_u = pygame.image.load("resource\\icon_exercise_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_exercise_xy = (1394,144)
icon_exercise_rect = icon_exercise_u.get_rect(topleft = icon_exercise_xy)

icon_time_s = pygame.image.load("resource\\icon_time_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_time_u = pygame.image.load("resource\\icon_time_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_time_xy = (1250,288)
icon_time_rect = icon_time_u.get_rect(topleft = icon_time_xy)

icon_diet_s = pygame.image.load("resource\\icon_diet_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_diet_u = pygame.image.load("resource\\icon_diet_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_diet_xy = (1394,288)
icon_diet_rect = icon_diet_u.get_rect(topleft = icon_diet_xy)

icon_energy_s = pygame.image.load("resource\\icon_energy_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_energy_u = pygame.image.load("resource\\icon_energy_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_energy_xy = (1250,432)
icon_energy_rect = icon_energy_u.get_rect(topleft = icon_energy_xy)

icon_sleep_s = pygame.image.load("resource\\icon_sleep_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_sleep_u = pygame.image.load("resource\\icon_sleep_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_sleep_xy = (1394,432)
icon_sleep_rect = icon_sleep_u.get_rect(topleft = icon_sleep_xy)

icon_month_s = pygame.image.load("resource\\icon_month_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_month_u = pygame.image.load("resource\\icon_month_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_month_xy = (1250,576)
icon_month_rect = icon_month_u.get_rect(topleft = icon_month_xy)

icon_week_s = pygame.image.load("resource\\icon_week_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_week_u = pygame.image.load("resource\\icon_week_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_week_xy = (1394,576)
icon_week_rect = icon_week_u.get_rect(topleft = icon_week_xy)

icon_move_backward = pygame.image.load("resource\\icon_move_backward.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_move_backward_xy = (1250,720)
icon_move_backward_rect = icon_back_arrow.get_rect(topleft = icon_move_backward_xy)

icon_move_forward = pygame.image.load("resource\\icon_move_forward.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_move_forward_xy = (1394,720)
icon_move_forward_rect = icon_back_arrow.get_rect(topleft = icon_move_forward_xy)

def draw_image(image, xy):
    WIN.blit(image, xy) #Screen.blit(image, (x,y))


def draw_bg(color):
    WIN.fill(color) #fill the window with color, color is a tuple variable (R,G,B)


def draw_rect(color, rectangle):
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(WIN, color, rectangle, 70 , 15)
    pygame.draw.rect(WIN, color, rectangle, 2 , 3)
    

def draw_line():
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.line(WIN, (0,0,0), (0,0), (600,100), 6)

def display_navigation(stat_select, timespan, period_selected):
    if(period_selected):
            draw_image(icon_period_s, icon_period_xy)
    else:
        draw_image(icon_period_u, icon_period_xy)

    draw_image(icon_back_arrow, icon_back_arrow_xy)

    if(stat_select == "social"):
        draw_image(icon_social_s, icon_social_xy)
    else:
        draw_image(icon_social_u, icon_social_xy)

    if(stat_select == "exercise"):
        draw_image(icon_exercise_s, icon_exercise_xy)
    else:
        draw_image(icon_exercise_u, icon_exercise_xy)
    if(stat_select == "time"):
        draw_image(icon_time_s, icon_time_xy)
    else:
        draw_image(icon_time_u, icon_time_xy)
    if(stat_select == "diet"):
        draw_image(icon_diet_s, icon_diet_xy)
    else:
        draw_image(icon_diet_u, icon_diet_xy)
    if(stat_select == "energy"):
        draw_image(icon_energy_s, icon_energy_xy)
    else:
        draw_image(icon_energy_u, icon_energy_xy)
    if(stat_select == "sleep"):
        draw_image(icon_sleep_s, icon_sleep_xy)
    else:
        draw_image(icon_sleep_u, icon_sleep_xy)
    if(timespan == "month"):
        draw_image(icon_month_s, icon_month_xy)
    else:
        draw_image(icon_month_u, icon_month_xy)
    if(timespan == "week"):
        draw_image(icon_week_s, icon_week_xy)
    else:
        draw_image(icon_week_u, icon_week_xy)
    draw_image(icon_move_backward, icon_move_backward_xy)
    draw_image(icon_move_forward, icon_move_forward_xy)


def display_analyze_screen():
    clock = pygame.time.Clock()
    run = True
    stat_select = ""
    timespan = "week"
    period_selected = False

    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frame
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running
            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_1): #If the player clicks X button, or presses keyboard 1 (the 1 key)
                pygame.quit() #quit
                exit() #terminate
            if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked 
                print(event.pos)
                if(icon_period_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    period_selected = not period_selected
                
                if(icon_social_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    stat_select = "social"
                if(icon_exercise_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    stat_select = "exercise"
                if(icon_time_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    stat_select = "time"
                if(icon_diet_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    stat_select = "diet"
                if(icon_energy_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    stat_select = "energy"
                if(icon_sleep_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    stat_select = "sleep"
                if(icon_month_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    timespan = "month"
                if(icon_week_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    timespan = "week"
                


        draw_image(background_image, (0,0))
        ######### DISPLAY GRAPH ############
        draw_image(img_axis, axis_xy)


        ######### DISPLAY NAVIGATION #########
        display_navigation(stat_select, timespan, period_selected)


        pygame.display.flip()#This updates the screen to show all changes     
        
    pygame.quit()

if __name__ == "__main__":
    display_analyze_screen()