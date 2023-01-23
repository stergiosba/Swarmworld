import numpy as np
from sklearn.cluster import DBSCAN
from agent import Agent
import numpy.linalg as la
import time

class World():
    def __init__(self, name) -> None:
        self.name = name
        self.clock = None
        self.clustering = None
        self.Agents = []

    def __repr__(self) -> str:
        result = f"{self.name}:\n{{\n"
        for agent in self.Agents:
            result+="\t"+str(agent)
            result+="\t"+35*"-"+"\n"
        return result+"}"


    def populate(self, N_agents):
        for i in range(N_agents):
            agent = Agent(i, 0, 3, np.random.normal(0,1,2)*50, np.random.normal(0,0.75,2),np.zeros(2))
            self.Agents.append(agent)
                
        all_positions = [agent.state[0,:] for agent in self.Agents]
        self.clustering = DBSCAN(eps=25, min_samples=2).fit(all_positions)
        self.assignColors()
        for id, agent in enumerate(self.Agents):
            agent.color = self.cluster_color[self.clustering.labels_[id]]
        
        
        #self.Agents[0].makeLeader()

    def assignColors(self):
        self.cluster_color = dict()
        labels = set(self.clustering.labels_)
        for i,label in enumerate(labels):
            self.cluster_color[label] = i

    def step(self, dt):
        all_size = []
        all_colors = []
        all_positions= []
        for id, agent in enumerate(self.Agents):
            agent.updatePosition(dt, self.clustering)
            all_positions.append(agent.state[0,:])
            all_size.append(agent.marker_size)

        self.clustering = DBSCAN(eps=25, min_samples=2).fit(all_positions)
        self.assignColors()
        
        for id, agent in enumerate(self.Agents):
            agent.color = self.cluster_color[self.clustering.labels_[id]]
            all_colors.append(agent.color)

        return (all_positions, all_colors, all_size)
        
        
        
        
