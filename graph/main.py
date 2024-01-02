import pandas as pd
from trmap import TRMap, makeGraph, findBestPath

# read in csv
df = pd.read_csv('/Users/lukezanuck/Desktop/Projects/traveling-runner/python-roster-scraper/hometowns.csv')
df = df.drop(labels='Unnamed: 0', axis=1)

starting_loc = 'Los Angeles, Calif.'
current_loc = starting_loc
ending_loc = 'Williams College'
goal_mileage = 3500
full_graph = makeGraph(df)
shortest_path = findBestPath(full_graph, starting_loc, ending_loc)
print(shortest_path)