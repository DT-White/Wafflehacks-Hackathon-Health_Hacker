import datetime

class jentry:
    #Variables
    __jentries = {}
    __is_menstruating = False

    #Constructor
    def __journal__(self, is_menstruating, jentries):
        self.is_menstruating = is_menstruating
        # tell the reader to get log to fill in "dictionary"
    
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