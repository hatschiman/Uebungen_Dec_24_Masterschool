## Aufgabe 3
# In der fehlerhaften Version wird bei jedem Alter, das größer oder gleich
# 12 ist, das erste if-Statement wahr und die anderen werden ignoriert.
# Es gibt verschiedene Versionen, wie man das lösen kann. Im Folgenden ist
# eine Variante (Umkehr der if-Statements)
# Am Ende habe ich noch dem Alter ein Spektrum gegeben, dass es größer 0
# sein muss. Dann kommt man mit negativen Zahlen auch tatsächlich mal in
# den else-Bereich


def age_group_classifier(age):

    if age > 64:
        
        print("Senior")
    elif age > 19:
        print("Adult")
    elif age > 12:
        print("Teenager")
    elif 0 <= age <= 12:
        print("Child")
    else:
        print("Invalid age")

# Test cases
age_group_classifier(14) # should print Senior