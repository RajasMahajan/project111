import plotly.graph_objects as go
import plotly.figure_factory as ff
import csv 
import pandas as pd
import random
import statistics

data = pd.read_csv('medium_data.csv')
dataone = data['reading_time'].tolist()

population_mean = statistics.mean(dataone)

def findmean(times):
    datais =[]
    for i in range(0,times):
        randomone = random.randint(0,len(data)-1)
        value = dataone[randomone]
        datais.appendvalue(value)
        meanone = statistics.mean(dataone)
        return meanone

def plot_graph(mean_list):
    data1 = mean_list
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([data1],['reading_time'], show_hist = False)
    fig.addtrace(go.Scatter(x =[mean,mean], y=[0,1], mode='lines', name='mean'))
    fig.show()

def setup():
    mean_list = []
    for i in range (0,100):
        randommean = findmean(30)
        mean_list.append(randommean)
        plot_graph(mean_list)

setup()
