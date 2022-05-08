import time
# Ich habe keine andere Lösung gefunden als "time.time" zu nutzen.

points = 0
name = input("Was ist dein Name: ")


start_time = time.time()
Frage1 = input("Was ist 1+1: ")
if Frage1 == "2":
    points += 1
    print("Das ist richtig! ")
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = int(end_time - start_time)
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")
print("")
print("")
start_time = time.time()
Frage2 = input("Was ist 2+2: ")
if Frage2 == "4":
    print("Das ist richtig! ")
    points += 1
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = end_time - start_time
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")
print("")
print("")
start_time = time.time()
Frage3 = input("Was ist 3+3: ")
if Frage3 == "6":
    print("Das ist richtig! ")
    points += 1
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = end_time - start_time
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")
print("")
print("")
start_time = time.time()
Frage4 = input("Was ist 3x3: ")
if Frage4 == "9":
    print("Das ist richtig! ")
    points += 1
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = end_time - start_time
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")
print("")
print("")
start_time = time.time()
Frage5 = input("Was ist 5x5: ")
if Frage5 == "25":
    print("Das ist richtig! ")
    points += 1
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = end_time - start_time
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")
print("")
print("")
start_time = time.time()
Frage6 = input("Was ist 9x9: ")
if Frage6 == "81":
    print("Das ist richtig! ")
    points += 1
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = end_time - start_time
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")
print("")
print("")
start_time = time.time()
Frage7 = input("Was ist 10/2: ")
if Frage7 == "5":
    print("Das ist richtig! ")
    points += 1
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = end_time - start_time
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")
print("")
print("")
start_time = time.time()
Frage8 = input("Was ist 21/7: ")
if Frage8 == "3":
    print("Das ist richtig! ")
    points += 1
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = end_time - start_time
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")
print("")
print("")
start_time = time.time()
Frage9 = input("Was ist 81/9: ")
if Frage9 == "9":
    print("Das ist richtig! ")
    points += 1
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = end_time - start_time
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")
print("")
print("")
start_time = time.time()
Frage10 = input("Was ist 10x10: ")
if Frage10 == "100":
    print("Das ist richtig! ")
    points += 1
else:
    print("Das ist leider falsch!")
end_time = time.time()
duration = end_time - start_time
if duration > 30:
    print("Du warst nicht schnell genug, und damit zählt es nicht! ")

print(name, "Du hast " + str(points) + " Punkte erreicht.")
print("")
print("")
input("Drücke die Enter Taste zum beenden! ")