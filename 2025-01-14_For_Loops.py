haustiere = ["Hund", 1, 5.6, "Maus"]
# Iteriere durch Liste
for tier in haustiere:
     print(f"Das Haustier heißt: {tier}")

# Iteriere durch String
mein_satz = "Hallo, ich bin der Instructor!"
# for element in mein_satz:
#     print(element)
# zahlenliste = [1, 2, 3, 4, 5, 6]


# Iteriere durch geordnete Zahlen mit range
# range(start, stop, step)   - Alle Werte selbst definiert
# range (start, stop)        - Start, Stop variabel, Step default auf 1
# range (stop)               - Stop variabel, Step defaul auf 1, Start default auf 0

for zahl in range(0, 20, 2):
    print(zahl)

# Iteriere durch geordnete Zahlen mit range
# Iteriere durch eine Liste mit der range-Funktion
# len(liste) gibt die Anzahl an Elementen in der Liste aus - also ihre Länge
# und kann somit als Stopp-Wert verwendet werden
for index in range(0, len(haustiere), 2):
    print(f"Tier Nummer {zahl}: {haustiere[index]}")

print("\nAufgabe 1") # \n ist ein Zeilenumbruchoperator (newline)

def print_character():
    input_string = input("Gib eine Zeichenfolge ein:")
    for char in input_string:
        print(char)

print_character()


print("\nAufgabe 3")
prog_lang = ["Javascript", "Typescript", "Python", "Java", "C#", "Swift"]
def display_strings(liste):
    for element in liste:
        if not element.lower().startswith("j"):
            print(element)

# vereinfachte Version (mit gleicher Funktionalität):
def display_strings_simple(liste):
    for element in liste:
        element_lower = element.lower() # konvertiere alles in Kleinbuchstaben
        if not element_lower.startswith("j"):
            print(element)

# Weitere Alternative (mit ohne Konvertierung):
def display_strings_logic(liste):
    for element in liste:
        if not element.startswith("j"):
            print(element)
        # Falls es nicht mit j beginnt, schaue nach J
        elif not element.startswith("J"):
            print(element)

display_strings(prog_lang)
display_strings_simple(prog_lang)
display_strings_logic(prog_lang)


print("\nAufgabe 4")
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for zahl in zahlen:
    # Bei geraden Zahlen ergibt die Modulo 2 Operation immer 0
    # => Unterscheidungskriterium
    if zahl%2 == 0:
        print(zahl, end=" ")
        # mit dem end-parameter kann bestimmt werden, wie der string endet
        # (default: "\n" , also ein Zeilenumbruch)
        # Deswegen gibt jedes print normalerweise auf einer neuen Zeile aus.


print("\nAufgabe 5")
gerade = []
ungerade = []
for zahl in zahlen:
    if zahl%2 == 0:
        gerade.append(zahl)
    else:
        ungerade.append(zahl)
print(f"Gerade:   {gerade}")
print(f"Ungerade: {ungerade}")


print("\nAufgabe 6")
names = []
for i in range(5):
    name = input("Geben Sie einen Namen ein: ")
    names.append(name)
print(f"Liste der Namen: {names}")