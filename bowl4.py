import numpy as np
import numpy as np
import math
bowlers={1:(3, 33), 2:(3.5, 30), 3:(4, 24), 4:(4.5, 18), 5:(5, 15)}
#no of overs a bowler can bowl
ov_left={1:2,2:2,3:2,4:2,5:2}
def pro_wicket(b):
	x,y=bowlers[b]
	pr_run=x
	pr_wicket=6./y
	return(pr_run,pr_wicket)
def strategy():
	#value matrix stores the total runs till current overs againts the wicket remaining
	#policy matrix store the bowler chosen against the wicket remaining to bowl
	value = np.zeros ((4, 11))
	policy=np.zeros((4,11))
	for wickets in range(1,4):
		print "total run scored when wicket remaining is",wickets,"at the end of tenth over"
		for overs in range(1,11):
			run=1000	
			for bowler in range(1,6):
				if(ov_left[bowler]!=0):
					runs=0
					r,pw=pro_wicket(bowler)
					runs+= pw*(r + value[wickets-1][overs-1])
					runs+= (1-pw)*(r+ value[wickets][overs-1])
					if(runs<run):
							run=runs
							action=bowler
			value[wickets][overs]=run
			policy[wickets][overs]=action
			ov_left[action]-=1
			
			print "wickets_rem",wickets,"over_bowled",overs,"runscored_tillnow",run,"bowler_chosen",action
			print "over_left for each bowler"
			print(ov_left)
		for i in range(1,6):
			ov_left[i]=2
	return  np.copy (value),np.copy(policy)

val,pol=strategy()
np.set_printoptions(formatter={'float': '{: 0.0f}'.format})
np.savetxt("bowl_val.txt" , val , fmt = "%i")
np.savetxt("bowl_policy.txt" , pol , fmt = "%i")




