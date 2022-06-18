from pathlib import Path

class file_reader:

    
    __track_menstruation = False

    def read_log(self):
        __p = Path(__file__)
        __filepath = str(__p.parent.absolute())
        file = open(__filepath + "\jentry_log.txt", "r")
        menstruation_line = file.readline()
        
        if not menstruation_line:
            return "EMPTY"
        self.__track_menstruation = menstruation_line.split("|")[0] == 'True'
        print(self.__track_menstruation)
        file.readline()
        jentries = []
        log_entry = file.readline()
        while log_entry:
            jentries.append(log_entry.split("|"))
            log_entry = file.readline()
        file.close()
        return jentries

    def track_menstruation(self):
        return self.track_menstruation


    def read_quotes(self):
        __p = Path(__file__)
        __filepath = str(__p.parent.absolute())
        file = open(__filepath + "\daily_quotes.txt", "r")
        quotes = []
        quote_line = file.readline()
        while quote_line:
            quotes.append(quote_line)
            quote_line = file.readline()
            file.readline()
        file.close()
        for quote in quotes:
            print(quote)
