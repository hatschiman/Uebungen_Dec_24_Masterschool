## Aufgabe 6
# Hier im Code sieht man einen Fehler, der dadurch entstanden ist, dass
# Variablen falsch benannt wurden. Es wird der Funktion number übergeben,
# allerdings arbeiten wir innerhalb der Funktion mit num, die außerhalb der
# Funktion definiert wird - das führt zu unerwartete Verhalten

num = 0
def number_checker(number):
    if number > 0:
    # if num > 0: # fehlerhaft
        return "Positive"
    elif number < 0:
    # elif num < 0: fehlerhaft
        return "Negative"
    else:
        return "Zero"

print(number_checker(5)) # Expected output: Positive