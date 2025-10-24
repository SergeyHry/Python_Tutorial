import re

sent = "Hallo meine liebe Heute habe ich 30 Pushups gemacccccht und hat 2 l Wasser getrunken!"

print(re.findall("[0-9]+", sent))
print(re.search("gemac?", sent))
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28), ("Anton", 21)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
lengths = map(str, sorted_students)
print(list(lengths))
numbers = [i for i in range(1, 31)]
print(numbers[::-1])

print(numbers[3])

c  = lambda x, y: x**y / 100
print (c(2,16))
