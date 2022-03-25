import pandas as pd
import plotly.graph_objects as go
import csv

a = pd.read_csv("data.csv")
b = a.loc[a["student_id"] == "TRL_xsl"]

fig = go.Figure(go.Scatter(
    y = b.groupby("level")["attempt"].mean(),
    x = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = "v"
))

fig .show()