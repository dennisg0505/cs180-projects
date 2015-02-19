#!/usr/bin/env python

import sys
import csv
from collections import defaultdict

# Graph class and dijkstra function from https://gist.github.com/econchick/4666413
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}
 
  def add_node(self, value):
    self.nodes.add(value)
 
  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance
 
def dijkstra(graph, initial):
  visited = {initial: 0}
  path = {}
 
  nodes = set(graph.nodes)
 
  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node
 
    if min_node is None:
      break
 
    nodes.remove(min_node)
    current_weight = visited[min_node]
 
    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node
 
  return visited, path


g = Graph()
for i in range(93):
	g.add_node(i + 1)

rowIndex = 0;
reader = csv.reader(sys.stdin.read().split('\n'))
for row in reader:
	if rowIndex == 0:
		header = row
	else:
		if row: 
			if row[0] < row[1] and row[4] != "0":
					g.add_edge(int(row[2]), int(row[3]), float(row[4]))
	rowIndex += 1

airports = [ 'ABQ', 'AMA', 'ANC', 'ATL', 'AUS', 'BDL', 'BFI', 'BGR', 'BHM', 'BIL', 
             'BNA', 'BOS', 'BUF', 'BWI', 'CHS', 'CLE', 'CLT', 'CMH', 'CPR', 'CRP', 
             'CVG', 'DAY', 'DEN', 'DFW', 'DLH', 'DSM', 'ERI', 'EWR', 'FAI', 'FLL', 
             'FWA', 'GEG', 'GPT', 'GRB', 'GSO', 'GSP', 'HNL', 'HSV', 'IAD', 'IAH', 
             'ICT', 'IND', 'JAN', 'JAX', 'JFK', 'LAS', 'LAX', 'LBB', 'MBS', 'MCI', 
             'MCO', 'MDW', 'MEM', 'MIA', 'MKE', 'MLI', 'MSP', 'MSY', 'MYR', 'OAK', 
             'ONT', 'ORD', 'ORF', 'PBI', 'PDX', 'PHF', 'PHL', 'PHX', 'PIT', 'PWM', 
             'RDU', 'RFD', 'RIC', 'RNO', 'ROC', 'RST', 'RSW', 'SAN', 'SAT', 'SAV', 
             'SDF', 'SEA', 'SFB', 'SFO', 'SJC', 'SLC', 'SMF', 'SRQ', 'STL', 'SYR', 
             'TPA', 'TUL', 'TUS' ]

out = dijkstra(g, 47)
path = out[1]

for key in path:
	print airports[key-1] + "," + airports[path[key]-1]