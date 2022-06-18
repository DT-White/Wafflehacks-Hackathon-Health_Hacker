from asyncio.windows_events import NULL
from contextlib import nullcontext
import pygame
from file_reader import FileReader
from journal import *
import random
from Main_Menu_Screen import display_main_menu_screen

file_reader = FileReader()
log_entries = file_reader.read_log()
journal = Journal(log_entries)
track_menstruation = True
trends = []
today_mood = 0
today_social = 0
today_energy = 0
today_freetime = 0
today_exercise = 0
today_diet = 0
today_sleep = 0
today_menstruation = False
today_journal = ""

def run():
    if log_entries == "EMPTY":
        track_menstruation = welcome_screen()
    zero_main_menu()

def welcome_screen():
    #display welcome
    #ask about menstruation
    return #true or false

def zero_main_menu():
    quote = random.choice(file_reader.read_quotes())
    show_journal_button = False
    if not datetime.today in journal.get_jentries():
        show_journal_button = True
    display_main_menu_screen(quote, show_journal_button)

    #BUTTONS --> {BOTTOM} of the screen:
        #go to [Trends] screen (screen five)
        #go to [Journal] screen (screen one)
        #go to [Quit] screen (screen six)

def one_mood_screen():
    #today_mood = display_mood_screen()

    # Back [<-.png] button (to main_menu)
    # prints "How is your mood today on a scale of one to ten?" on screen (make it cozy <3)
    # loop 10 times to display following:
        #display mood button #[i] <-- iterates 1 through 10
        #buttons should vary in color from {RED} to {GREEN} (fade from red to green)

    #display [check.png] button (Screen two; record selected button above into Mood)
        #Button should be {between 5 and 6}
    #needs to also display "1", and "10" underneath the line of buttons
        #don't want to display all 10 numbers
    pass

def two_social_energy_freetime_screen():
    

    #do the following each for "Social", "Energy", "Freetime":
        #loop 4 times to display following:
            #A box with [i] <-- iterates {0 through 3}
            #box color should vary from {RED} to {GREEN}
            #buttons should print left to right
        #this row of buttons should be labeled "Social", "Energy", "Freetime" in order, labeled from top to bottom
        #To the left of each name, an image representing each will be displayed
            #Social --> message chat logo
            #Energy --> lightning bolt
            #Freetime --> clock
    
    #BUTTONS --> {TOP} of the screen:
        # [Mental Health] tab (current screen --> disable button)
        # [Physical Health] tab (screen three)
        # [Journal] tab (screen four)
        # back [<-] button (screen zero)
    pass

def three_exercise_diet_sleep_screen():
    #do the following each for "Exercise", "Diet", "Sleep":
        #Loop 4 times to display following:
            #A box with [i] <-- iterates 0 through 3
            #box color should vary from RED to GREEN
            #buttons should print left to right
        #this row of buttons should be labeled "Exercise", "Diet", "Sleep" in order, labeled from top to bottom
        #To the left of each name, an image representing each will be displayed
            #Exercise --> dumbbell
            #Sleep --> Moon and stars
            #Diet --> An apple or drumstick or something
    
    #BUTTONS --> {TOP} of the screen:
        # [Mental Health] tab (screen two)
        # [Physical Health] tab (current screen --> disable button)
        # [Journal] tab (screen four)
        # back [<-] button (screen zero)
    pass

def four_journal_screen():
    #display empty text box to accept user input
    #display menstruation [blood.png] button
        #if user menstruates, display button
            #else 
        #button should be a boolean to indicate that user is either currently on or off period (bleeding or not)
    #display [Submit] journal button (parses/logs data, goes to screen **ZERO** the main menu screen)

        #jentry called -> data parsed here

    #BUTTONS --> top of the screen:
        # [Mental Health] tab (screen two)
        # [Physical Health] tab (screen three)
        # [Journal] tab (current screen --> disable button)
        # back [<-] button (screen zero)
    pass

def five_analysis_screen():
    #Display graph:
        #X-axis is date
            #should have configuration for 7-day, and 30-day scale
            #7-day scale is the {DEFAULT}
        #Y-axis is mood
            #should range from 0 (at the origin) to 10 at the highest point
    
    #BUTTONS --> {RIGHT} of the screen:
        #Buttons should be organized in two columns and six rows
        
        #ROW {ONE}
            #displays a menstruation [blood.png] button that toggles period days (see below)
            #displays a back [<] button (returns to screen one --> main menu)
        
        #ROWS {TWO} - {THREE} - {FOUR}
            #order of elements to display, left to right, top to bottom:
                #Social, Energy, Freetime, Exercise, Sleep, Diet
            #All six variable [X.png] where X is an image representing the statistic to track
                #these images should show up on screens two and three (physical and mental health screens)
            
        #ROW {FIVE}
            #Month-Long [calendar.png] to display the graph on a 30-day scale
            #Week-Long [calendar_week_highlighted.png] to display the graph on a 7-day scale
            
        #ROW {SIX}
            # Next [>] and Previous [<] buttons that cycle through the currently selected time-scale on the graph
                # if "Week" scale is selected, cycle through 7 days at a time
                # if "Month" scale is selected, cycle through 30 days at a time

    #Above the graph:
        #display a red line starting with the day the period started and period ended
            #should account for a currently occuring period (ending at the present day)
                #Do we want to have a symbol indicating an on-going period?
    pass

def six_quit_screen():
    trend_message = "You're doing well! Keep up the good work!"
    reminder_or_quote = ""
    if journal.check_lowscore("Mood"):
        trends.append("Looks like your mood has been low recently :\(")
        get_downward_trend_message("Social")
        get_downward_trend_message("Energy")
        get_downward_trend_message("Freetime")
        get_downward_trend_message("Exercise")
        get_downward_trend_message("Diet")
        get_downward_trend_message("Sleep")
    if len(trends) > 0:
        trend_message = random.choice(trends)
    if not datetime.today in journal.get_jentries():
        reminder_or_quote = "Don't forget to log your journal entry for today!"
    else:
        reminder_or_quote = random.choice(file_reader.read_quotes())
    #display_quit_screen(trend_message, reminder_or_quote)
    
    #BUTTONS --> {Bottom} of the screen::
        # a [Back] button (go to screen one --> main menu)
        # and a [Quit] button (which closes the application)
    

def get_downward_trend_message(value):
    if journal.is_downward_trend(value):
        trends.append("There's been a downward trend in your " + value + " recently.")


run()