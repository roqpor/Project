def add_dict(year, kind):
    from collections import OrderedDict
    import csv
    with open('data.csv') as file:
        stream = csv.reader(file)
        coal ={}
        gas = {}
        water = {}
        lst = ['1jan', '2feb', '3mar', '4apr', '5may', '6june', '7july', '8aug', '9sep', '10oct', '11nov', '12dec']
        for num, i in enumerate(stream):
            if num == 0:
                continue
            if num == 1 or num ==2 or num == 3:
                coal[i[1]] = dict()
                for a, each in enumerate(lst):
                    coal[i[1]][each] = i[a+2]
            elif num == 4 or num == 5 or num == 6:
                gas [i[1]] = dict()
                for a, each in enumerate(lst):
                    gas[i[1]][each] = i[a+2]
            elif num == 7 or num == 8 or num == 9:
                water[i[1]] = dict()
                for a, each in enumerate(lst):
                    water[i[1]][each] = i[a+2]
        #return list each kind that input
        if kind == 'coal':
            coal1 = coal[year].values()
            coal1 = [float(i) for i in coal1]
            return coal1
        elif kind == 'gas':
            gas1 = gas[year].values()
            gas1 = [float(i) for i in gas1]
            return gas1
        elif kind == 'water':
            water1 = water[year].values()
            water1 = [float(i) for i in water1]
            return water1

####################################################################################################

kind = input()
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('roqpor', '7o0kvfelsl')
trace1 = Scatter(
    x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y=add_dict('2551', kind),
    name='2551',
)
trace2 = Scatter(
    x=['Jan', 'feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y=add_dict('2552', kind),
    name='2552',
)
trace3 = Scatter(
    x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y=add_dict('2553', kind),
    name='2553',
)
data = Data([trace1, trace2, trace3])
plot_url = py.plot(data)
