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
    def __jentry__(self, mood, social, energy, freetime, exercise, diet, sleep, menstruation, journal):
        self.today = datetime.datetime.now().strftime("%x") # --> MM/dd/yy
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
    def get_mood(self):
        return self.mood
        
    def get_social(self):
        return self.social

    def get_energy(self):
        return self.energy

    def get_freetime(self):
        return self.freetime

    def get_exercise(self):
        return self.exercise
    
    def get_diet(self):
        return self.diet

    def get_sleep(self):
        return self.sleep
    
    def get_menstruation(self):
        return self.menstruation

    def get_journal(self):
        return self.journal

    def get_date(self):
        return self.today
    
    #Setters
    
    #Methods
    def get_log(self):
        log = self.today + "|" + self.mood + "|" + self.social + "|" + self.energy + "|" + self.freetime + "|" + self.energy + "|" + self.diet + "|" + self.sleep + "|" + self.menstruation + "|" + self.journal
        return log
