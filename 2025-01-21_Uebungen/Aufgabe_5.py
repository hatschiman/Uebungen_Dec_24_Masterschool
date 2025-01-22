## Aufgabe 5
# Da Pfade in Linux mit einem / beginnen, wird das erste Element der Liste
# ein leerer String sein, weil vor dem ersten / nichts kommt.

def path_root_dir(path):
    splitted = path.split("/")
    # return splitted[0] # fehlerhaft
    return splitted[1]

path = "/usr/bin/data"
print(path_root_dir(path))
