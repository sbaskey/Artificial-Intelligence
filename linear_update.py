
import random
import matplotlib.pyplot as plt
import numpy as np
import math


t=[]
tsq=[]
mtsq=[]
for i in range(1,1001):
    t.append(1/i)
    tsq.append(1/(i*i))
    mtsq.append(-1/(i*i))
    
plt.plot(range(1000),t,c='r',label="1/t")
plt.plot(range(1000),tsq,c='k',label="1/t*t")
plt.plot(range(1000),mtsq,c='c',label="-1/t*t")
plt.legend(loc='upper right')
plt.show()



#1st set, step 1
noise=[]
theta=[]
for i in range(1000):
    n=random.choice([-1,1])
    noise.append(n)
    n1=0
    for j in range(i+1):
        n1+=noise[j]
    n1=n1/(i+1)
    theta.append(n1)


#1st set, step 2
theta2=[]
t2=noise[0]
theta2.append(t2)
k=100
for i in range(1,1000):
    alpha1=1/(i+1+k)
    t2=theta2[i-1] + alpha1*(noise[i] - theta2[i-1])    
    theta2.append(t2)
    
plt.plot(range(1000),theta,c='r',label="Averaging")
plt.plot(range(1000),theta2,c='k',label="Averaging using recursion with alpha=1/t+k")
plt.legend(loc='upper right')
plt.show()


#1st set, step 3
theta3=[]
t3=noise[0]
theta3.append(t3)
for i in range(1,1000):
    alpha2=2
    t3=theta3[i-1] + alpha2*(noise[i] - theta3[i-1])
    theta3.append(t3)  
    
plt.plot(range(1000),theta3,c='c')
plt.title('Recursion with constant step-size')
plt.show()


#1st set, step 4.2
theta_star=2
theta4=[]
t2=noise[0] + theta_star
theta4.append(t2)
k=100
for i in range(1,1000):
    alpha1=1/(i+1+k)
    t2=theta4[i-1] + alpha1*(theta_star + noise[i] - theta4[i-1])    
    theta4.append(t2)
    
plt.plot(range(1000),theta4,c='k')
plt.title('Averaging and Recursion with input plus noise')
plt.show()


#1st set, step 4.3
theta_star=2
theta5=[]
t3=noise[0] + theta_star
theta5.append(t3)
for i in range(1,1000):
    alpha2=2
    t3=theta5[i-1] + alpha2*(theta_star + noise[i] - theta5[i-1])
    theta5.append(t3)

plt.plot(range(1000),theta5,c='c')
plt.title('Averaging and Recursion(with constant step-size) with input plus noise')
plt.show()   



#2nd set
size=(1000,2)
noise2d=np.zeros(size)
for i in range(1000):
    noise2d[i][0]=random.choice([-1,1])
    noise2d[i][1]=random.choice([-1,1])    



#2nd set, step 1 & 2
theta2d2=np.zeros(size)
theta2d=np.zeros(size)
t20=noise2d[0][0]
t21=noise2d[0][1]
k=100
for i in range(1,1000):
    alpha2d1=1/(i+1+k)
    theta2d2[i]=theta2d2[i-1] + alpha2d1*(noise2d[i] - theta2d2[i-1])
    n1=0
    n2=0
    for j in range(i+1):
        n1+=noise2d[j][0]
        n2+=noise2d[j][1]
    n1=n1/(i+1)
    n2=n2/(i+1)
    theta2d[i][0]=n1
    theta2d[i][1]=n2

plt.plot(range(1000),theta2d,c='r',label="Averaging")
plt.plot(range(1000),theta2d2,c='k',label="Averaging using recursion with alpha=1/t+k")
plt.legend(loc='upper right')
plt.title('Two Dimensional')
plt.show()




#2nd set, step 3
theta2d3=np.zeros(size)
t30=noise2d[0][0]
t31=noise2d[0][1]
for i in range(1,1000):
    alpha2d2=2
    theta2d3[i]=theta2d3[i-1] + alpha2d1*(noise2d[i] - theta2d3[i-1])
    
plt.plot(range(1000),theta3,c='c')
plt.title('Recursion with constant step-size in 2D')
plt.show()



#2nd set, step 4.2
theta_star2d=[2,3]
theta2d4=np.zeros(size)
theta2d4[0][0]=noise2d[0][0] + theta_star2d[0]
theta2d4[0][1]=noise2d[0][1] + theta_star2d[1]
k=100
for i in range(1,1000):
    alpha2d1=1/(i+1+k)    
    theta2d4[i]=theta2d4[i-1] + alpha2d1*(theta_star2d[0] + noise2d[i] - theta2d4[i-1])
    
plt.plot(range(1000),theta2d4,c='k')
plt.title('Averaging and Recursion with input plus noise in 2D')
plt.show()




#2nd set, step 4.3
theta_star2d=[2,3]
theta2d5=np.zeros(size)
theta2d5[0][0]=noise2d[0][0] + theta_star2d[0]
theta2d5[0][1]=noise2d[0][1] + theta_star2d[1]
alpha2d2=2
for i in range(1,1000):
    theta2d5[i]=theta2d5[i-1] + alpha2d2*(theta_star2d[0] + noise2d[i] - theta2d5[i-1])
    
plt.plot(range(1000),theta5,c='c')
plt.title('Averaging and Recursion(with constant step-size) with input plus noise in 2D')
plt.show()




#3rd set, step 1
b=[2,3]
alpha=0.1
theta=np.zeros(size)
theta_norm=np.zeros(size)
theta_norm[0]=theta_star-theta[0]
theta_norm[0]=np.linalg.norm(theta_norm[0])
for i in range(1,1000):
    theta[i]=theta[i-1] + alpha*(b - theta[i-1])
    theta_norm[i]=theta_star-theta[i]
    theta_norm[i]=np.linalg.norm(theta_norm[i])
    
plt.plot(range(1000),theta_norm,c='r')
plt.show()




#3rd set, step 2.1
A=[[1,0],
   [0,1]]
theta2=np.zeros(size)
theta2_norm=np.zeros(size)
theta2_norm[0]=theta_star-theta2[0]
theta2_norm[0]=np.linalg.norm(theta2_norm[0])
for i in range(1,1000):
    theta2[i]=theta2[i-1] + alpha*(b - np.matmul(A,theta2[i-1]))
    theta2_norm[i]=theta_star-theta2[i]
    theta2_norm[i]=np.linalg.norm(theta2_norm[i])
    
plt.plot(range(1000),theta2_norm,c='r')
plt.show()




#3rd set, step 2.2
Alist=[[[2,0],[0,1]],[[1,0],[0,2]],[[1,0.1],[-0.1,1]],[[1,1],[-1,1]],[[1,10],[-10,1]],[[1,10],[10,1]],[[1,0.1],[0.1,1]]]
for i in range(7):
    A=Alist[i]
    theta2=np.zeros(size)
    theta2_norm=np.zeros(size)
    theta2_norm[0]=theta_star-theta2[0]
    theta2_norm[0]=np.linalg.norm(theta2_norm[0])
    for j in range(1,1000):
        theta2[j]=theta2[j-1] + alpha*(b - np.matmul(A,theta2[j-1]))
        theta2_norm[j]=theta_star-theta2[j]
        theta2_norm[j]=np.linalg.norm(theta2_norm[j])
    
    plt.plot(range(1000),theta2_norm,c='r')
    print("A = ",end='')
    print(A)
    plt.show()




#3rd set, step 2.3
blist=[[1,1],[1,-1],[10,1]]
for k in range(3):
    b=blist[k]
    Alist=[[[2,0],[0,1]],[[1,0],[0,2]],[[1,0.1],[-0.1,1]],[[1,1],[-1,1]],[[1,10],[-10,1]],[[1,10],[10,1]],[[1,0.1],[0.1,1]]]
    for i in range(7):
        A=Alist[i]
        theta2=np.zeros(size)
        theta2_norm=np.zeros(size)
        theta2_norm[0]=theta_star-theta2[0]
        theta2_norm[0]=np.linalg.norm(theta2_norm[0])
        for j in range(1,1000):
            theta2[j]=theta2[j-1] + alpha*(b - np.matmul(A,theta2[j-1]))
            theta2_norm[j]=theta_star-theta2[j]
            theta2_norm[j]=np.linalg.norm(theta2_norm[j])
    
        plt.plot(range(1000),theta2_norm,c='r')
        print("b = ",end='')
        print(b,end='')
        print("\t",end='')
        print("A = ",end='')
        print(A)
        plt.show()



#3rd set, step 3
blist=[[1,1],[1,-1],[10,1]]
for k in range(3):
    b=blist[k]
    Alist=[[[2,0],[0,1]],[[1,0],[0,2]],[[1,0.1],[-0.1,1]],[[1,1],[-1,1]],[[1,10],[-10,1]],[[1,10],[10,1]],[[1,0.1],[0.1,1]]]
    for i in range(7):
        A=Alist[i]
        theta2=np.zeros(size)
        theta2_norm=np.zeros(size)
        theta2_norm[0]=theta_star-theta2[0]
        theta2_norm[0]=np.linalg.norm(theta2_norm[0])
        for j in range(1,1000):
            theta2[j]=theta2[j-1] + alpha*(b - np.matmul(A,theta2[j-1]) + noise[j])
            theta2_norm[j]=theta_star-theta2[j]
            theta2_norm[j]=np.linalg.norm(theta2_norm[j])
    
        plt.plot(range(1000),theta2_norm,c='r')
        print("b = ",end='')
        print(b,end='')
        print("\t",end='')
        print("A = ",end='')
        print(A)
        plt.show()



#3rd set, step 4
c=[10,100,1000]
for k in range(3):
    Alist=[[[2,0],[0,1]],[[1,0],[0,2]],[[1,0.1],[-0.1,1]],[[1,1],[-1,1]],[[1,10],[-10,1]],[[1,10],[10,1]],[[1,0.1],[0.1,1]]]
    for i in range(7):
        A=Alist[i]
        theta2=np.zeros(size)
        theta2_norm=np.zeros(size)
        theta2_norm[0]=theta_star-theta2[0]
        theta2_norm[0]=np.linalg.norm(theta2_norm[0])
        for j in range(1,1000):
            alpha=0.1/(c[k]+j+1)
            theta2[j]=theta2[j-1] + alpha*(b - np.matmul(A,theta2[j-1]) + noise2d[0])
            theta2_norm[j]=theta_star-theta2[j]
            theta2_norm[j]=np.linalg.norm(theta2_norm[j])
    
        plt.plot(range(1000),theta2_norm,c='r',label="alpha=0.1/(c+t)")
        print("c = ",end='')
        print(c[k],end='')
        print("\t",end='')
        print("A = ",end='')
        print(A)
        plt.legend(loc='upper right')
        plt.show()







