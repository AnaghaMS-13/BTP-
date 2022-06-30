#plot graph using LaTex
import os

def plot(x,y,n,arr): #takes x & y cordinates, no. of edges, laplacian matrix as arguments

	f = open("graphdrawing.tex", "w")
	f.write("\documentclass{article}\n")
	f.write("\usepackage{tikz}\n")
	f.write("\\title{learning}\n")
	f.write("\\begin{document}\n")
	
	
	f.write("\\begin{tikzpicture}[node distance={100 mm}, thick, main/.style = 	{draw, circle,inner sep=1.5}] \n")
	
	#loop to draw nodes
	for i in range(n): 	
		f.write("\\node[main] ("+str(i)+") at (" + str(7*x[i])  + "," + str(7*y[i]) 	+ ") {$x_{"+str(i)+"}$}; \n")
	

	#loop to draw edges
	for i in range(n): 
		for j in range(n): 
			if (arr[i][j]== -1) :
				f.write("\draw ("+str(i)+") -- ("+str(j)+"); \n")
	
	f.write("\end{tikzpicture}\n")
	f.write("\end{document}\n")
	f.close()	


os.system("texmaker graphdrawing.tex")   #automate opening of texmaker


