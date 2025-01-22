## Aufgabe 4
# Hier an der Stelle wird im if-Statement der gesamte new_text überschrieben,
# wenn ein Leerzeichen gefunden wurde - das wollen wir nicht.
# Unten findet ihr zwei Möglichkeiten zur Korrektur des Bugs

def text_with_no_spaces(sentance):
    new_text = ""
    for char in sentance:
        if char == ' ':
            pass # pass bedeutet, dass hier in der Stelle nichts passieren soll
            # new_text = char # fehlerhafte Stelle im Code
        else:
            new_text += char
    return new_text

def text_with_no_spaces(sentance):
    new_text = ""
    for char in sentance:
        if char != ' ':
            new_text += char
    return new_text


text = "New Document"
print(text_with_no_spaces(text))