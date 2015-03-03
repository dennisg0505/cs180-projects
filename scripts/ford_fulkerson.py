#!/usr/bin/env python

class Edge(object):
	def __init__(self, u, v, w):
		self.source = u
		self.sink = v  
		self.capacity = w
	def __repr__(self):
		return "%s->%s:%s" % (self.source, self.sink, self.capacity)
 
class FlowNetwork(object):
	def __init__(self):
		self.adj = {}
		self.flow = {}
 
	def add_vertex(self, vertex):
		self.adj[vertex] = []
 
	def get_edges(self, v):
		return self.adj[v]
 
	def add_edge(self, u, v, w=0):
		if u == v:
			raise ValueError("u == v")
		edge = Edge(u,v,w)
		redge = Edge(v,u,0)
		edge.redge = redge
		redge.redge = edge
		self.adj[u].append(edge)
		self.adj[v].append(redge)
		self.flow[edge] = 0
		self.flow[redge] = 0
 
	def find_path(self, source, sink, path):
		if source == sink:
			return path
		for edge in self.get_edges(source):
			residual = edge.capacity - self.flow[edge]
			if residual > 0 and edge not in path:
				result = self.find_path( edge.sink, sink, path + [edge]) 
				if result != None:
					return result
 
	def max_flow(self, source, sink):
		path = self.find_path(source, sink, [])
		while path != None:
			residuals = [edge.capacity - self.flow[edge] for edge in path]
			flow = min(residuals)
			for edge in path:
				self.flow[edge] += flow
				self.flow[edge.redge] -= flow
			path = self.find_path(source, sink, [])
		return sum(self.flow[edge] for edge in self.get_edges(source))

g = FlowNetwork()

airports = ["MDL", "DEL", "JFK", "SIN", "CDG", "RGN", "SHA", "LAX"]

for airport in airports:
	g.add_vertex(airport)

links = [
	"MDL DEL 5",
	"MDL SIN 6",
	"MDL RGN 7",
	"DEL JFK 3",
	"DEL CDG 5",
	"DEL SIN 4",
	"SIN CDG 4",
	"SIN SHA 1",
	"SIN RGN 6",
	"RGN SHA 7",
	"JFK LAX 5",
	"JFK CDG 3",
	"CDG LAX 7",
	"CDG SHA 4",
	"SHA LAX 9"
]

for link in links:
	temp = link.split()
	g.add_edge(temp[0], temp[1], int(temp[2]))

print g.max_flow("MDL", "LAX")