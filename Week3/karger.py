import random
 
file_handle = open("input.txt", "r")
graph = {}
for line in file_handle:
    node = int(line.split()[0])
    edges = []
    for edge in line.split()[1:]:
        edges.append(int(edge))
    graph[node] = edges
file_handle.close()
 
def karger(graph):
    while len(graph) > 2:
#final step when only two vertices are left in the graph
        removed = 0
        added = 0
        start = random.choice(graph.keys())
        finish = random.choice(graph[start])
#randomly choosing a edge that will be collapsed to nly the start node
 
    #Adding the edges from the absorbed node:
        for edge in graph[finish]:
            if edge != start:
                # this stops us from making a self-loop
                graph[start].append(edge)
                #this will add the edges of the collapsed node to the start  
               
    ## Deleting the references to the absorbed node and changing them to the source node:
        for edge in graph[finish]:
            graph[edge].remove(finish)
            if edge != start:
                # this stops us from re-adding all the edges in start.
                graph[edge].append(start)
        del graph[finish]
    print graph
    for i in graph:
        print len(graph[i])

karger(graph)

   
