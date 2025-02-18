"""def set_age():
    try:
        age = int(input("Geben Sie ihr Alter ein: "))
    except ValueError:
        print("Bitte geben Sie eine ganze Zahl ein")
    else:
        if age < 0:
            raise ValueError("Ungültiges Alter. Bitte geben Sie eine positive Zahl ein")

set_age()"""

"""try:
    num = int(input("Geben Sie eine Nummer ein: "))
    result = 10/num
except ValueError:
    print("Fehler")
except ZeroDivisionError:
    print("Fehler: Division durch 0")
else:
    print(f"Ergebnis: {result}")"""

# Aufgabe 1
# if/else
# Hier schaue ich der einfachheit halber nur nach Ganzzahlen - um das Programm
# vollständiger zu halten, müsste man den gleichen Check nochmal für Floats
# machen und den entsprechenden Kombinationen. Das habe ich einfach mal weg-
# gelassen

def is_divisible_by(number, divisor):

    # isinstance(var, type) überprüft, ob die Variable var vom Typ type ist
    # und gibt entsprechend True oder False zurück
    if isinstance(number, int) and isinstance(divisor, int):
        return number % divisor == 0
    else:
        return "Wrong Input"

print(is_divisible_by(10, 2))
print(is_divisible_by(10, "2"))  # Causes an exception

# Aufgabe 2

def add_percentage(price, percentage):
    if isinstance(price, (int, float)) and isinstance(percentage, (int, float)):
        return price + (percentage * price)

def add_percentage(price, percentage):
    try:
        return price + (percentage * price)
    except TypeError:
        return "Falscher Datentyp"
    finally:
        print("Dieser Output geschieht in jedem Fall")

print(add_percentage(100, 0.1))
print(add_percentage(100, "0.05"))  # Causes an exception

# Aufgabe 3:
def get_grade(database, student_name):
    try:
        return database[student_name]
    except KeyError:
        return "Name nicht in Datenbank gefunden"

# Case insensitive:
# Hier etwas komplizierter - Wir erstellen zwei Listen aus den Keys der
# Database. Eine Enthält die tatsächlichen Keys und die andere die Keys klein-
# geschrieben. Wir schauen, ob der kleingeschriebene (.lower()) Name des
# Studenten in der Kleingeschriebenen Liste ist und wenn ja, welchen Index er
# hat und Nutzen diesen Index dann in der richtigen Liste, um uns den Key
# zu holen
def get_grade(database, student_name):
    db_keys = list(database.keys())
    db_keys_lower = [key.lower() for key in db_keys]
    if student_name.lower() in db_keys_lower:
        index = db_keys_lower.index(student_name.lower())
        name = db_keys[index]
        return database[name]
    else:
        return "Name nicht in Datenbank gefunden"

db = {"John": "A+", "Mary": "B", "Jane": "C", "Thomas": "B+"}

name = "John"
print(get_grade(db, name))  # Works fine
name = "Johnn"
print(get_grade(db, name))  # Causes an exception

#Bonusaufgabe:
# mögliche Errortypes: https://www.tutorialsteacher.com/python/error-types-in-python
def calculate_square(number):
    if isinstance(number, str):
        raise TypeError("Falsches Format, bitte nutzen Sie float oder int")
    if number < 0:
        raise ValueError("Nummer darf nicht negativ sein")
    if not 100 >= number >= 1:
        raise ValueError("Nummer muss zwischen 1 und 100 liegen.")
    return number * number

# Abfangen der möglichen Exceptions:
try:
    calculate_square(101)
except ValueError as v_error:
    print(v_error)
except TypeError as t_error:
    print(t_error)