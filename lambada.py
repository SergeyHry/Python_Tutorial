import re

sent = "Hallo meine liebe Heute habe ich 30 Pushups gemacccccht und hat 2 l Wasser getrunken!"

print(re.findall("[0-9]+", sent))
print(re.search("gemac?", sent))
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28), ("Anton", 21)]
sorted_students = sorted(students, key=lambda x: x[0])
print(sorted_students)
lengths = map(str, sorted_students)
print(list(lengths))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

for number in numbers:
    print(number)

