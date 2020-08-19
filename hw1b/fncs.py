import numpy as np
import networkx as nx


def get_parents(node):
	child_edges = edges[np.where(edges[:,1] == node)]
	return child_edges[:,0]

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
	marked_nodes = { i : False for i in nodes }
	#children = set(edges[:,1])
	ord_i = 0
	# TODO: You will need to change this code
	while ord_i < N - 1:
		for node in nodes:
			if marked_nodes[node]:
				continue
			child_edges = edges[np.where(edges[:,1] == node)]
			if child_edges.size > 0:
				parents = child_edges[:,0]
				parent_not_marked = False
				for parent in parents:
					if not marked_nodes[parent]:
						parent_not_marked = True
						break
				if parent_not_marked:
					continue
			marked_nodes[node] = True
			Ord[node] = ord_i
			ord_i += 1
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


def test():
	G = nx.DiGraph()
	G.add_edges_from(
		[('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
		('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])
	Ord = compTopOrder(G.edges)
	print('Ordering = ',Ord)
	H = nx.relabel_nodes(G, Ord)
	checkTopOrder(H.edges)

if __name__ == '__main__':
	test()