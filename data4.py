import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getdatasource(data_path):
    marks=[]
    days_present=[]
    with open(data_path) as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return{"x":marks,"y":days_present}

def findcorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Marks and Days present is: ",correlation[0,1])

def setup():
    data_path="Student Marks vs Days Present.csv"
    data_source=getdatasource(data_path)
    findcorrelation(data_source)
setup()