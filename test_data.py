import csv

def get_test_peeps():
    dataList = []
    with open('./test.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            dataList.append(row)

    people = []
    header = True

    for row in dataList:
        if not header:
            dic = {}
            dic['PassengerId'] = int(row[0])
            dic['Pclass'] = int(row[1])
            dic['Name'] = row[2]

            if row[3] == "male":
                dic['Sex'] = 0
            else:
                dic['Sex'] = 1

            try:
                dic['Age'] = float(row[4])
            except:
                dic['Age'] = -1

            dic['FamSize'] = int(row[5]) + int(row[6])
            dic['Ticket'] = row[7]
            try:
                dic['Fare'] = float(row[8])
            except:
                dic['Fare'] = -1
            dic['Cabin'] = row[9]
            dic['Embarked'] = row[10]
            people.append(dic)

        else:
            header = False

    test_peeps = []
    for person in sorted(people):
        if person["Age"] == -1:
            continue
        test_peeps.append([int(float(person['Age'])//10), person['Sex'], int(person['Pclass'])])

    return test_peeps
