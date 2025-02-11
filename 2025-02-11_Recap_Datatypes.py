# Folgender Code war gedacht als Beispiel für die Verwendung von None in
# Python. Generell nutzt man None, um ein Fehlen eines Wertes auszudrücken


# Zum Beispiel hier in der Liste ist an der vierten Stelle ein fehlender Wert,
# None dient hier als Platzhalter und zeigt an, dass hier ein Wert stehen
# sollte
liste_zahlen = [1, 3, 4, None, 56, 7]

# Weiteres Beispiel: Funktionen, die keinen expliziten return-Wert definiert
# haben, wie hier, geben per standardmäßig None zurück.
def my_func():
    print("Hallo")

print(my_func())

# Noch ein Beispiel für ein Dictionary, dass bestimmt Automarken als Key und
# entsprechende Autotypen in einer Liste gespeichert als Value enthalten.
# Unter dem Key Opel finden wir den Wert None, der darauf hinweist, dass an
# dieser Stelle z.B. keine Autos verfügbar sind.
meine_autos = {"VW": ["Polo", "Touran"],
               "Mercedes": ["A-Klasse"],
               "Opel": None}


# Aufgabe: Welcher Datentyp für die Verwendung der Siegreihenfolge von
# Sprintern?
# Antwort: Da die Namen geordnet in Reihenfolge gespeichert werden
# sollen, bietet sich die Liste als Datentyp zu Speicherung an, da sie
# dies aufgrund ihrer geordneten Struktur schon beinhaltet.
reihenfolge_list = ["RunnerB", "RunnerC", "RunnerA"]

# Es ist nicht falsch, das Ganze als Dictionary zu speichern, jedoch
# ist es deutlich umständlicher und auch unnötig.
reihenfolge_dict = {"RunnerA": 3, "RunnerB": 1, "RunnerC": 2}
# reihenfolge_dict = {3: "RunnerA"....

# Aufgabe: Speichere die Anzahl an Gold, Silber und Bronzemedaillen der Länder.
# Hier bietet sich eine verschachtelte Speicherung in einem Dictionary an,
# wobei Ländern oder Medaillenfarbe als primäre Keys sinnvoll sind.
medaillen = {"germany": {"gold": 1,  "silber": 3, "bronze": 6},
             "austria": None}
print(medaillen["germany"]["gold"])

medaillen = {"gold": {"germany": 1, "austria": None},  # [gold, silver, bronze]
             "silver": {"germany": 3, "austria": None},
             "bronze": {"germany": 6, "austria": None}}
print(medaillen["gold"]["germany"])
# Wenn man sich weiß, welche Positionen den jeweiligen Medaillenfarben
# entsprechen, kann man als innere Struktur auch eine Liste verwenden:
medaillen = {"germany": [1, 3, 6],  # [gold, silver, bronze]
             "austria": None}
print(medaillen["germany"][1])
# Anmerkung: None könnte hier zum Beispiel anzeigen, dass Österreich noch nicht
# fertig ist mit den Wettbewerben und die Daten später eingefügt werden.

# Zur Verschachtelung komplexer Datentypen:
# Da es erlaubt ist, komplexe Datentypen (Liste, Tupel, Dictionary) ineinander
# einzusetzen, ergibt sich die Problematik des Zugriffs auf die Elemente in
# ihnen. Dies wird erreicht durch verketteten Zugriff mittels Index in eckigen
# Klammern. Dabei wird auf die Elemente von außen nach innen zugegriffen.

nested_list = [[1, 2], [3, 4], [5, 6], [7, 8], [[9, 10], [11, 12]]]

# Zugriff auf die Zahl 6: Diese befindet sich in der dritten Liste innerhalb
# der übergeordneten Liste, und in dieser dritten Liste ist sie das zweite
# Element
# Zugriff auf die dritte Liste:
sublist = nested_list[2]
# Zugriff auf zweites Element der dritten Liste:
number_6 = sublist[1]
# Oder zusammengeschrieben:
number_6 = nested_list[2][1]

# Weiteres Beispiel: Zugriff auf das Element 12 in der verschachtelten Liste
# Hier finden wir eine zusätzliche Ebene der Verschachtelung
# Zugriff auf die fünfte Unterliste:
sublist = nested_list[4]
# davon Zugriff auf die zweite Unterunterliste
subsublist = sublist[1]
# Zugriff auf zweites Element der Unterunterliste:
number_12 = subsublist[1]

# Oder zusammengeschrieben:
number_12 = nested_list[4][1][1]


# Tupel: Sehr ähnlich zum Datentyp Listen mit dem wichtigen Unerschied, dass
# Tupel im Gegensatz zu Listen immutable (unveränderlich) sind. Das heißt,
# Wenn sie einmal definiert ist, kann sie nicht mehr verändert werden.
# Sie werden definiert durch runde Klammern

# Man kann in Listen Elemente ändern, anhängen, entfernen
meine_liste = [1, 2, 3, 4, 5]
meine_liste[1] = 0
meine_liste.append(6)
meine_liste.pop()

# die gleichen Operationen werden bei Tupeln Fehler aufwerfen
# (deswegen an dieser Stelle auskommentiert
meine_tupel = (1, 2, 3, 4, 5)
# meine_tupel[1] = 0
# meine_tupel.append(6)
# meine_tupel.pop()

# Würde man das Tupel ändern wollen, müsste man der Variable ein neues Tupel
# zuweisen, welches die Änderungen enthält. An dieser Stelle empfiehlt es sich
# allerdings, eine Liste zu verwenden, da Tupel für diesen Anwendungszweck
# nicht gedacht sind. Tupel verwendet man normalerweise, wenn man weiß, dass
# sich die Elemente in ihm nicht ändern werden und man stellt so sicher, dass
# sie es auch nicht können.
mein_tupel = (1, 0, 3, 4, 5)