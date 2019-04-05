""" 
name:surendra baskey
roll no:111601027
program description :python program to reach to shore in 1 dimensional world
assumptio:shore in 1d is defined as a point
         :sea and shore are assumed to be the 2 staes of the environment
     
logic:bunny is made to move to and fro from its initial position and increasing its position unit distance at a step untill it 
     reches the shore
     
"""
class shore:  #class shore is defined
    loc=20
    def __init__(self,agent_loc):
        self.agent_loc=agent_loc

    def percept(self,steps,direction):
        if steps!=0:
            print self.agent_loc, "\t\t", steps, "\t", direction
        if direction=="r":
            self.agent_loc=self.agent_loc+steps
        else:
            self.agent_loc=self.agent_loc-steps

        if self.loc==self.agent_loc:
                          print self.agent_loc, "\t\t", steps, "\t", direction
                          return 1
        else:
            return 0
#class agent is defined
class agent:
    steps=0
    #function for left movement
    def mov_left(self):
        self.steps=self.steps+1

        percep=s.percept(self.steps,"l")
        if percep:
            print 'shore reached'
        else:
            self.mov_right()
     #function for right movement
    def mov_right(self):
        self.steps=self.steps+1
        percept=s.percept(self.steps,"r")
        if percept:
            print 'shore reached'
        else:
            self.mov_left()

print 'agent location steps direction'
agent_loc=0
steps=0
s=shore(agent_loc)#initial location of agent is given
percep=s.percept(steps,'l')
if percep:
    print 'shaore reached'
else:
    a=agent()
    a.mov_left()



