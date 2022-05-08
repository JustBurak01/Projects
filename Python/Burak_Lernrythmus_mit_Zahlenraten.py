import time
import webbrowser
start_time = time.time()



def zahlenraten():
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


pausen = input("Gib ein wieviele Pausen du haben möchtest: ")
pausen_zähler = 0
x = input("Gib an wann alle x Sekunden eine Pause sein soll in Sekunden: ")
y = input("Gib an wie lange die Pause sein soll in Sekunden: ")
start_time

while int(pausen_zähler) < int(pausen):
    time.sleep(int(x))
    webbrowser.open("https://i.giphy.com/media/zmmIYDnHJzuEI60dVd/giphy.webp")
    pausen_zähler = pausen_zähler + 1
    print("Deine Pausen Anzahl beträgt " + str(pausen_zähler) + "!")
    end_time = time.time()
    duration = int(end_time - start_time)
    print("Du arbeitest seit " + str(duration ) + " Sekunden.")
    time.sleep(int(y))
    warmup = input("Willst du ein kleines Warm Up spielen,schreibe ja oder nein: ")
    if warmup == "ja":
        zahlenraten()
    elif warmup == "nein":
        print("Ok dann wünsche Ich dir viel Spaß.")
    Beenden = input("Möchtest du das Programm beenden? schreibe ja oder nein: ")
    if Beenden == "ja":
        quit()
    elif Beenden == "nein":
        print("Ok dann noch viel Spaß! ")
        continue



