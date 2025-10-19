import matplotlib.pyplot as plt
with open("text.txt", "a") as file:
    students = ["Endy", "Carol", "Luis", "Paul", "Lucia"]
    for student in students:
        file.write(student)
daten_liste = []
graf = []

with open("C:/Users/Student/Desktop/Kostenplan_Vorlage.csv", "r") as file:
    for line in file:
        e = line.strip().split(";")
        graf.append(int(e[2]))
        eintrag = {
            "id": e[0],
            "name": e[1],
            "alter": e[2]
        }






