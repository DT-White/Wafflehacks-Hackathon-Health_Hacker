from genericpath import exists
from pathlib import Path

p = Path(__file__)
filepath = str(p.parent.absolute()) + "\jentry_log.txt"


def write_to_log(log_entry):
    if not exists(filepath):
        open(filepath, "x")
        file = open(filepath, "a")
        file.write()
    file = open(filepath + "\jentry_log.txt", "a")
    file.write(log_entry)