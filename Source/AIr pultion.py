import csv
with open("C:/Users/Oliver/Hack.txt") as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)

name = (d[4][2:7])
length = len(name)
result = 0

name2 = list(map(float, name))
length = len(name2)
for i in range(length):
    result = sum(map(float,name))

print(result)
