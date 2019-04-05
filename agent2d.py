""" 
name:surendra baskey
roll no:111601027
program description :python program to two reach agent(bunny) to shore in 2 dimensional world
assumptio:shore is defined as straight line 
      :if bunny reaches any of the points on the line ,then bunny is on the shore
      :sea and shore are assumed to be the 2 staes of the environment
logic:bunny is made to move to and fro from its initial position and increasing its position unit distance at a step
     at the same time bunny is made to change direction 
     the sequence of movement bunny followed is r-l-u-d
      

"""

#class environment is defined 
class environment:
    shore_loc=20    #shore line is defined
    count=0
    totalsteps=0
   

    def __init__(self, agentloc_x,agentloc_y): #x and y are the position coordinate in 2d
        self.agentloc_x = agentloc_x
        self.agentloc_y=agentloc_y

     #percept function returns if the bunny reach the shore
    def percept(self, steps, direction):
        if steps != 0:
            print self.agentloc_x,"\t",self.agentloc_y,"\t",self.totalsteps, "\t", direction
        if direction == "r":
            self.totalsteps+=1
            self.agentloc_x=self.agentloc_x+steps
            self.agentloc_y=self.agentloc_y
        elif direction=="d":
            self.totalsteps+=1
            self.agentloc_x=self.agentloc_x
            self.count+=1
            self.agentloc_y=self.agentloc_y-self.count

        elif direction=="u":
            self.totalsteps+=1
            self.agentloc_x=self.agentloc_x
            self.count+=1
            self.agentloc_y=self.agentloc_y+self.count
        else:
            self.totalsteps+=1
            self.agentloc_x=self.agentloc_x-steps
            self.agentloc_y=self.agentloc_y
            
        
        if self.agentloc_x==self.shore_loc:
            print self.agentloc_x,"\t\t",self.agentloc_y,"\t",self.totalsteps, "\t", direction 
            return 1
        else:
            return 0


class agent:
    """Class that defines agent"""
    steps = 0
     #funtion for move right
    def move_right(self):
        self.steps = self.steps + 1
        percept = env.percept(self.steps, "r")
        if percept:
            print "shore reached"
        else:
            self.move_left()

     #funtion for move up
    def move_up(self):
        self.steps = self.steps 
        percept = env.percept(self.steps, "u")
        if percept:
            print "shore reached"
        else:
            self.move_down()
    #funtion for move left
    def  move_left(self):


        self.steps = self.steps +1
        percept = env.percept(self.steps, "l")
        if percept:
            print "shore reached"
        else:
            self.move_up()
    #funtion for move down
    def move_down(self):
          self.steps = self.steps 
          percept = env.percept(self.steps, "d")
          if percept:
              print "shore reached"
          else:
              self.move_right()

print("Agent Location   Steps  Direction ")

steps = 0  # initialize steps

env=environment(18,0)  # object of class environment is created and initial position of agent is given

percept =env.percept(steps, "r")  # agent recieves percept from shore

if percept:
    print("Shore reached")
else:  # if shore not reached agent moves right

    a = agent() #object for class agent is created
    a.move_right()






