# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
N = 10000
k = 10
pr=[0.10,0.50,0.60,0.80,0.90,0.25,0.60,0.45,0.75,0.65]
arm_selected = []
numbers_of_selections = [0] * k
sums_of_reward = [0] * k
total_reward = 0
def get_reward(arm):
		rand = np.random.random() 
		reward = 1 if (rand < pr[arm]) else 0
		return reward
for n in range(0, N):
    arm = 0
    max_upper_bound = 0
    for i in range(0, k):
	#shrinkage of level towards its mean value
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_reward[i] / numbers_of_selections[i]
            delta_i = math.sqrt(2 * math.log(n+1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            arm = i
    arm_selected.append(arm)
    numbers_of_selections[arm]+=1
    reward = get_reward(arm)
    sums_of_reward[arm] += reward
    total_reward += reward


print(numbers_of_selections)





