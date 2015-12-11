import csv
with open('csv.csv') as file:
    stream = csv.reader(file)
    coal = {}
    gas = {}
    water = {}
    lst = ['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec', 'elect per year', 'price', 'capital']
    for num, i in enumerate(stream):
        if num == 0:
            continue
        if num == 1 or num == 2 or num == 3:
            coal[i[1]] = dict()
            for a, each in enumerate(lst):
                coal[i[1]][each] = i[a+2]
        elif num == 4 or num == 5 or num == 6:
            gas[i[1]] = dict()
            for a, each in enumerate(lst):
                gas[i[1]][each] = i[a+2]
        elif num == 7 or num == 8 or num == 9:
            water[i[1]] = dict()
            for a, each in enumerate(lst):
                water[i[1]][each] = i[a+2]
    kind = input()
    kindd = eval(kind)
    year = input()
    month = input()
    print(kind, 'month', month, 'year', year, ':', kindd[year][month])
    print('electric per year', ':', kindd[year]['elect per year'])
    print('price', ':', kindd[year]['price'])
    print('capital', ':', kindd[year]['capital'])
