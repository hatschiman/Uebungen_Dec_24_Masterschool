## Aufgabe 2
# Das return-Statement in der For-Schleife sorgt dafür, dass die SChleife schon
# nach dem ersten Durchlauf abgebrochen und ein Wert zurückgegeben wird, da
# ein return auch immer das Ende bzw. den Abbruch einer Funktion bedeutet

def sum_of_nums(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
        # return sum # alte, fehlerhafte Zeile
    return sum

numbers = [1,42,7]
print(sum_of_nums(numbers))