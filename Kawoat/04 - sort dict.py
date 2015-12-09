def sort_dict(kind, year):
    from collections import OrderedDict
    import csv
    with open('data.csv') as file:
        stream = csv.reader(file)
        coal = {}
        gas = {}
        water = {}
        lst = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] #01 = January - 12 = December
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
        #sort dict by key
        if kind  == 'coal':
            coal1 = OrderedDict(sorted(coal[year].items()))
            coal1 = [float(i) for i in coal1.values()]
            return coal1
        elif kind == 'gas':
            gas1 = OrderedDict(sorted(gas[year].items()))
            gas1 = [float(i) for i in gas1.values()]
            return gas1
        elif kind  == 'water':
            water1 = OrderedDict(sorted(water[year].items()))
            water1 = [float(i) for i in water1.values()]
            return water1
print(sort_dict(input(), input()))
