#function that takes laplacian matrix of a graph and return a truncated matrices based on flag that is taken a argument  

import numpy as np
def trunc(flag,n,arr,cycle):

	notcycle=[]
	for i in range(n):
            	if i not in cycle:
			notcycle.append(i)
	var=arr
	fix=arr
	
	#column deletion
	var = np.delete(var, (cycle), axis=1)     
	fix = np.delete(fix, (notcycle), axis=1)
	
	#row deletion
	var = np.delete(var, (cycle), axis=0)    
	fix = np.delete(fix, (cycle), axis=0)


	if flag == 0 :      #return value based on flag
		return var
	else :
		return fix

