#using method 1 : ie taking n-f columns out of n column in matrix
#tutte embedding

import numpy as np
import math

from dk_newplot import plot	   #function to plot graph in tikz
from dk_truncate import trunc      #function to truncate rows and col


#adding variable cordinates & fixed cordinates;return val will be used to create tikz file
def updatecoordinate(fixcord,varcord,n,cycle):
	
	
	varcord=varcord.flatten() ##flatten used to change 2D matrix to 1D 
	

	update_cordinate =[]
	k=0
	l=0
	for i in range(n):
		if i in cycle:
			update_cordinate.append(fixcord[k])
			k=k+1
		else:
			update_cordinate.append(varcord[l])
			l=l+1
	
	return update_cordinate


#solve linear equation
def linear(array1,array2): 
    
	solution = np.linalg.solve(array1, array2)
        return solution


#to do matrix multiplication
def matrix_multiplication(array1,array2):

	return( np.dot(array1, array2) )


#to find degree of a particular vertex 
def deg(x):   
	return(len(graph[x]))


#create matrix if i==j then deg of vertex;else -1 if edge exist / 0 is edge not exist
def matrix(n):
	arr = np.zeros( (n,n) ) 
	for i in range(n) :
	  for j in range(n) :
		if(i==j):
			arr[i,j]=deg(i)  	#function that returns degree of vertex 
		else :
			if i in graph[j]:	#if edges present: -1
	        		arr[i,j]= -1	
			else:
	      			arr[i,j]=  0	#if edges not present : 0
        return(arr)
	


#return value only take fixed cordinate and leaving out rest
def separate(n,f,cycle,listt):
	fixedcord_part= map(listt.__getitem__, cycle)
	return fixedcord_part



#find cycle in graph to set as fixed
def cyclefn():
   return [0,1,2,3,4,5] #hard coded 


#find fixed cycle cordinates by using properties of convex polygons
def fix_cycle(n,f,cycle,count):
	x1=1
	y1=1		
	x=np.zeros(n)
	y=np.zeros(n)
	c=0           #count
	for k in range(n) :      
	    if k in cycle:        
	    	x[k]=x1*math.cos((2*math.pi*c)/f)
	    	y[k]=y1*math.sin((2*math.pi*c)/f)
		c=c+1	
	if count == 0 :
		return(x)
	else:
		return(y)


			

#....................................................................

#input graph___________ assumptn now: 3-connected planar graph
graph = {
  0 : [5,1,6] ,
  1 : [0,2,6] ,
  2 : [1,3,6] ,
  3 : [2,4,6] ,
  4 : [3,5,6] ,
  5 : [4,0,6] ,
  6 : [0,1,2,3, 4, 5] 
}

n=7	#n is number of total vertices
f=6	# f is number of fixed vertices ie the outer cycle vertices

cycle=cyclefn()	#cycle contains indes of fixed vertices
arr=matrix(n)	# arr is the laplacian matrix for given graph

fix=trunc(1,n,arr,cycle)	#flag=1 , 

      
A=trunc(0,n,arr,cycle)		#flag=0 returns A matrix after truncating arr

#.......
x=fix_cycle(n,f,cycle,0) #x contains cordinates and flag =0 specifies x-axis
fixed_xcord=separate(n,f,cycle,x) #truncating x to have only size of f

xnew= np.zeros( (f,1) )#ynew is y but represented as column matrx, to do matrix mul
		
for i in range(f):                
	xnew[i][0] =fixed_xcord[i]

			#B of x matix got by matrix multiplication and taking neg value
B=  - (matrix_multiplication(fix,xnew) )  
  
xsoln=linear(A,B)	#xsoln is solving linear equation for matrix A and B 



#.......
y=fix_cycle(n,f,cycle,1) #y contains cordinates and flag =1 specifies y-axis 
fixed_ycord=separate(n,f,cycle,y)

ynew= np.zeros( (f,1) )	#ynew is y but represented as column matrx, to do matrix mul  		
for i in range(f):
	ynew[i][0] =fixed_ycord[i]

			#B of y matix got by matrix multiplication and taking neg value
B= -( matrix_multiplication(fix,ynew) )
           
ysoln = linear(A,B)
   
X=updatecoordinate(fixed_xcord,xsoln,n,cycle)
Y=updatecoordinate(fixed_ycord,ysoln,n,cycle)
plot(X,Y,n,arr)






