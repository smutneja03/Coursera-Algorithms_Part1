#!/usr/bin/env python
import sys
sys.setrecursionlimit(300000)
N = 875714
G={}
#graph with the directions as per the input file
Grev={}
#graph with the directions reversed
for i in range(1, N+1):
    G[i]=[]
    Grev[i]=[]
fin=open("SCC.txt", "r")
for line in fin:
    v1=int(line.split()[0])
    v2=int(line.split()[1])
    G[v1].append(v2)
    Grev[v2].append(v1)
fin.close()
#global variables to keep record
visited={}
#whether the node is visited or not
finish={}
#to keep a record of finishing time of the nodes in the first half
leader={}
#to keep record of the leaders of the scc in the 2nd pass
t = 0
s = 0

def dfs(G, i):
    global t, s
    visited[i]=1
    leader[i]=s
    for j in G[i]:
        if(visited[j]==0): 
            dfs(G,j)
    t=t+1
    finish[i]=t

def dfs_loop(G):
    global t, s,N
    t=0 #number of nodes processed so far
    s=0 #current source vertex
    i=N
    for i in range(1,N+1):
#initially setting all to be none 
        visited[i]=0
        finish[i]=0
        leader[i]=0

    while(i>0):
        if(visited[i]==0):
            s=i
            dfs(G,i)
        i=i-1


#everything set
#finally ready to call the functions with the right graph kind in the corr order
dfs_loop(Grev) 
#THE FIRST LOOP ON REVERSE GRAPH
#done with the second step of the three steps algorithm
# construct new graph
newGraph={}
for i in range(1,N+1):
    temp=[]
    for x in G[i]: 
        temp.append(finish[x])
#to keep record of the edges of the actual nodes in the correct order
    newGraph[finish[i]]=temp

dfs_loop(newGraph) #THE SECOND LOOP 
#done with the third step of the three steps algorithm

    # statistics
lst= sorted(leader.values())
stat=[]
pre=0
for i in range(0,N-1):
    if lst[i]!=lst[i+1]:
        stat.append(i+1-pre)
        pre=i+1
stat.append(N-pre)
L= sorted(stat)
L.reverse()
print(L[0:10])
