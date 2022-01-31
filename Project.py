import csv
import numpy as np
import plotly.express as px

def get_data_source(data_path):
    days = []
    marks = []

    with open(data_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            days.append(int(float(row["Days Present"])))
            marks.append(int(float(row["Marks"])))

    return {
        "x": days,
        "y": marks
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(f"Correlation is {correlation[0, 1]}")

def plot_figure(data_source):
    fig = px.scatter(x = data_source["x"], y = data_source["y"])
    fig.show()

def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plot_figure(data_source)

setup()
