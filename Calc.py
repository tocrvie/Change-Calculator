###### Eingabeaufforderung 

kosten = float(input("Eingabe Produktkosten : "))
moneyGiven = float(input("Eingabe Zahlungssumme : "))
deltaMoney = moneyGiven - kosten
while deltaMoney <0:
    print("du hast zu wenig gezahlt!")
    moneyGiven = input("Eingabe Zahlungssumme : ")
    deltaMoney = moneyGiven - kosten


####### Hard coded - Wähung  -Euro €
moneyListe = [  50,
                20,
                10,
                5,
                2,
                1,
                0.50,
                0.20,
                0.10,
                0.05,
                0.02,
                0.01
             ]

changeMoney={  "50 Euro"    : "0",
        "20 Euro"    : "0", 
        "10 Euro"    : "0", 
        "5 Euro"     : "0",
        "2 Euro"     : "0",
        "1 Euro"    : "0",
        "0.5 Euro"  : "0",
        "0.2 Euro"  :  "0",
        "0.1 Euro"   : "0",
        "0.05 Euro"    : "0",
        "0.02 Euro"    : "0",
        "0.01 Euro"    : "0"
    }

# Calculation + Adds lib + shows lib
print("Wechselgeld : ")

for i in moneyListe:
    if i<=deltaMoney:
        count = round(float(deltaMoney/i),5)
        deltaMoney = deltaMoney%i
        changeMoney[str(i)+" Euro"] = int(count)


for name, anzahl in changeMoney.items():
    if int(anzahl) >0:        
        print(str(name) +": " + str(anzahl))

    
