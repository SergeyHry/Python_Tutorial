import queue

try:
    with open("C:/Users/Student/Desktop/test.csv", "r", encoding="utf-8") as file:
        s=set()
        newQ = queue.PriorityQueue()
        for line in file:
            e = line.split(";")
            s.add(e[1])
            newQ.put(e[1])
        print(s, "Anzahl: " ,len(s))
        while not newQ.empty():
            print(newQ.get())

except FileNotFoundError:
    print("File not found")

l = queue.Queue()
for i in range(0,10):
    l.put(i)
while not l.empty():
    print(l.get())

