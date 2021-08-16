import plotly.express as px
import pandas as pd
import csv

with open("Student Marks vs Days Present.csv")as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()