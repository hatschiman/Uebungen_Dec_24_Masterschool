# Conditional Expressions
# Booleans:
#   True
#   False

# Verschiedene Vergleichsoperatoren:
a = 20
b = 20
print(f"a = {a}  b = {b}")
print(f"Gleich         (a == b): {a == b}")
print(f"Ungleich       (a != b): {a != b}")
print(f"Größer als     (a > b) : {a > b}")
print(f"Größer gleich  (a >= b): {a >= b}")
print(f"Kleiner als    (a < b) : {a < b}")
print(f"Kleiner gleich (a <= b): {a <= b}")
print("")

# If conditions überprüfen eine Bedingung und führen den Codeblock aus, wenn
# die Bedingung wahr (True) ist
score = 92
if score > 90:
    print("Sehr gut bestanden!!")
# Wenn die if-Condition False ergibt, kann man weitere Conditions mit elif
# überprüfen (mehrfach möglich)
elif score > 80:
    print("Gut bestanden!")
# Wenn alle oberen Conditions False ergeben, kann man mit else noch alle
# übrigen Fälle abdecken
else:
    print("Nicht bestanden")

# Logische Verknüpfungen:
temp = 26
weekend = False
if not (temp > 25 and weekend):
        print("Wir gehen baden!")

# Logische Operatoren dienen zur logischen Verknüpfung von Wahrheitswerten,
# d.h. aus zwei Wahrheitswerten wird einer. Dazu stehen die and und die or-
# Verknüpfung zur verfügung, sowie eine Möglichkeit, Wahrheitswerte mit not
# zu negieren:

wert1 = True
wert2 = False

# and-Verknüpfung (beide Werte müssen wahr sein für ein True):
print("")
print("UND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or-Verknüpfung (mindestens einer muss wahr sein für True):
print("")
print("ODER")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negation kehrt die Wahrheitswerte ins Gegenteil
print("")
print("Negation")
print(not True)
print(not False)
