from file_reader import FileReader
from jentry import Jentry
from datetime import datetime, timedelta

class Journal:
    #Variables
    jentries = {}

    #Constructor
    def __Journal__(self):        
        for current_jentry in FileReader.read_log():
            self.jentries = {[jentry[0]] : Jentry(current_jentry[1], current_jentry[2], current_jentry[3], current_jentry[4], current_jentry[5], current_jentry[6], current_jentry[7], current_jentry[8], current_jentry[9])}
    
    #Getters
    def get_is_menstruating(self):
        if (FileReader.track_menstruation):
            return True
        return False

    def get_jentries(self):
        return self.jentries
    
    #Setters
    
    #Methods
    def find_trend(self, value_to_check):
        today = datetime.now().strftime("%x")
        three_day_score = 0

        for current_day in self.jentries.keys:
            print(current_day)

        # Find trend
            # if last 3 days total score for attribute < 3 or 4
                # prompt reminder

        # get average of statistic
            # if week --> x / 7
                # return weekly average
                # return tip if weekly score < threshold
            # if month --> x / 30
                # return monthly average
                # return tip if monthly score < threshold