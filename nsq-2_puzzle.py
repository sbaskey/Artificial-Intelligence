"""
Quiz1-Nsquare minus 2 puzzle.
Name-Surendra Baskey
Roll no-111601027
 """

import numpy as np
import Queue as Queue
import copy
#seeting up environment
class environment:
    #goal matrix
    """gm=[[1 , 2, 3],
       [ 4 , 5, 6],
       [7,8,9]]"""
       
    #input matrix
    gm=[[1,1,0,-1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]
    
    m=[[1,1,1,1],
       [1,1,1,1],
       [1,1,0,1],
       [1,1,1,-1]]
   
    """m=[[1,2,3],
       [4,8,9],
        [7,5,6]]"""
    #initialising manhattan matrix
    def __init__(self,n):
       self.n=n
       self.man=np.zeros(self.n*self.n).reshape(self.n,self.n)

    def h(self,m):
	man=[]
	h=0
	for i in range(self.n):
		for j in range(self.n):
             #v=m[i][j]
			if(m[i][j]==-1):
				x=i
				y=j
				h=abs(0-i) + abs(3-j)
				return h
        
        #print self.man
        #return h  #returns the heuristic values
    #blank function returns the index for the blank blocks
    def blank(self,m):
        a=[]
        for i in range(self.n):
              for j in range(self.n):
                     if(m[i][j]==0):                     
                        a.append(i)
                        a.append(j)
        return a
    #move up funtion
    def move_up(self,matrix,i,j,k):
         if i==0:
             return matrix
         if i!=0:
            matrix[i][j]=matrix[i-1][j]
            matrix[i-1][j]=k
            #print matrix
            return matrix
    #move down function
    def move_down(self,matrix,i,j,k):
         if i==self.n-1:
              return matrix      
         if i!=self.n-1:
            matrix[i][j]=matrix[i+1][j]
            matrix[i+1][j]=k 
            return matrix  
    #move left function
    def move_left(self,matrix,i,j,k):
         if j==0:
             return matrix
         if j!=0:
            matrix[i][j]=matrix[i][j-1]
            matrix[i][j-1]=k
            return matrix
    #move right function
    def move_right(self,matrix,i,j,k):
         if j==self.n-1:
               return matrix
         if j!=self.n-1:
            matrix[i][j]=matrix[i][j+1]
            matrix[i][j+1]=k
            return matrix
    #printing a matrix
    def print_m(self,m,h,d):
          print "h=",h
          print "d",d
          for i in range(self.n):
                 print m[i]
                 
          
    #heuristic search function
    #this function put the initial matrix into the priority que
    """in the search process it extract an matrix with least heuristic value
       does 8 possible movement for 2 blocks and checks if any configuration gives 
       heuristic value 0.the currently visited states are put in to visit dictionary and put
       back into the queue with their heuristic value untill we get the state with h=0"""
    def heur_search(self,m,a):
      q=Queue.PriorityQueue()
      h=env.h(m)
      k=0
      q.put((h , 0,0,m,"start"))
      k-=1
      visit={}
      count=0
      cnt=0
      
      while not q.empty():
         #print(cnt)
        # print("resulted states in this steps")
         cnt+=1          
         c= q.get()
         m1=c[3]
         h=c[0]
         mat2str = str(m1)
         visit[mat2str]=count
         count+=1
         a=env.blank(copy.deepcopy(m1))
         k1=m1[a[0]][a[1]]
         #k2=m1[a[2]][a[3]]
         env.print_m(m1,h,c[4])
        # print(c[3])
        
         c1=env.move_right(copy.deepcopy(m1),a[0],a[1],0)
         mat2str =str(c1)
         if (mat2str not in visit):
                 visit[mat2str]=count
                 count+=1
                 h1=env.h(c1)
                 #env.print_m(c1,h1)
                 if (h1==0):
                    #print "steps=",cnt
                    return c1
            
                 q.put((h1,k,-count+k,c1,"right1"))
                 k-=1

         c2=env.move_down(copy.deepcopy(m1),a[0],a[1],0)
         mat2str =str(c2)
         if (mat2str not in visit):
                 visit[mat2str]=count
                 count+=1
                 h2=env.h(c2)
                 q.put((h2,k,-count+k,c2,"down1"))
                 k -= 1
                 
                 #env.print_m(c2,h2)
                 if (h2==0):
                 #print "steps=",cnt
                    return c2 
         
            
         
         c3=env.move_left(copy.deepcopy(m1),a[0],a[1],0)
         mat2str =str(c3)
         if (mat2str not in visit):
                 visit[mat2str]=count
                 count+=1
                 h3=env.h(c3)
                 q.put((h3,k,-count+k,c3,"left1"))
                 k-=1
                 
                 #env.print_m(c3,h3)
                 if (h3==0):
                 #print "steps=",cnt
                    return c3
         
            
         
         c4=env.move_up(copy.deepcopy(m1),a[0],a[1],0)
         
         mat2str =str(c4)
         if (mat2str not in visit):        
                 visit[mat2str]=count
                 count+=1
                 h4=env.h(c4)
                 q.put((h4,k,-count+k,c4,"up1"))
                 k-=1
         
                 
                 #env.print_m(c4,h4)
                 if (h4==0):
                 #print "steps=",cnt
                     return c4 
         
            


         #print("visited",visit)
               
        
         
        
        

env=environment(4)
m1=env.m
a=env.blank(copy.deepcopy(m1))
s=env.heur_search(copy.deepcopy(m1),a)
print s


	


