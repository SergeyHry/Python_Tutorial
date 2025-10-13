import matplotlib.pyplot as plt
with open("text.txt", "a") as file:
    students = ["Endy", "Carol", "Luis", "Paul", "Lucia"]
    for student in students:
        file.write(student)
daten_liste = []

with open("C:/Users/Student/Desktop/Kostenplan_Vorlage.csv", "r") as file:
    for line in file:
        e = line.strip().split(";")
        eintrag = {
            "id": e[0],
            "name": e[1],
            "alter": e[2]
        }
        daten_liste.append(eintrag)

print(daten_liste[2])
xs = [1,2,5,6,7,8,9]
ys = [1,12.5,20,5,10,2.5,7.5]
plt.title("Mein Grafik")
plt.bar(xs, ys)
plt.plot(xs, ys)
plt.show()