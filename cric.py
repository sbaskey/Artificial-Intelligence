import numpy as np
import math
#import matplotlib.pyplot as plt


#given the batsmen and the action it is to give two probabilities
#first is the probability of getting out
#second gives the probability of scoring the run
def get_probabilies (action , x):
    
    if (x < 1 or x > 10 ):
        return (-1 , -1)
    pw_min = [0.01, 0.02, 0.03, 0.1, 0.3]        #for the best problem
    pw_max = [0.1, 0.2, 0.3, 0.5, 0.7]           #for the worst problem
    
    pw = pw_max[action] + (pw_min[action] - pw_max[action]) * ( (x-1)/9 )
    
    #for the probability of scoring if the batsmen is not getting out
    pr_min = 0.5
    pr_max = 0.8
    
    pr = pr_min + (pr_max - pr_min) * ( (x-1)/9)
    return (pw , pr)


def bellman (old_value):
    new_value = np.zeros (old_value.shape)
    policy = np.zeros (old_value.shape , dtype = int)
    
    #rows give the number of balls left
    #columns give the number of wicket left
    
    runs = [1,2,3,4,6]
    
    for i in range(1 , old_value.shape[0]):
        for j in range(1 , old_value.shape[1]):
            
            final_value = -1
            for action in [0,1,2,3,4]:               #actions encode the correspoding score he is trying to score
                ans = 0
                pw , pr = get_probabilies (action , j)   # 0 - 1, 1 - 2 , 2 -3 , 3 -4 ,4-6
                ans += pw * (0 + new_value[i-1][j-1])
                ans += (1-pw) * pr* (runs[action] + new_value[i-1][j] )
                ans += (1 - pw) * (1-pr) * (0 + new_value[i-1][j])    
                if (final_value < ans):
                    final_value = ans
                    policy[i][j] = runs[action]
            
            new_value[i][j] = final_value
    return  np.copy (new_value) ,np.copy(policy)


current_value = np.zeros ((301 , 11))
policy = np.zeros (current_value.shape , dtype = np.int)
update , policy= bellman (current_value)


np.set_printoptions(formatter={'float': '{: 0.0f}'.format})
np.savetxt("policy.txt" , policy , fmt = "%i")


np.savetxt("value.txt" , update , fmt = "%i")


