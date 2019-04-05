#random movement of agent in 3d environment
"""
names:
Surendra Baskey-111601027
Sachin Hansdah-111601019
Rajendra Singh-111601017

Description:
 def determine_dir function gives random direction and percept function update the current position of
he running agent.run fun initiates the movement for agent.
"""


import numpy as np 
class agent3d:
    def __init__(self):
        self.dir=0
        self.loc=(0,0,0)
        self.reward=0


    def determine_dir(self):
        self.dir=np.random.randint(0,6)
        if self.dir==0:
            return 0
        elif self.dir==1:
            return 1
        elif self.dir==2:
            return 2
        elif self.dir==3:
            return 3
        elif self.dir==4:
            return 4
        else:
            return 5
        
    def move(self):

        if self.reward==1:
            return

        self.dir = self.determine_dir()
        per = env.percept(self.dir)
        #print "per",per

        if per==1:

            #print self.dir
            if self.dir==0:  
               self.loc=(self.loc[0] + 1,self.loc[1] +0,self.loc[2]+0)
            elif self.dir==1:
               self.loc=(self.loc[0] -1,self.loc[1] +0,self.loc[2]+0)
            elif self.dir==2:
               self.loc=(self.loc[0] + 0,self.loc[1] +1,self.loc[2]+0)
            elif self.dir==3:
                self.loc=(self.loc[0] + 0,self.loc[1] -1,self.loc[2]+0)
            elif self.dir==4:
                self.loc=(self.loc[0] + 0,self.loc[1]+0,self.loc[2]+1)
            else:
                self.loc=(self.loc[0] + 0,self.loc[1]+0,self.loc[2]-1)
            
       # print self.loc

        if per == 2:
                 self.reward=1

class Environment2d:
    def __init__(self, l):
        self.agent = agent3d()
        self.l = l
        m = (l + 1) // 2
        self.iloc = (m, m,m)

    def percept(self, dir):
       # print self.agent.loc
        if dir==0:
               cur_loc=(self.iloc[0] + self.agent.loc[0] + 1,self.iloc[1] + self.agent.loc[1] + 0,self.iloc[2]+self.agent.loc[2]  +0)
        elif dir==1:
               cur_loc=(self.iloc[0] + self.agent.loc[0] - 1,self.iloc[1] + self.agent.loc[1] +0,self.iloc[2]+self.agent.loc[2] + 0)
        elif dir==2:
               cur_loc=(self.iloc[0] + self.agent.loc[0] + 0,self.iloc[1] + self.agent.loc[1] +1,self.iloc[2]+self.agent.loc[2] + 0)
        elif dir==3:
             cur_loc=(self.iloc[0] + self.agent.loc[0] + 0,self.iloc[1] + self.agent.loc[1] -1,self.iloc[2]+self.agent.loc[2] + 0)
        elif dir==4:
             cur_loc=(self.iloc[0] + self.agent.loc[0] + 0,self.iloc[1] + self.agent.loc[1] +0,self.iloc[2]+self.agent.loc[2] + 1)
        else:
             cur_loc=(self.iloc[0] + self.agent.loc[0] + 0,self.iloc[1] + self.agent.loc[1] +0,self.iloc[2]+self.agent.loc[2] - 1)

        print "dir",dir
        print "cur_loc",cur_loc
        
        if cur_loc==(self.l,self.l,self.l):
                return 2
        if(cur_loc[0] < 0 or cur_loc[1]<0 or cur_loc[2]<0 or cur_loc[0] > self.l or cur_loc[1]>self.l or cur_loc[2]>self.l):
            return 0

        return 1
        

    

    def run(self):
        moves = 0
        while self.agent.reward==0:
            self.agent.move()
            moves += 1
        return moves

l = 4
env = Environment2d(l)
cm = env.run()
print "moves",(cm)
print env.agent.reward
