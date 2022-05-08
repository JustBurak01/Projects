import random
nummer = random.randint(1, 100)

player_name = input("Hallo wie lautet dein Name?: ")
versuche = 0
print("okay," + player_name + " Du kannst anfangen eine Zahl zwischen 1 und 100 zu erraten")

while versuche < 6:
    raten = int(input())
    versuche += 1
    if raten < nummer:
        print("Zu niedrig")
    if raten > nummer:
        print("Zu hoch")
    if raten == nummer:
        break
if raten == nummer:
        print("Du hast die Zahl in " + str(versuche) + " Versuchen erraten, und dir somit meinen Schatz verdient! ")
else:
        print("Du hast die Zahl nicht erraten die Zahl lautet: " + str(nummer))

input("Drücke die Enter Taste um das Programm zu schließen")
