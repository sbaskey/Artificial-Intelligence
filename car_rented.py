#logic
#states is the number of cars in the each location
#poison distribution gives the expecter number of car rented and shifted .
#probabilty of shifted and rented are evaluated considering the
#poison distribution of each location
#optimum policies are decided for which it gives maximum reward value

from __future__ import print_function
import csv
import numpy as np
import copy
class Car:

    def __init__(self, gamma=0.9, capacity=(20, 10, 10), max_cars_moved=5):
        self.capacity = capacity
        self.max_cars_moved = max_cars_moved
        self.v = np.zeros((capacity[0], capacity[1], capacity[2]))
        self.gamma = gamma
        self.fact = self.generate_factorials()
        self.actions = self.generate_actions()
        self.states = self.generate_states()
        self.optimalAction = [[[0 for _ in range(capacity[2])] for _ in range(capacity[1])] for _ in range(capacity[0])]
        self.A = len(self.actions)
        self.pro1, self.pro2, self.left1, self.left2 = self.generate_probabilities()

    def generate_probabilities(self):
        pro1 = np.zeros((25, 3))
        pro2 = np.zeros((25, 3))
        left1 = np.zeros((25, 3))
        left2 = np.zeros((25, 3))

        sum1 = np.zeros(3)
        sum2 = np.zeros(3)

        l1 = [3, 2, 2]
        l2 = [3, 1, 1]

        for i in range(0, 25):
            for j in range(0, 3):
                p1 = self.poisson(i, l1[j])
                p2 = self.poisson(i, l2[j])
                pro1[i, j] = p1
                pro2[i, j] = p2
                sum1[j] += p1
                sum2[j] += p2
                left1[i, j] = sum1[j] 
                left2[i, j] = sum2[j]
        return pro1, pro2, left1, left2

    #factorial for poison distribution
    @staticmethod
    def generate_factorials(n=30):

        fact = np.zeros(n + 1)
        fact[0] = 1
        for i in range(1, n + 1):
            fact[i] = i * fact[i - 1]
        return fact

    #generates all possible transition states
    def generate_states(self):

        states = []
        for s1 in range(0, self.capacity[0]):
            for s2 in range(0, self.capacity[1]):
                for s3 in range(0, self.capacity[2]):
                    states.append((s1, s2, s3))
        return states

    def generate_actions(self):
        actions = []
        red = {}
        val = self.max_cars_moved
        for f1 in range(0, val + 1):
            for g1 in range(0, val + 1):
                for f2 in range(0, val + 1):
                    if f1 and f2: continue
                    for g2 in range(0, val + 1):
                        for f3 in range(0, val + 1):
                            if f3 and g1: continue
                            for g3 in range(0, val + 1):
                                if g2 and g3: continue
                                c = (f2 + f3 - f1 - g1, f1 + g3 - f2 - g2, g1 + g2 - f3 - g3)
                                cost = (f1 + g1 + f2 + f3) * 2
                                el = (f1, g1, f2, g2, f3, g3)
                                if c not in red or red[c][0] > cost:
                                    red[c] = cost, el
        for (i, j) in red.items():
            actions.append(j[1])

        return actions

    def poisson(self, n, lamb):
        return pow(lamb, n) / self.fact[n] * np.exp(-lamb)

    @staticmethod
    def inf_norm(a):

        res = -np.inf
        for i in range(0, a.shape[0]):
            for j in range(0, a.shape[1]):
                for k in range(0, a.shape[2]):
                    if abs(a[i, j, k]) > res:
                        res = abs(a[i, j, k])

        return res

    def generate_new_states(self, sn1, sn2, sn3, cn1, cn2, cn3):

        next_states = []
        for l1 in range(0, sn1):
            for l2 in range(0, sn2):
                for l3 in range(0, sn3):
                    for e1 in range(0, cn1):
                        for e2 in range(0, cn2):
                            for e3 in range(0, cn3):
                                next_states.append((l1, l2, l3, e1, e2, e3))
        return next_states

    def calculate_probabilites(self, a, b):

        l1, l2, l3, e1, e2, e3 = a
        sn1, sn2, sn3 = b

        if l1 == sn1:
            p1 = 1 - self.left1[l1, 0] + self.pro1[l1, 0]
        else:
            p1 = self.pro1[l1, 0]

        if l2 == sn2:
            p2 = 1 - self.left1[l2, 1] + self.pro1[l2, 1]
        else:
            p2 = self.pro1[l2, 1]

        if l3 == sn3:
            p3 = 1 - self.left1[l3, 2] + self.pro1[l3, 2]
        else:
            p3 = self.pro1[l3, 2]

        if sn1 - l1 + e1 == self.capacity[0] - 1:
            p4 = 1 - self.left2[e1, 0] + self.pro2[e1, 0]
        else:
            p4 = self.pro2[e1, 0]

        if sn2 - l2 + e2 == self.capacity[1] - 1:
            p5 = 1 - self.left2[e2, 1] + self.pro2[e2, 1]
        else:
            p5 = self.pro2[e2, 1]

        if sn3 - l3 + e3 == self.capacity[2] - 1:
            p6 = 1 - self.left2[e3, 2] + self.pro2[e3, 2]
        else:
            p6 = self.pro2[e3, 2]

        return p1, p2, p3, p4, p5, p6



    def value_iteration(self, v):

        optimalAct = None

        for state in self.states:
            s1, s2, s3 = state
            maxv = -np.inf

            for action in self.actions:
                f1, g1, f2, g2, f3, g3 = action
                if f1 + g1 > s1 or f2 + g2 > s2 or f3 + g3 > s3:
                    continue
                sn1 = s1 - f1 - g1 + f2 + f3
                sn2 = s2 - f2 - g2 + f1 + g3
                sn3 = s3 - f3 - g3 + g1 + g2

                if sn1 >= self.capacity[0] or sn2 >= self.capacity[1] or sn3 >= self.capacity[2]:
                    continue

                reward = (f1 + g1 + f2 + f3) * -2

                next_states = self.generate_new_states(sn1 + 1, sn2 + 1, sn3 + 1, self.capacity[0], self.capacity[1],
                                                       self.capacity[2])
                res = reward

                for next_state in next_states:
                    l1, l2, l3, e1, e2, e3 = next_state
                    p1, p2, p3, p4, p5, p6 = self.calculate_probabilites(next_state, (sn1, sn2, sn3))

                    if (sn1 - l1 + e1 >= self.capacity[0] or sn2 - l2 + e2 >= self.capacity[1] or sn3 - l3 + e3 >= self.capacity[2]):
                        continue

                    p = p1 * p2 * p3 * p4 * p5 * p6

                    fn1 = sn1 - l1 + e1
                    fn2 = sn2 - l2 + e2
                    fn3 = sn3 - l3 + e3
                    res = res + p * (10 * (l1 + l2 + l3) + self.gamma * v[fn1, fn2, fn3])
                #choosing the optimum action
                if res > maxv:
                    maxv = res
                    optimalAct = action

            v[state] = maxv
            self.optimalAction[state[0]][state[1]][ state[2]] = optimalAct

    def run(self, epsilon=0.1):
        cnter = 0
        last_v = self.v
        while True:
            new_v = copy.deepcopy(last_v)
            self.value_iteration(new_v)
            norm = self.inf_norm(last_v - new_v)
            last_v = new_v
            if norm < epsilon:
                break
            cnter += 1
        self.v = last_v


epsilon = 0.1
gamma = 0.9
capacity = 5,3,3

env = Car(gamma, capacity, 2)
env.run(epsilon)
print (env.v)
#np.savetxt("bowl_val.txt" , env.v )
#print (env.optimalAction)

