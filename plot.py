import titanic
from matplotlib import pyplot as plt
from collections import Counter

people = titanic.people

def age_survivors():
    ages = []
    Survived = []

    dead = []
    age_dead = []

    fig, ax = plt.subplots(2)

    for person in people:
        if person['Survived'] == '1':
            Survived.append(person['Survived'])
            if person['Age'] == "":
                continue
            else:
                ages.append(float(person['Age']))

        elif person['Survived'] == '0':
            if person['Age'] == "":
                continue
            else:
                age_dead.append(float(person['Age']))


    #ages = ages[1:]
    #Survived = Survived[1:]
    print ages
    print Survived

    c = Counter(ages)
    c_dead = Counter(age_dead)

    print c


    ax[0].bar(c.keys(), c.values(), color='g')
    plt.xlabel("Age")
    plt.ylabel("Number of Survivors")
    plt.title("Ages of Titanic Survivors")
    fig.show()

    plt.bar(c_dead.keys(), c_dead.values())
    plt.xlabel("Age")
    plt.ylabel("Number of Deads")
    plt.title("Ages of Titanic Deads")
    fig.show()
    plt.show()

def sex_survivors():
    for person in people:
        males = 0
        females = 0
        if person['Survived'] == '1':
            if person['Sex'] == "male":
                males += 1
            elif person['Sex'] == 'female':
                females += 1
    print males
    print females

def main():
    age_survivors()
    #sex_survivors()

main()





