import pandas as pd
import numpy as np
import networkx as nx
import haversine as hs   
from haversine import Unit

class TRMap:

    def __init__(self, graph: nx.Graph(), 
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

def makeGraph(data: pd.DataFrame) -> nx.Graph():
        # create empty graph
        G = nx.Graph()

        # iterate through every possible combination
        for i in range(0, len(data)):
            city = data.iloc[i]['hometown']
            city_coords = (data.iloc[i]['latitude'], data.iloc[i]['longitude'])

            G.add_node(city)

            for j in range(0, len(data)):

                if i is not j:
                    dest = data.iloc[j]['hometown']
                    dest_coords = (data.iloc[j]['latitude'], data.iloc[j]['longitude'])
                    distance = round(hs.haversine(city_coords, dest_coords, unit=Unit.MILES), 2)
                    G.add_edge(city, dest, weight=distance)
                
        return G
    
#TODO: helper function to find distance between two locations
def dist(data, city1: str, city2: str):
    pass   