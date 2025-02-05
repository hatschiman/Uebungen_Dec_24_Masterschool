# Erstellen eines Dictionaries
my_dict = {"key_1": "value_1"}

print(my_dict["key_1"])

# Hinzufügen eines Wertes
my_dict["key_2"] = "value_2"
print(my_dict)

# Werte aus dem Dictionary entfernen
del my_dict["key_1"]
print(my_dict)

# Werte modifizieren
my_dict["key_2"] = "Neuer Wert"
print(my_dict)

# Member checking
print("key_2" in my_dict)


# Loopen über dict
my_dict = {"key_1": "value_1"}
my_dict["key_2"] = "value_2"

for key in my_dict:
    print(key)
    print(my_dict[key])

for key in my_dict.keys():
    print(key)
    print(my_dict[key])

keys_liste = my_dict.keys()
print(list(my_dict.keys()))

for value in my_dict.values():
    print(value)



for key, value in my_dict.items():
    print(key, value)
print(my_dict.items())



a, b = (1, 2)

print(a)
print(b)

dict_2 = {1:"Eins", 2:"Zwei", 3:None}

auto = {"Marke": "VW", "Modell": "Thunderstorm", "Jahr":"2026"}
auto["Kraftstoff"] = "Wasserstoff in Kernfusion"
auto["Jahr"] = 3026

for key, value in auto.items():
    print(f"Key: {key}, Value: {value}")

print(auto)