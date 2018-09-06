import numpy as np
import pickle
import time
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd     
from load_data import load_data
import helper_functions as hf

rank = 0
size = 20


start = time.time()

fname = 'reality_miningdata'
filename = 'data/'+fname+'.txt'
G, to_predict, fullG = load_data(filename)

directed=False
k=len(to_predict)
min_links = k
score_tolerance=1e-10
score_inf=1e18
force_exact=False


A = nx.adjacency_matrix(G)
num_nodes = A.shape[0]
node_list = G.nodes()
degrees = np.sum(A, axis=1)
M = A/degrees
r = list(range(num_nodes))
eigval = hf.scipy_eigsh(M)

for i in range(num_nodes):
	for j in range(rank,num_nodes,size):
		if A[i,j] == 0 and i!=j:
			first = hf.partition(M,np.array([i,j]),np.array([i,j]))
			comp = hf.complement(r,[i,j])
			second = hf.partition(M,np.array([i,j]),comp) 
			temp = hf.partition(M, comp, comp)
			third = np.linalg.inv(hf.partition(M, comp, comp)-eigval*np.identity(num_nodes-2))
			fourth = hf.partition(M, comp,np.array([i,j]))
			okay = second @ third @ fourth
			this = first-okay
			send = this[0,1]	
			

if rank==0:
	print(time.time() - start)










