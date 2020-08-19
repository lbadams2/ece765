import numpy as np

# This function computed the topological ordering a graph. It
# takes as an input an array of edges. It returns a dictionary
# mapping the old nodes to the corresponding entry in the 
# ordering.
def compTopOrder(edges):
	# Initializing edges and nodes
	edges = np.array(edges)
	nodes = set(edges.flatten())
	
	# Initializing Ordering
	Ord = {}
	
	# Extracting the number of Nodes
	N = len(nodes)

	# TODO: You will need to change this code
	for node in nodes:
		Ord[node] = node
		
	return Ord

# This function performs the check for topological ordering.
# It retuns 'True' if the check is satisfied. It takes as an
# input an array of edges.
def checkTopOrder(edges):
	# Initializing edges and nodes
    edges = np.array(edges)
    nodes = set(edges.flatten())
	
	# Initializing check to 'True'
    flag = True
	
	# Iterating for edges until the condition is not valid
    for node in nodes:
		# Extracting parents from edges
        par = edges[edges[:,1]==node,0]
		
		# Checking that the parents have a lower ordering
        v = np.prod(par<node)
		
		# If condition is violated then returning 'False'
        if(v==0):
            flag = False
            break
    return flag
