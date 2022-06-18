import datetime

from FileReader import file_reader

class Journal:
    #Variables
    __jentries = {}
    __is_menstruating = False

    #Constructor
    def __Journal__(self):        
        for current_jentry in file_reader.read_log:
            self.__jentries[jentry[0]] = Jentry(current_jentry[1])
    
    #Getters
    def get_menstruation(self):
        return self.menstruation

    # def get_jentries(self):
    #     return self.__jentries
    
    #Setters
    
    #Methods
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