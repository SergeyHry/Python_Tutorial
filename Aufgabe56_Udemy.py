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
            count = count  + (int(liste[4]))
plt.title("name Max (Male)")
plt.fill_between(xs, ys)
plt.show()
print (count)

listSlice = ["Maximilian", "Erik", "Kolen"]

liste2 = [li* 2 for li in listSlice]
print(liste2)
liste2 = [len(st) for st in listSlice]
print(liste2)

d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}
print(d)
print(d.get("Singapur"))
t = ["Koala", 15, True,5.99]

for key in d:
    value = d[key]
    print(key,"/ ",  value)
for key, value  in d.items():
    print(key, "/", value)
count = 0


with open("C:/Users/Student/Desktop/export.csv", "r") as file:
    dict = {"name":"", "year": "", "vergeben": 0}
    summe = 0
    for f in file:
        liste = f.strip().split(";")
        if liste[2] == "1880":
            verg = int(liste[4])
            name = liste[1]
            summe = summe + verg
            if verg > dict["vergeben"]:
                dict = {"name": name, "year": liste[2], "vergeben": verg}
    print(dict)
    print(summe)


