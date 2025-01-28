from os import MFD_ALLOW_SEALING

a = True
b = False

a = 1
b = 4

print("Vergleichsoperatoren bei Werten")
print(f"a = {a}")
print(f"b = {b}")
print(f"a == b -> {a == b}")
print(f"a != b -> {a != b}")
print(f"a > b -> {a > b}")
print(f"a < b -> {a < b}")
print(f"a >= b -> {a >= b}")
print(f"a <= b -> {a <= b}")


print(f'"t" in "test" -> {"t" in "test"}') # Membership-Operator

print(f"True < False -> {True < False}")

# logische Operatoren

print("\nLogisch AND")
print(f"True and True -> {True and True}")
print(f"True and False -> {True and False}")
print(f"False and True -> {False and True}")
print(f"False and False -> {False and False}")

print("\nLogisch OR")
print(f"True or True -> {True or True}")
print(f"True or False -> {True or False}")
print(f"False or True -> {False or True}")
print(f"False or False -> {False or False}")

print("\nNOT - Negierung")
print(f"not True -> {not True}")
print(f"not False -> {not False}")

print("\nVerschachtelungen")
print("not False or False and False or True ->")
print(not False or False and False or True)
print("not (False or False) and (False or True) ->")
print(not (False or False) and (False or True))

"""Wir wollen eine Funktion schreiben, die checkt,
ob alle Zahlen in einer Liste größer als 100 sind"""
## Lazy Variante
def are_all_nums_bigger_100(numbers):
    for zahl in numbers:
        if zahl <= 100:
            return False
    return True

## Komplizierte Variante:
def are_all_nums_bigger_100(numbers):
    true_false_list = []
    for zahl in numbers:
        if zahl <= 100:
            true_false_list.append(False)
        else:
            true_false_list.append(True)
    if False in true_false_list:
        return False
    else:
        return True

print("\nFunktion are_all_nums_bigger_100")
print(are_all_nums_bigger_100([122, 100, 222]))



fridge = ["a", "b", "c"]

## Beispiellösung für die Back-Aufgabe
# Diese Funktion überprüft, ob alle Elemente aus liste in
# container enthalten sind und wird dann in der nächsten
# Funktion verwendet

fridge = ["a", "b", "c"] # vorhandene Zutaten

def contains_all(liste, container):
    for item in liste:
        if item not in container:
            return False
    return True

# Hier wird überprüft, wo die Zutaten passen und am Ende
# ein String ausgegeben, der mehrzeilig ist.
# Mehrzeilige Strings sind mit dreifachem Anführungszeichen
# markiert und speichern Zeilenumbrüche.
def which_cake(ingredients):
    # benötigte Zutaten:
    banana = ["a", "c", "d"]
    cheese_cake = ["a", "b", "c"]
    chocolate = ["a", "d", "e"]
    return f"""Bananenkuchen: {contains_all(ingredients, banana)}
Cheese Cake: {contains_all(ingredients, cheese_cake)}
Schokoladencookie: {contains_all(ingredients, chocolate)}"""

print(which_cake(fridge))