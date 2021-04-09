import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

data = pd.read_csv("./studentMarks.csv")

df = data["Math_score"].tolist()



def exp():
    dataset = []
    for i in range(0,100):
        index = random.randint(0, len(df)-1)
        num = df[index]
        dataset.append(num)

    mean1 = statistics.mean(dataset)
    return mean1

meanlist = []

for i in range(0,1000):
    mean2 = exp()
    meanlist.append(mean2)

mean = statistics.mean(meanlist)

stdev = statistics.stdev(meanlist)
print(mean,stdev)
#1st dev
dev1start = mean - stdev
dev1end = mean + stdev 
#2nd dev
dev2start = mean - 2*stdev
dev2end = mean + 2*stdev 
#3rd dev
dev3start = mean - 3*stdev
dev3end = mean + 3*stdev 


figure = ff.create_distplot([meanlist],['Math_score'], show_hist=False)
figure.add_trace(go.Scatter(x = [mean,mean], y = [0,0.15], mode = "lines", name = "mean"))
figure.add_trace(go.Scatter(x = [dev1start,dev1start], y = [0,0.15], mode = "lines", name = "dev1start"))
figure.add_trace(go.Scatter(x = [dev2start,dev2start], y = [0,0.15], mode = "lines", name = "dev2start"))
figure.add_trace(go.Scatter(x = [dev3start,dev3start], y = [0,0.15], mode = "lines", name = "dev3start"))
figure.add_trace(go.Scatter(x = [dev1end,dev1end], y = [0,0.15], mode = "lines", name = "dev1start"))
figure.add_trace(go.Scatter(x = [dev2end,dev2end], y = [0,0.15], mode = "lines", name = "dev2start"))
figure.add_trace(go.Scatter(x = [dev3end,dev3end], y = [0,0.15], mode = "lines", name = "dev3start"))
figure.show()

dt1 = pd.read_csv("./data1.csv")
df1 = data["Math_score"].tolist()
mean1 = statistics.mean(df1) 


dt2 = pd.read_csv("./data1.csv")
df2 = data["Math_score"].tolist()
mean2 = statistics.mean(df2) 
figure = ff.create_distplot([meanlist],['Math_score'], show_hist=False)
figure.add_trace(go.Scatter(x = [mean,mean], y = [0,0.15], mode = "lines", name = "mean"))
figure.add_trace(go.Scatter(x = [mean2,mean2], y = [0,0.15], mode = "lines", name = "mean1"))
figure.add_trace(go.Scatter(x = [dev1end,dev1end], y = [0,0.15], mode = "lines", name = "dev1start"))
figure.show()



dt3 = pd.read_csv("./data1.csv")
df3 = data["Math_score"].tolist()
mean3 = statistics.mean(df3) 
