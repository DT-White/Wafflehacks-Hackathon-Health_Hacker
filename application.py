import pygame;

def zero_main_menu():
    #display quote of the day --> randomly generated from list of about 50 quotes
    #show health reminder --> based on data

    #buttons:
        #go to [Trends] screen (screen five)
        #go to [Journal] screen (screen one)
        #go to [Quit] screen (screen six)
    pass

def one_mood_screen():
    # Back [<-] button (to main_menu)
    # prints "How is your mood today on a scale of one to ten?" on screen (make it cozy <3)
    # loop 10 times to display following:
        #display mood button #[i] <-- iterates 1 through 10
        #buttons should vary in color from RED to GREEN (fade from red to green)

    #display [Submit] button (Screen two)
    #needs to also display "1" and "10" underneath the line of buttons
    pass

def two_social_energy_freetime_screen():
    #do the following each for "Social", "Energy", "Freetime":
        #loop 4 times to display following:
            #A box with [i] <-- iterates 0 through 3
            #box color should vary from RED to GREEN
            #buttons should print left to right
        #this row of buttons should be labeled "Social", "Energy", "Freetime" in order, labeled from top to bottom
    
    #buttons on top of screen:
        # [Mental Health] tab (current screen --> disable button)
        # [Physical Health] tab (screen three)
        # [Journal] tab (screen four)
        # back [<-] button (screen one)
    pass

def three_exercise_diet_sleep_screen():
    #do the following each for "Exercise", "Diet", "Sleep":
        #Loop 4 times to display following:
            #A box with [i] <-- iterates 0 through 3
            #box color should vary from RED to GREEN
            #buttons should print left to right
        #this row of buttons should be labeled "Exercise", "Diet", "Sleep" in order, labeled from top to bottom
    
    #buttons on top of screen:
        # [Mental Health] tab (screen two)
        # [Physical Health] tab (current screen --> disable button)
        # [Journal] tab (screen four)
        # back [<-] button (screen one)
    pass

def four_journal_screen():
    #display empty text box to accept user input
    #display menstruation [Period?] button
        #button should be a boolean to indicate that user is either currently on or off period (bleeding or not)
    #display [Submit] journal button (parses/logs data, goes to screen FIVE)

    #buttons on top of screen:
        # [Mental Health] tab (screen two)
        # [Physical Health] tab (screen three)
        # [Journal] tab (current screen --> disable button)
        # back [<-] button (screen one)
    pass

def five_analysis_screen():
    
    pass

def six_quit_screen():
    pass