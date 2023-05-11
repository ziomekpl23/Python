print("Witaj w grze pt.kamień, papier,nozyce")

import random
user_action = input("wykonaj ruch (kamien, papier, nozyce): ")
possible_actions = ["kamien", "papier", "nozyce"]
computer_action = random.choice(possible_actions)
if user_action == computer_action:
    print(f"Oboje gracze uzyli {user_action}. Remis!")
elif user_action == "kamien":
    if computer_action == "nozyce":
        print("kamien zmiazdzyl nozyce! Wygrales!")
    else:
        print("Papier zakryl kamien! przegrales.")
elif user_action == "papier":
    if computer_action == "kamien":
        print("papier zakryl kamien! wygrales!")
    else:
        print("nozyce pociely papier! przegrales.")
elif user_action == "nozyce":
    if computer_action == "papier":
        print("nozyce sciely papier! Wygrales!")
    else:
        print("kamien zmiazdzyl nozyce! przegrales.")
