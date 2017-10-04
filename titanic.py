import csv

dataList = []
with open('./train.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        dataList.append(row)

people = []
header = True

for row in dataList:
    if not header:
        dic = {}
        dic['PassengerId'] = int(row[0])
        dic['Survived'] = int(row[1])
        dic['Pclass'] = int(row[2])
        dic['Name'] = row[3]

        if row[4] == "male":
            dic['Sex'] = 0
        else:
            dic['Sex'] = 1

        try:
            dic['Age'] = float(row[5])
        except:
            dic['Age'] = -1

        dic['FamSize'] = int(row[6]) + int(row[7])
        dic['Ticket'] = row[8]
        dic['Fare'] = float(row[9])
        dic['Cabin'] = row[10]
        dic['Embarked'] = row[11]
        people.append(dic)

    else:
        header = False

print people

def get_target_list():
    target_list = []
    for person in sorted(people):
        if person['Age'] == -1:
            continue
        try:
            target_list.append(int(person['Survived']))
        except:
            continue
    return target_list

target_list = get_target_list()

peeps = []
for person in sorted(people):
    try:
        peeps.append([int(float(person['Age'])//10), person['Sex'], int(person['Pclass'])])
    except:
        continue
print sorted(peeps)
