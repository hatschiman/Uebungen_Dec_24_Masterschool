movies_prices = {"Inception": 12,
                 "Avatar": 15,
                 "Moana": 8}

# Einträge hinzufügen und ändern
movies_prices["Dune"] = 15
movies_prices["Inception"] = 10

# Ausgabe der Filmtitel (als Liste)
print("\nFilmtitel: ")
print(list(movies_prices))

# Formatierte Ausgabe von Film und Preis
for movie, price in movies_prices.items():
    print(f"{movie} - ${price}")

# Funktionen
def add_movie(movie, price):
    if movie not in movies_prices:
        movies_prices[movie] = price
    else:
        print("Movie schon vorhanden")

def update_price(movie, price):
    if movie in movies_prices:
        movies_prices[movie] = price
    else:
        print("Movie nicht vorhanden")

print("\nAdd movie and update price:")
add_movie("Dune", 20)
update_price("Dune", 13)

def get_ticket_price(movie):
    if movie in movies_prices:
        print(f"Der Film {movie} kostet ${movies_prices[movie]}")
    else:
        print(f"Film ({movie}) nicht gefunden")

def delete_movie(movie):
    if movie in movies_prices:
        del movies_prices[movie]
    else:
        print(f"Film ({movie}) nicht gefunden")

print("\nGet ticket price and delete movie:")
get_ticket_price("Duneeeeee")
delete_movie("Avatar 2")

# Aufgabe 3 - Student Grades

print("\nAufgabe 3")
student_grades = {
    "Emma": [88, 92, 79],
    "Jonas": [76, 81, 85],
    "Ben": [90, 87, 93],
    "Felix": [72, 75, 70],
    "Lena": [95, 89, 91],
#    "Coward":[92, 92, 92]  # Für Testzwecke, wenn zwei Topstudenten gleichauf
}

# Ausgabe der besten Note des jeweiligen Studenten:
# Hier nutzen wir die eingebaute max()-Funktion von Python, die uns den
# größten Wert einer Liste zurückgibt
print("Ausgabe der besten Note der Studenten: ")
for student, grades in student_grades.items():
    print(f"{student}: {max(grades)}")

print("\nAusgabe der Durchschnittsnote der Studenten: ")
# Hier wird die Summe (sum()) durch die Länge der Liste geteilt und
# dann mit round() gerundet
for student, grades in student_grades.items():
    print(f"{student}: {round(sum(grades)/len(grades))}")

# Eine mögliche Lösung für die Funktion find_top_student:
# Es wird durch das Dictionaty iteriert und immer, wenn die Note größer ist als
# die vorhergehende werden die Variablen top_student und top_grade aktualisiert
# wenn die Note gleich ist, dann wird nur der Name des Studenten der
# top_student - Liste angehängt (für den Fall, dass zwei oder mehr Studenten
# die gleiche Bestenote haben
def find_top_student(student_grades):
    top_student = []
    top_grade = 0
    for student, grades in student_grades.items():
        mean_grade = round(sum(grades)/len(grades))
        if mean_grade > top_grade:
            top_grade = mean_grade
            top_student = [student]
        elif mean_grade == top_grade:
            top_student.append(student)
    return top_student, top_grade

print("\n Ausgabe des besten Studenten: ")
print(find_top_student(student_grades))
