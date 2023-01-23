import numpy as np
import matplotlib.pyplot as plt
from yaml import load, dump, Loader, dumper
from simulator import Simulator
from world import World 
from agent import Agent

stream = open("config.yaml", 'r')
config = load(stream, Loader=Loader)

simulator_options = config['simulator']

sim = Simulator(simulator_options)

Swarmworld = World("Swarmworld")
N=5000
Swarmworld.populate(N)
Swarmworld.step(0.01)

sim.simulate(Swarmworld)
x= plt.show()
