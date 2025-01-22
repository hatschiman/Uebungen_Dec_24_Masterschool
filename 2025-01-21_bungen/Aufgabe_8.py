## Aufgabe 8
# Hier hat man ein paar eckige Klammern zu viel gesetzt. Bei der Ermittlung der
# Länge der Liste wird die übergebene Liste family_members wiederum als
# Element in eine Liste eingefügt [family_members] und somit hat die Liste
# immer eine Länge von 1

def family_size_classifier(family_members):
    # num_members = len([family_members]) # fehlerhaft
    num_members = len(family_members)

    if num_members <= 3:
        return "Your family is small."
    elif 4 <= num_members <= 6:
        return "Your family is medium-sized."
    else:
        return "Your family is big!"

# Example usage:
my_family = ["Alice", "Bob", "Charlie", "David"]
result = family_size_classifier(my_family)
print(result) # should be medium-sized