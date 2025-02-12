# Aufgabe 1
even_schedule = {"100m": "10am",
                 "long Jump": "11am"}

# Aufgabe 2
performers = {
    "100m": ["Usain bolt", "Daniel", "Marco"],
    "Jumping": ["Usain bolt", "Daniel", "Marco"]
}

# Aufgabe 3

medal = {"100m": [["Usain Bolt",  "Jamaica"],
                  ["Marco", "Germany"],
                  ["Jon", "USA"]]
         }

medal = {"100m": [{"name": "Usain Bolt", "country": "Jamaica"},
                  {"name": "Marco", "country": "Germany"},
                  {"name": "Jon", "country": "USA"}]
         }

medal = {"100m":
             {"Gold": ["Usain Bolt",  "Jamaica"],
              "Silver": ["Marco", "Germany"],
              "Bronze": ["Jon", "USA"]}
         }

medal = {"100m":
             {"Gold": {"name": "Usain Bolt", "country": "Jamaica"},
              "Silver": {"name": "Marco", "country": "Germany"},
              "Bronze": {"name": "Jon", "country": "USA"}}
         }

# Aufgabe 4
athlete_bio = {"123":
                   {"name": "Usain Bolt",
                    "Medals": "12",
                    "Age": "23"}
               }
athlete_bio = {"Usain Bolt": "description" }


# Aufgabe 5
event_scores = {"gymnastics":
                    {"vault":
                         {"PersonA": 12,
                          "PersonB": 8},
                     "floor_exercise":
                         {"PersonA": 12,
                          "PersonB": 8}
                     }
                }


# Aufgabe 6
Historical_medal = {"Spain" : {2024:
                                   {"Gold": 34,
                                    "Silver": 45,
                                    "Bronze": 67},
                               2020:
                                   {"Gold": 14,
                                    "Silver": 35,
                                    "Bronze": 67}
                               }
                    }
