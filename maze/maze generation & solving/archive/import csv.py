import csv

with open('laby.csv','r') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)
for j in range (len(data)):
    for i in range(len(data[j])):
        if data[j][i]=='4999':
            data[j][i]=1
        if data[j][i]=='-1':
            data[j][i]=0
        if data[j][i]=='4954':
            data[j][i]=4
        if data[j][i]=='4904':
            data[j][i]=3
print(data)