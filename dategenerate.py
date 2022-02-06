import datetime as dt
import pandas as pd
import numpy as np

dates = [] #will load dates in it 

for i in range(200):
    start = dt.datetime.today()+dt.timedelta(i)
    day = start.strftime("%A")
    if (day == "Monday" or day == "Thursday"):
        dates.append(start.date().strftime("%d-%m-%Y"))

s = pd.Series(np.array(dates))
s.to_excel("Dates.xlsx")