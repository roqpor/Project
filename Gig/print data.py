import csv
with open('data.csv') as file:
    stream = csv.reader(file)
    coal = {}
    gas = {}
    water = {}
    lst = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', \
           'september', 'october', 'november', 'december', 'electric per year', 'price', 'capital']
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
        print('fuel', ':', kind)
        print('month', ':', month)
        print('year', ':', year)
        print('productivity', ':', coal[year][month], 'million units')
        print('electric per year', ':', coal[year]['electric per year'], 'million units')
        print('price', ':', coal[year]['price'], 'per unit')
        print('cost per year', ':', coal[year]['capital'], 'million bath')
    elif kind == 'gas':
        print('fuel', ':', kind)
        print('month', ':', month)
        print('year', ':', year)
        print('productivity', ':', gas[year][month], 'million units')
        print('electric per year', ':', gas[year]['electric per year'], 'million units')
        print('price', ':', gas[year]['price'], 'per unit')
        print('cost per year', ':', gas[year]['capital'], 'million bath')
    elif kind == 'water':
        print('fuel', ':', kind)
        print('month', ':', month)
        print('year', ':', year)
        print('productivity', ':', water[year][month], 'million units')
        print('electric per year', ':', water[year]['electric per year'], 'million units')
        print('price', ':', water[year]['price'], 'per unit')
        print('cost per year', ':', water[year]['capital'], 'million bath')
        
