

from unicodedata import digit

#while
counter = 0
while counter < 10:
    print(counter)
    counter += 1
#for
for i in range (0,10):
    print(i)

#Aufgabe 1
chaos = ["old preise: 20", "new preise: 49", "old preise: 40", "new preise: 80"]
preislist = []
for i in chaos:
    preise = int(i.split(":")[1])
    print(i)
    if "old" in i:
        if preise <= 20:
            preise = preise *0.8
        elif preise <= 49:
            preise = preise * 0.5
    preislist.append(preise)
print(preislist)
print("/".join(chaos))
#Aufgabe 2

for i in range (5):
    print()
    j = 0
    while j<=i:
        print("*", end=" ")
        j+=1

#Aufgabe 3
print()
i = 6
while i>=0:
    print("")
    i -= 1
    for j in range (0,i):
        print("*", end=" ")
print()
#Aufgabe 4
for i in range (5):
    leer = " " * (5-i)
    sterne = "*" * (2*i-1)
    print(leer + sterne)
#aufgabe 4
index = 0
abc = "abcdefghijklmnopqrstuvwxyz"
for i in range(5):
    for j in range(5):
        if index < len(abc):
            print(abc[index], " ",  end="")
            index += 1
    print()

menge = []
datei = int(input("wie viele Datenträger?"))
for i in range(datei):
    datei2 = int(input(f"geben Sie die Größe der Datei {i+1} in KB"))
    menge.append(datei2)
    menge[i] /= 1000000
print(f"Die gesamtgröße der Dateien  beträgt: {sum(menge)} GB")


