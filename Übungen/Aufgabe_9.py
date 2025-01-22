## Aufgabe 9
# Hier in dieser Aufgabe entsteht der Fehler durch das spezifische Verhalten
# der sorted-Funktion, die Groß- und Kleinbuchstaben gesondert behandelt.
# Das kann man umgehen, indem man vorher alle Buchstaben auf eine Größe
# konvertert

def are_anagrams(word1, word2):
    word1_chars_sorted = sorted(word1) # Hier entsteht das Problem
    word2_chars_sorted = sorted(word2) # Hier entsteht das Problem
    word1_chars_sorted = sorted(word1.upper())
    word2_chars_sorted = sorted(word2.upper())
    sorted_word1 = ''.join(word1_chars_sorted)
    sorted_word2 = ''.join(word2_chars_sorted)
    return sorted_word1 == sorted_word2

print(are_anagrams('Silent', 'Listen'))  # should be True, but gives False