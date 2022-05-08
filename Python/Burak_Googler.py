import webbrowser
google = input("Schreiben sie hier (suche) rein: ")

if google == "suche":
    webbrowser.open_new("https://google.com")
else:
    print("Bitte Programm erneut öffnen und (suche) reinschreiben")
