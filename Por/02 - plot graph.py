#test print graph
import plotly.plotly as py
import plotly.graph_objs as go
x2551 = go.Scatter(
        x=['2008-01', '2008-02', '2008-03', '2008-04', '2008-05', '2008-06', '2008-07', '2008-08', '2008-09', '2008-10', '2008-11', '2008-12'],#month
        y=[1062.24, 1063.77, 1062.57, 1063.57, 1064.87, 1061.37, 1063.98, 1065.19, 1063.46, 1061.09, 1063.01, 1063.21]#fix value from csv
        name='2551'#name of line
    )
x2552 =  go.Scatter(
        x=['2008-01', '2008-02', '2008-03', '2008-04', '2008-05', '2008-06', '2008-07', '2008-08', '2008-09', '2008-10', '2008-11', '2008-12'],
        y=[1062.74, 1062.71, 1062.54, 1063.76, 1064.22, 1061.7, 1062.11, 1063.01, 1062.48, 1062.25, 1062.53, 1064.58]#fix value from csv
        name='2552'
    )
x2553 =  go.Scatter(
        x=['2008-01', '2008-02', '2008-03', '2008-04', '2008-05', '2008-06', '2008-07', '2008-08', '2008-09', '2008-10', '2008-11', '2008-12'],
        y=[1064.57, 1063.39, 1063.89, 1064.04, 1064.48, 1065.36, 1065.71, 1064.54, 1065.96, 1063.47, 1063.21, 1065.23]#fix value from csv
        name='2553'
    )     
data = [x2551, x2552, x2553]
plot_url = py.plot(data, filename='date-axes')
