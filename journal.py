import datetime

class jentry:
    #Variables
    __jentries = {}
    __is_menstruating = False

    #Constructor
    def __journal__(self, is_menstruating, jentries):
        self.is_menstruating = is_menstruating
        #jentries map
    
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
        log = self.date + "|" + self.mood + "|" + self.social + "|" + self.energy + "|" + self.freetime + "|" + self.energy + "|" + self.diet + "|" + self.sleep + "|" + self.menstruation + "|" + self.journal
        return log