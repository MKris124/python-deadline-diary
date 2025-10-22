from typing import Collection, List, Literal, Type
import class_file as Class

def Reading():
    try:
        path = "adatok.txt"
        readed_informations = open(path, "r", encoding="utf-8")
        rows = readed_informations.readlines()
        events: List[Class.Event] = []
        for row in rows:
            line = row.strip("\n").split(",")
            id = line[0].strip()
            name = line[1].strip()
            sdate = line[2].strip()
            time = line[3].strip()
            place = line[4].strip()
            if len(line) == 5:
                other = ""
            else:
                other = line[5].strip()
            e = Class.Event(sdate, time, name, place, other, id)
            events.append(e)
        readed_informations.close()
        return events
    except (FileExistsError, FileNotFoundError):
        print('Fájlkezelési hiba')
