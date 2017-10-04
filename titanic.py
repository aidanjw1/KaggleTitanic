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
        dic['PassengerId'] = row[0]
        dic['Survived'] = row[1]
        dic['Pclass'] = row[2]
        dic['Name'] = row[3]
        dic['Sex'] = row[4]
        dic['Age'] = row[5]
        dic['FamSize'] = int(row[6]) + int(row[7])
        dic['Ticket'] = row[8]
        dic['Fare'] = row[9]
        dic['Cabin'] = row[10]
        dic['Embarked'] = row[11]
        people.append(dic)

    else:
        header = False


for person in people:
    if person['Sex'] == "male":
        person['Sex'] = 0
    else:
        person['Sex'] = 1

print people

def get_target_list():
    target_list = []
    for person in sorted(people):
        try:
            target_list.append(int(person['Survived']))
        except:
            print person['Survived']

    print target_list
    return target_list

peeps = []
for person in sorted(people):
    try:
        peeps.append([person['Sex'], person['Pclass'], float(person['Age'])//10])
    except:
        continue
