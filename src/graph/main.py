import pandas as pd
import trmap as tr
import matplotlib.pyplot as plt

# read in csv
df = pd.read_csv('/Users/lukezanuck/Desktop/Projects/traveling-runner/python-roster-scraper/hometowns.csv')
df = df.drop(labels='Unnamed: 0', axis=1)
#df = df.drop_duplicates(subset="hometown")
df = df.drop(index=7)
print(df)

starting_loc = 'Los Angeles, Calif.'
current_loc = starting_loc
ending_loc = 'Williams College'
goal_mileage = 3500
G = tr.makeGraph(df)

# tsp
greedy_tsp = tr.nx.approximation.greedy_tsp
path = greedy_tsp(G, source=starting_loc)
path.pop(len(path)-1)
print(path)

# code to draw graph
# tr.nx.draw(full_graph)
# plt.show()