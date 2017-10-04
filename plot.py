import titanic
from matplotlib import pyplot as plt
from collections import Counter

people = titanic.people

print people

ages = []
Survived = []

for person in people:
    if person['Survived'] == '1':
        Survived.append(person['Survived'])
        if person['Age'] == "":
            continue
        else:
            ages.append(float(person['Age']))

#ages = ages[1:]
#Survived = Survived[1:]
print ages
print Survived

c = Counter(ages)

print c


plt.bar(c.keys(), c.values())
plt.show()




