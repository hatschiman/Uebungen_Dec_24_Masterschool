## Aufgabe 7
# Hier in der Funktion wurden im Quelltext Klammern vergessen. Dies führt dazu,
# dass nicht der return-Wert der Funktion user_inut.lower() mit "yes"
# verglichen wird, sondern die Funktion selbst, was zu fehlerhaftem Verhalten
# führt.

def ask_user():
    user_input = input("Do you want to proceed? (yes/no): ")

    print(f"Fehlerhafter Zugriff auf Funktion: {user_input.lower}")
    print(f"Korrekter Zugriff auf Funktion:    {user_input.lower()}")

    # if user_input.lower == "yes":
    if user_input.lower() == "yes":
        print("Proceeding with the specific action...")
        # Add your specific action here
    else:
        print("No action taken.")

# Call the function
ask_user()