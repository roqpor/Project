import csv
from IPyhon.core.display import HTML
from nvd3 import multiBarChart
chart = multiBarChart(width = 1024, heiht = 600, x_axis_format = None)
data = []
with open('csv.csv', newline = '', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
xdata = []
ydata = []
i = 0
while i < len(data):
    xdata.append(data[i][0])
    ydata.append(int(data[i][5]))
    i += 1
chart.add_series(name = 'ENERGY', y = ydata, x = xdata)
chart.buildhtml()
HTML(chart.htmlcontent)
