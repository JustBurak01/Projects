name = input("Wie heißt du denn?: ")

print("Hallo " + name + ", Ich hoffe dir geht es gut.")
print("")

city = input("Aus welcher Stadt kommst du?: ")

print("Die Stadt " + city + ", soll sehr schön sein :)" + ".")
print("")

while True:
    feeling = input("Wie geht es dir, eher gut, oder eher schlecht? ").lower()
    if feeling == "gut":
        print("Oh, dann hast du ja noch genügend Energie, um durch den Tag zu kommen" + ".")
        break
    elif feeling == "schlecht":
        print("Dann würde ich dir raten, erstmal eine Pause zu machen von allem" + ".")
        break
    else:
        print("Könntest du es bitte nochmal hinschreiben?")




print('')
print('')
print("Ich wünsche dir noch einen schönen Tag, und hoffe du kannst ihn genießen")
print('')
print('')
input("Bitte die Enter Taste drücken zum schließen" + ".")
