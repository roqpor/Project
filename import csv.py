import csv
with open('csv.csv') as file:
    test = csv.reader(file)
    for i in test:
        print(i)
