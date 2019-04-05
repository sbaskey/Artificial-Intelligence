
#random movement of agent in 1d environment
"""
Names:
Surendra Baskey-111601027
Sachin Hansdah-111601019
Rajendra Singh-111601017

Description:
 def determine_dir function gives random direction and percept function update the current position of
he running agent.run fun initiates the movement for agent.
"""
import numpy as np 
class agent1d:
    def __init__(self):
        self.dir=0
        self.loc=0
        self.reward=0


    def determine_dir(self):
        self.dir=np.random.randint(0,2)
        if self.dir==0:
            return 1
        else:
            return -1

    def move(self):
        if self.reward==1:
            return

        self.dir = self.determine_dir()
        print "dir",self.dir
        percep= env.percept(self.dir)

        if percep:
            self.loc = self.loc + self.dir

        if percep == 2:
            self.reward=1

class Environment1d:
    def __init__(self, l):
        self.agent = agent1d()
        self.l = l
        m = (l + 1) // 2
        self.iloc = m
        
    def percept(self, dir):
        cur_loc=self.iloc + self.agent.loc + dir
        print cur_loc
        if(cur_loc == self.l):
            return 2
        if(cur_loc < 0 or cur_loc > self.l):
            return 0

        return 1

    

    def run(self):
        moves = 0
        while self.agent.reward==0:
            self.agent.move()
            moves += 1
            
        return moves



l = 10
env = Environment1d(l)
cm = env.run()
print "moves",(cm)
    
