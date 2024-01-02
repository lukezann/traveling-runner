import pandas as pd
import numpy as np
import networkx as nx
import haversine as hs   
from haversine import Unit

class TRMap:

    def __init__(self, graph: nx.Graph, 
                current_mileage: int, 
                goal_mileage: int, 
                starting_loc: str,
                current_loc: str,
                ending_loc: str):
        
        self.graph = graph
        self.current_mileage = current_mileage
        self.goal_mileage = goal_mileage
        self.starting_loc = starting_loc
        self.current_loc = current_loc
        self.ending_loc = ending_loc
    
    def updateCurrentMileage(self, miles: int):
        self.current_mileage += miles

    def updateGoalMileage(self, new_goal_mileage: int):
        self.goal_mileage = new_goal_mileage

def makeGraph(data: pd.DataFrame) -> nx.Graph:
        # create empty graph
        graph = nx.Graph

        # iterate through every possible combination
        for i in range(0, len(data)+1):
            for j in range(0, len(data)+1):

                # do not need to make a self-loop
                if i == j: break

                city1_name = data.iloc[i]['hometown']
                city2_name = data.iloc[j]['hometown']

                city1_coords = (data.iloc[i]['latitude'], data.iloc[i]['longitude'])
                city2_coords = (data.iloc[j]['latitude'], data.iloc[j]['longitude'])

                distance = round(hs.haversine(city1_coords, city2_coords, unit=Unit.MILES), 2)
                
                graph.add_edge(city1_name, city2_name, weight=distance)

        return graph
    
# find path closest to mileage goal with most amount of stops
def findBestPath(graph: nx.Graph, start: str, end: str):
    pass