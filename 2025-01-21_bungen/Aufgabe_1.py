## Aufgabe 1
# Da eine Division durch 0 nicht möglich ist, muss die zweite Nummer undgleich
# 0 sein und nicht gleich - sonst entsteht ein Fehler

def simple_calculator(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
        # if num2 == 0:  # alter, fehlerhafte Zeile
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero!")
            return
    else:
        print("Invalid operation!")
        return

    print(f"Result: {result}")


simple_calculator(15, 3, '/') # should be 5.0