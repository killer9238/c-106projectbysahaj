import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getdatasource(data_path):
    ice_cream_sales=[]
    cold_drinks_sales=[]
    with open(data_path) as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drinks_sales.append(float(row["Ice-cream Sales( â‚¹ )"]))
    return{"x":ice_cream_sales,"y":cold_drinks_sales}

def findcorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Temperature v/s IceCream sales: ",correlation[0,1])

def setup():
    data_path="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data_source=getdatasource(data_path)
    findcorrelation(data_source)
setup()