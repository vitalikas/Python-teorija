a = [1, 15, 2, 6, 8, 77, 21, 14, 3, 55, 0]

# vyvesti znachenija, kotorye menshe 5:
# sposob nr. 1 s while:
i = 0
while i != len(a):
    if a[i] < 5:
        print(a[i])
    i = i+1

# sposob nr. 2 s for:
for elem in a:
    if elem < 5:
        print (elem)

# sposob nr. 3 v massiv:
print([elem for elem in a if elem < 5])


b = [124, 255, 101, 100, 459, 444, 368, 237, 125, 128,
     300, 412, 438, 388, 365, 207, 124, 299, 303, 411]

# vyvesti vse chiotnye znachenija i, esli vstretitsia chislo 237, to ostanovitsia:
for elem in b:
    if elem == 237:
        break
    if elem % 2 == 0:
        print(elem)

# podschitat i vyvesti kol-vo povtoriajushihsia znachenij:
from collections import Counter
c = Counter(b)
print(c.items())

# sposob cherez panda:
import panda as dp
dict(dp.value_counts(b))

# proverka na visokosnyj god:
yearStr = input("Какой сейчас год? ")

year = int(yearStr)
if year % 4 == 0:
    print(year,"- високосный")
else:
    print(year, "- обычный")