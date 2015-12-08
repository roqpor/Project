import csv
with open('csv2.csv') as file:
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
    year = input()
    month = input()
    if kind == 'coal':
        print('ถ่านหิน', 'month', month, 'year', year, ':', coal[year][month])
        print('electric per year', coal[year]['elect per year'])
        print('price', coal[year]['price'])
        print('capital', coal[year]['capital'])
    elif kind == 'gas':
        print(gas[year][month])
        print('electric per year', gas[year]['elect per year'])
        print('price', gas[year]['price'])
        print('capital', gas[year]['capital'])
    elif kind == 'water':
        print(water[year][month])
        print('electric per year', water[year]['elect per year'])
        print('price', water[year]['price'])
        print('capital', water[year]['capital'])
        
