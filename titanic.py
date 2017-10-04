import csv

dataList = []
with open('./train.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        dataList.append(row)

people = []

for row in dataList:
    dic = {}
    dic['PassengerId'] = row[0]
    dic['Survived'] = row[1]
    dic['Pclass'] = row[2]
    dic['Name'] = row[3]
    dic['Sex'] = row[4]
    dic['Age'] = row[5]
    dic['SibSp'] = row[6]
    dic['Parch'] = row[7]
    dic['Ticket'] = row[8]
    dic['Fare'] = row[9]
    dic['Cabin'] = row[10]
    dic['Embarked'] = row[11]
    people.append(dic)

for person in people:
    if person['Name'] == 'Name':
        people.remove(person)

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
        peeps.append([int(float(person['Age'])//10), person['Sex'], int(person['Pclass'])])
    except:
        continue
print sorted(peeps)
