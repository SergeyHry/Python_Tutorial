people = ["Max", "Alessandro", "Sergey", "Timo", "Daniel"]
for person in people:
    people2 = ("/").join(people)
print(people2)
people.append("Favad")
peopleString = ", ".join(people)
print (peopleString)
print(peopleString.split(", "))

for i in (people):
    wieVieleBuchstaben = (len("".join(people)))
print(wieVieleBuchstaben)

def deleteElement(list, string):
    try:
        list = [l for l in list if l!= string]
        print(list)
    except ValueError as e:
        print("Value ist Falsch bitte liste und String  eingeben", e)
    except TypeError as e:
        print("Der Datentyp ist falsch")
    finally:
        print("das Element wurde entfernt.")


testList = ["Pepsi", "Fanta", "Cola", "Sprite"]
deleteElement(testList, "Pepsi")
try:
    people = {1: "Anna", 2: "Max", 3: "Tom"}
    for key in list(people.keys()):
        if people[key] == "Max":
            people.pop(key)
    for v in people.values():
        print(v +" ", end= "")
except Exception as e:
    print("so was geht nicht!", e)