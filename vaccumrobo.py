
""" 
name:surendra baskey
roll no:111601027
program description :python program for vaccum robot cleaner
assumptio:the plane is assumed to be of 2 dimension 
          :each point represent a coordinate in a 2 dimensional plane
     
 logic:robot is made to move in a spiral manner in the order of r-d-l-u
      :each point is compared with dirt point
      

"""
class environment:
    dx=0      #dx and dy is the dirt point
    dy=0
    totalstep=0
    def __init__(self, sx,sy):   #sx,sy are robot position
        self.sx =sx
        self.sy =sy

    def percept(self, steps, direction):
        if steps != 0:
            print self.sx,self.sy, "\t\t",self.totalstep, "\t", direction
        #movement in right direction
        if direction == "r":
            self.totalstep+=1
            self.sx=self.sx+1
            self.sy=self.sy
        #movement in left direction
        elif direction=="l":
            self.totalstep+=1
            self.sx=self.sx-1
            self.sy=self.sy
        #movement in up direction
        elif direction=="u":
            self.totalstep+=1
            self.sx=self.sx
            self.sy=self.sy + 1
        #movement in down direction
        else:
            self.totalstep+=1
            self.sx=self.sx
            self.sy=self.sy-1
         #dirt point and robot position are checked
        if  (self.sy==self.dy and self.sx==self.dx):
           print self.sx,self.sy, "\t\t",self.totalstep, "\t", direction
           return 1
        else:
           return 0
        
class agent:
    """Class that defines agent"""
    steps=0
    flag=0
    count=0
    """ for the movement in r-l-u-d direction 
        the movement is done 1 unit at a time.after each step position
        of robot is checked with dirt position
        if the dirt point reached then flag is set to 1 """
    def move_right(self):
        self.steps = self.steps + 1
        for i in range(self.steps):
                  percept = env.percept(self.steps, "r")
                  if percept:
                      print "dirt cleaned"
                      self.flag=1
                      break
        if self.flag==0:
            self.move_down()

    def move_up(self):
        self.count=self.count+1
        for i in range(self.count):
                  percept = env.percept(self.steps, "u")
                  if percept:
                      print "dirt cleaned"
                      self.flag=1
                      break
        if self.flag==0:
              self.move_right()

    def  move_left(self):

        self.steps = self.steps + 1
        for i in range(self.steps):
                  percept = env.percept(self.steps, "l")
                  if percept:
                      print "dirt cleaned"
                      self.flag=1
                      break
        if self.flag==0:
             self.move_up()

    def move_down(self):
        self.count=self.count+1
        for i in range(self.count):
                  percept = env.percept(self.steps, "d")
                  if percept:
                      print "dirt cleaned"
                      self.flag=1
                      break
        if self.flag==0:
             self.move_left()

print("Agent_loc(x,y)  Steps  Direction ")
steps = 0  # initialize steps

env=environment(1,1)  # initial robot position

percept =env.percept(steps, "r")  # robot recieves the percept from the environment

if percept:
    print "dirt cleaned"
    
else:  # if the dirt is not found at start point it starts movement
       #initialyu
    a=agent()
    a.move_right()







