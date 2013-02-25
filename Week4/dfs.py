#!/usr/bin/en python

graph = {"s" :["a", "b"] , "a":["s", "c"], "b":["c", "s", "d"], "c":["a", "b", "d", "e"], "d":["b", "c", "e"], "e":["c", "d"]}

start = "s"
def depth_first_search(graph, start):
	visited = {}
	for i in graph:
		visited[i] = 0
#will keep record of all the visited vertices
#initially all the nodes are kept as yet to be visited
	stack = []
	visited[start] = 1
	stack.append(start)
	while len(stack)!=0:
		node = stack.pop(-1)
#explore agressively , backtrack only when necessary
		for edge in graph[node]:
			if visited[edge]==0:#not visited yet
				visited[edge] = 1
				stack.append(edge)
 				print "queue at the next step is ", stack
	print visited
depth_first_search(graph,start)
