import csv
import queue

try:
    with open("C:/Users/Student/Desktop/test.csv", "r", encoding="utf-8") as file:
        s=set()
        d = {}
        newQ = queue.PriorityQueue()
        counter = 0
        for line in file:
            e = line.split(";")
            s.add(e[1])
            d = {e[3]:e[1]}
        print(s, "Anzahl: ", len(s))
        print("Anzahl: ", counter)
        while not newQ.empty():
            print(newQ.get())
except FileNotFoundError:
    print("File not found")

l = queue.Queue()
for i in range(0,10):
    l.put(i)
while not l.empty():
    print(l.get())
names = {}
try:
    with open("C:/Users/Student/Desktop/export.csv", "r") as file:
        counter = 0
        for row in file:
            e = row.split(";")
            if counter!= 0:
                number = int(row[0])
                name = int(row[1])
                if name in names:
                    names[name] = number
                    print(row)
                    break
                counter = counter + 1
        print(names)
except FileNotFoundError:
    print("File not found")
def joke(hey = "Blablabla", intg = 2):
    for i in range (2,9):
        print(hey * i*intg)
joke(intg = 5, hey = "Bla")
def endern(var):
    return var.upper()[0:2]


go = "gogogogo"
print(go)
go = endern(go)
print(go)

li = [1,2,3,4,5,6,7]
print(*li)
