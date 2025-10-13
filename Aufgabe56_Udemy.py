import matplotlib.pyplot as plt
with open("C:/Users/Student/Desktop/export.csv", "r") as file:
    li = []
    xs = []
    ys = []
    count = 0
    name = "Max"
    gender = "M"
    for f in file:
        liste = f.strip().split(";")
        if liste[1] == name and liste[3] == gender and (int(liste[2])) >=1950 and (int(liste[2])) <=2020:
            li.append(liste)
            xs.append(int(liste[2]))
            ys.append(int(liste[4]))
plt.title("name Max (Male)")
plt.fill_between(xs, ys)
plt.show()



