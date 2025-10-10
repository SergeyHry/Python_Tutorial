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
