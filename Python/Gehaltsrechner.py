stundenlohn = input("Bitte gebe deinen Stundenlohn an: ")
tag = 8 * int(stundenlohn)
monat = 20 * tag
year = monat * 12

print("Dein Stundenlohn beträgt " + str(stundenlohn) + "€")
print("Du verdienst " + str(tag) + "€ pro Tag")
print("Du verdienst " + str(monat) + "€ pro Monat")
print("Du verdienst " + str(year) + "€ im Jahr")

input("Bitte drücke die Enter Taste zum schließen")
