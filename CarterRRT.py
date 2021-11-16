import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from random import randrange
import numpy as np
import math
from networkx.classes.function import path_weight

def rrt(Wolrd,Start,End,Obs,Res):
	nodes = {}
	nodes[0] = (Start[0],Start[1])
	nodePoses = []
	nodePoses.append(Start)
	tree = nx.Graph()
	pathFound = False
	minLen =57.5
	itr = 0
	while pathFound == False:
		newNode = [randrange(0,50),randrange(0,50)]
		minid = float("inf")
		
		closest = -1
		for i in range(len(nodePoses)):
			if np.hypot(nodePoses[i][0]-newNode[0],nodePoses[i][1]-newNode[1]) <= Res:
				if np.hypot(nodePoses[i][0]-newNode[0],nodePoses[i][1]-newNode[1]) <= minid:
					minid = np.hypot(nodePoses[i][0]-newNode[0],nodePoses[i][1]-newNode[1])
					closest = i
				else:
					pass
			else:
				pass
		if closest != -1:
			itr+=1
			nodePoses.append(newNode)
			nodes[itr] = (newNode[0],newNode[1])
			tree.add_edge(closest,itr,weight=np.hypot(nodePoses[closest][0]-nodePoses[itr][0],nodePoses[closest][1]-nodePoses[itr][1]))
			if np.hypot(End[0]-newNode[0],End[1]-newNode[1]) <=  End[2]:
				if nx.shortest_path_length(tree,source=0,target=itr,weight='weight') <= minLen:
					pathFound=True
				else:
					pass
			else:
				pass
		else:
			pass
		
	options = {
		"font_size": 1,
		"node_size": 3,
		"node_color": "white",
		"edgecolors": "black",
		"linewidths": 5,
		"width": 5,
	}
	path = nx.shortest_path(tree,0,itr,weight='weight')
	nx.draw_networkx(tree, nodes, **options)
	path_x = []
	path_y = []
	for j in range(len(path)):
		path_x.append(nodePoses[path[j]][0])
		path_y.append(nodePoses[path[j]][1])
	
	plt.plot(path_x,path_y)
	endRegion =plt.Circle((End[0],End[1]),End[2],color='r')
	ax = plt.gca()
	ax.add_patch(endRegion)
	plt.axis("on")
	plt.show()

def main():
	World = [50,50] #Map size
	Start = [1,1] #Start coordinate
	End = [30,30,5] #End Coordinate with radius
	Obs = [] #Obstacles and obstacle radii
	Res = 3 #Resolution of rrt
	rrt(World,Start,End,Obs,Res)

if __name__ == '__main__':
	main()

