from pathlib import Path
__p = Path(__file__)
__filepath = str(__p.parent.absolute())
__track_menstruation = False

file = open(__filepath + "\jentry_log.txt", "r")
menstruation_line = file.readline()
if not menstruation_line:
    print("EMPTY")
__track_menstruation = menstruation_line.split("|")[0] == 'True'
print(__track_menstruation)
file.readline()
jentries = []
log_entry = file.readline()
while log_entry:
    jentries.append(log_entry.split("|"))
    log_entry = file.readline()
file.close
print("jentries") 