import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


class Simulator():
    def __init__(self, simulator_options, axis='off') -> None:
        self.options = simulator_options
        # Object to be simulated
        self.object = None
        self.axis = axis
        self.setupSimulator()
        
    def startAnimation(self):
        L = 500
        self.ax = plt.axes(xlim=(-L-50,L+50),ylim=(-L-50,L+50))
        """Initial drawing of the scatter plot."""
        self.scat = self.ax.scatter(x=0, y=0, alpha=0.876, marker='o')
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.ax.axis(self.axis)
        return self.scat,

    def simulate(self, world):
        self.object = world

    def runAnimation(self, i):
        world_state = self.object.step(self.dt)

        self.scat.set_offsets(world_state[0])
        self.scat.set_array(world_state[1])
        self.scat.set_sizes(world_state[2])
        return self.scat,

    def setupSimulator(self):
        # Simulator parameters unpacking
        self.final_time = self.options['final_time']
        self.accuracy = 2**self.options['accuracy']
        self.dt = self.final_time/self.accuracy

        # Matplotlib animation setup
        self.fig, self.ax = plt.subplots()
        self.ax.axis(self.axis)
        # Then setup FuncAnimation.
        self.ani = animation.FuncAnimation(self.fig, self.runAnimation, interval=1, 
                                        init_func=self.startAnimation, blit=True)

        

