import numpy as np
import numpy.linalg as la

class Agent():
    def __init__(self, id, leader, radius, pos, vel, acc) -> None:
        self.id = id
        self.state = np.array([pos, vel, acc])
        self.radius = radius
        self.leader = leader
        self.color = None
        self.marker_size = 50
        
    def __str__(self) -> str:
        return f"Agent ID: [0,{self.id}]: \n\tPosition: [{self.state[0,0]:.1f}, {self.state[0,0]:.1f}] \n\tVelocity: [{self.state[1,0]:.1f}, {self.state[1,1]:.1f}] \n\tAcceleration: [{self.state[2,0]:.1f}, {self.state[2,1]:.1f}]\n"

    def __repr__(self) -> str:
        return f"Agent ID: [0,{self.id}]: \n\tPosition: [{self.state[0,0]:.1f}, {self.state[0,0]:.1f}] \n\tVelocity: [{self.state[1,0]:.1f}, {self.state[1,1]:.1f}]\n\tAcceleration: [{self.state[2,0]:.1f}, {self.state[2,1]:.1f}]\n"

    def makeLeader(self):
        self.leader = 1
        self.radius = 5
        self.marker_size = 200

    def updatePosition(self, dt, clustering):
        eps = 10**(-5)
        v_max = 20
        if abs(self.state[0,0])-500>=eps:
            self.state[0,0] = np.sign(self.state[0,0])*500
            self.state[1,0] *= -1
            self.state[1,1] *= 1
        if abs(self.state[0,1])-500>=eps:
            self.state[0,1] = np.sign(self.state[0,1])*500
            self.state[1,0] *= 1
            self.state[1,1] *= -1
        self.state[0,:]+=v_max*(self.state[1,:]/la.norm(self.state[1,:]))*dt
        

