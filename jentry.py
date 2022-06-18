import pygame
import datetime

class jentry:
    #Variables
    today = datetime.datetime.now().strftime("%x")
    mood = 0
    social = 0
    energy = 0
    freetime = 0
    exercise = 0
    diet = 0
    sleep = 0
    menstruation = False
    journal = ""

    #Constructor
    def __jentry__(mood, social, energy, freetime, exercise, diet, sleep, menstruation, journal):
        self.today = datetime.datetime.now().strftime("%x")
        self.mood = mood
        self.social = social
        self.energy = energy
        self.freetime = freetime
        self.exercise = exercise
        self.diet = diet
        self.sleep = sleep
        self.menstruation = menstruation
        self.journal = journal
    
    #Getters
    #Setters
    #Methods