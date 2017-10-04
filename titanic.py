import csv

list = []
with open('/Users/aidanwhite/Desktop/train.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        list.append(row)

big_list = []

for row in list:
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
    big_list.append(dic)

print big_list