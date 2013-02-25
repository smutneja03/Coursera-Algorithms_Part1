#The file contains the edges of a directed graph. 
#Vertices are labeled as positive integers from 1 to 875714. 
#Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head
# (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex).
# So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646
#Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph. 

#Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). 
#So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If your algorithm #finds less than 5 SCCs, then write 0 for the remaining terms. 
#Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be #"400,300,100,0,0".

from sys import argv

import sys
sys.setrecursionlimit(300000)
#dfs implementation
#0 univistied
#1 visited
#2 explored



#globals
visited={}
finish={}
leader={}

def init():
    for i in range(1,N+1):
        visited[i] = 0
        finish[i] = 0
        leader[i] = 0

#dfs function
def dfs(G, i):
    global t
    visited[i] = 1
    leader[i] = s
    for j in G[i]:
        if(visited[j] == 0): dfs(G,j)
    t = t + 1
    finish[i] = t


#visit the nodes	
def dfs_loop(G):
    global t
    global s
    t = 0 #number of nodes processed so far
    s = 0 #current source vertex
    i = N
    while( i > 0):
        if(visited[i] == 0):
            s = i
            dfs(G, i)
        i = i -  1




#graph
G = { }
#transpose of graph
GT = { }

#max number of vertices
N = 875714

for i in range(1, N+1) :
	G[i] = []
	GT[i] = []

# read from file		
script, filename = argv
for line in open(filename,'r').readlines():	
	inputstr = []
	inputstr = line.split()
	x = int(inputstr[0])
	y = int(inputstr[1])
	G[x].append(y)
	GT[y].append(x)


#connected component logic						
init()
dfs_loop(GT)

newGraph={}
for i in range(1,N+1):
       temp=[]
       for x in G[i]: temp.append(finish[x])
       newGraph[finish[i]] = temp
init()
dfs_loop(newGraph)

# statistics
a_list= sorted(leader.values())
stat=[]
pre=0
for i in range(0,N-1):
    if a_list[i] != a_list[i+1]:
        stat.append(i+1-pre)
        pre = i+1
stat.append(N-pre)
final_answer= sorted(stat)
final_answer.reverse()
print(final_answer[0:5])	
