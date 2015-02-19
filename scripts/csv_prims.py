#!/usr/bin/env python

import sys
import csv
from collections import defaultdict
from collections import OrderedDict

# Graph class from https://gist.github.com/econchick/4666413
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
 
def getFirstCoord(coordinate):
  first = ""

  for char in coordinate:
    if char == '(':
      next
    elif char == ',':
      break
    else:
      first += str(char)

  return first

def getSecondCoord(coordinate):
  second = ""
  firstPassed = False

  for char in coordinate:
    if char == ',':
      firstPassed = True
    elif char == ')':
      next
    elif firstPassed:
      second += str(char)
    else:
      next

  return second

def prims(graph, initial):
  mst = Graph()
  mst.add_node(initial)
  distances = OrderedDict()

  nodes = graph.nodes
  current = initial

  while nodes:
    nodes.remove(current)
    adjacentEdges = graph.edges[current]

    for edge in adjacentEdges:
      string = "(" + str(current) + "," + str(edge) + ")"
      distances[string] = graph.distances[(current,edge)]
    
    sortedDistances = OrderedDict(sorted(distances.items(), key=lambda t: t[1]))
    
    while sortedDistances:
      coord = sortedDistances.popitem(last=False)[0]
      first = getFirstCoord(coord)
      second = getSecondCoord(coord)
      if int(second) in nodes:
        break

    if not sortedDistances:
      return mst

    mst.add_node(second)
    mst.add_edge(first, second, 0)

    current = int(second)

  return mst


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

mst = prims(g, 47)

for node in mst.edges:
  for edge in mst.edges[node]:
    print airports[int(node)] + ',' + airports[int(edge)]

#for key in path:
#	print airports[key] + "," + airports[path[key]]