## Beispiel 1: fehlerhafte Funktion

def add_underscores(word):
    new_word = "_"
    for char in word:
        # new_word = char + "_"  # diese Zeile war im Original und fehlerhaft
        new_word = new_word + char + "_"
        # oder: new_word += char + "_"
        print(new_word)
    return new_word


phrase = "hello"
print(add_underscores(phrase))


## Beispiel 2: Finde heraus, welche Funktion fehlerhaft ist
#  Dies geht am leichtesten, indem man die Zwischenergebnisse ausgibt

def only_even_nums(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

def lowest(list_nums):
    min = 0
    for num in list_nums:
        if num < min:
            min = num
    return min

list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Erhalte eine Liste mit ausschließlich geraden Zahlen
list_even = only_even_nums(list_nums)
print(list_even)


lowest = lowest(list_even)
print(lowest)