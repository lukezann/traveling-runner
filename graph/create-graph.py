import pandas as pd
import numpy as np
import networkx as nx
import haversine as hs   
from haversine import Unit

# read csv
df = pd.read_csv('/Users/lukezanuck/Desktop/Projects/traveling-runner/python-roster-scraper/hometowns.csv')
df = df.drop(labels='Unnamed: 0', axis=1)

# create empty adjacency matrix
adj_matrix = np.ndarray(shape=(len(df), len(df)))

# fill adjacency matrix with distance in miles
# used as weights for graph
for i, row in enumerate(adj_matrix):
    for j, col in enumerate(row):
        # city1_name = df.iloc[i]['hometown']
        # city2_name = df.iloc[j]['hometown']

        city1_coords = (df.iloc[i]['latitude'], df.iloc[i]['longitude'])
        city2_coords = (df.iloc[j]['latitude'], df.iloc[j]['longitude'])

        distance = round(hs.haversine(city1_coords, city2_coords, unit=Unit.MILES), 2)
        adj_matrix[i][j] = distance

# TODO: create graph from adjacency matrix and add labels