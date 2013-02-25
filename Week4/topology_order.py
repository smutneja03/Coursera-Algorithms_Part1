#!/usr/bin/env python

graph = {"s" :["v", "w"] , "v":["t"], "w":["t"], "t" :[]}

current_label = len(graph)
visited = {}
mark = {}

def depth_first_search(graph, start):
	global visited, mark, current_label
	stack = []
	visited[start] = 1
	for edge in graph[start]:
		if visited[edge]!=1:
			depth_first_search(graph, edge)
	mark[start] = current_label
	current_label -=1 	

def depthfirstsearch_loop(graph):
	global visited, mark, current_label
	for i in graph:
        	visited[i] = 0#will keep record of all the visited vertices #initially all the nodes are kept as yet to be visited
	for node in graph:
		if visited[node]==0:
			depth_first_search(graph, node)
	
depthfirstsearch_loop(graph)

print mark
