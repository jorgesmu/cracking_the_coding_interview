from heap import Heap
import random

def rebuild_path(start, destination, come_from):
	path = [destination]
	current_node = destination
	while current_node != start:
		current_node = come_from[current_node]
		path.append(current_node)
	path.reverse()
	return path

def edges_heap(edges):
	inequality = lambda x,y: x["priority"] < y["priority"]
	edges_copy = edges[:]
	for edge in edges_copy:
		edge["priority"] = 0
	return Heap(edges_copy, inequality) # Heap mins
		
def process_edge(edge):
	return edge["source"], edge["target"], edge["weight"]


def heuristic(node, destination):
	# This is a really bad heuristic. It might not lead to the best
	# path as its no minor than all the real distances in the graph
	# Also, it will probably waste time exploring the map in directions that are not necesarilly
	# towards the final destination
	return random.randrange(30)


def search_path(graph, start, destination):
	come_from = {}
	cost = {start: 0}
	visited = set([start])
	queue = edges_heap(graph[start])
	found = False
	while(not found and queue.size() > 0):
		source, target, edge_cost = process_edge(queue.pop())
		new_cost = cost[source] + edge_cost
		if  target not in visited or cost[target] > new_cost:
			come_from[target] = source
			cost[target] = cost[source] + edge_cost
			if target not in visited:
				edges_copy = graph[target][:]
				for edge in edges_copy:
					edge['priority'] = new_cost + heuristic(edge['target'], destination)
				queue.push_all(edges_copy)
			visited.add(target)
			if target == destination:
				found = True
	return found, come_from, cost

def disjktra(graph, start, destination):
	if start == destination:
		return {'path': [], 'cost': 0}
	found, come_from, cost = search_path(graph, start, destination)
	if not found:
		return {'path': None, 'cost': None}
	path =  rebuild_path(start, destination, come_from)
	return {'path': path, 'cost': cost[destination]}


# Assuming nodes have a numeric id and a list of edged
# with weight, graph is being represented as an Adjacency list
graph = {
	1: [
		{
			"source": 1, # Adding this for avoiding extra data processing in the code but could be made dinamically as its redundant
			"weight": 12,
			"target": 2
		}
	],
	2: [
		{
			"source": 2,
			"weight": 1,
			"target": 3
		},
	],
	3: [
		{
			"source": 3,
			"weight": 3,
			"target": 1
		},
		{
			"source": 3,
			"weight": 46,
			"target": 6
		},
		{
			"source": 3,
			"weight": 7,
			"target": 10
		}
	],
	4: [
		{
			"source": 4,
			"weight": 3,
			"target": 2
		},
		{
			"source": 4,
			"weight": 54,
			"target": 9
		}
	],
	5: [
		{
			"source": 5,
			"weight": 1,
			"target": 4
		},
		{
			"source": 5,
			"weight": 2,
			"target": 7
		}
	],
	6: [
		{
			"source": 6,
			"weight": 10,
			"target": 4
		}
	],
	7: [
		{
			"source": 7,
			"weight": 10,
			"target": 4
		}
	],
	8: [],
	9: [
		{
			"source": 9,
			"weight": 10,
			"target": 10
		},
		{
			"source": 9,
			"weight": 10,
			"target": 8
		}
	],
	10: [
		{
			"source": 10,
			"weight": 10,
			"target": 1
		}
	],
}
print('path from 1 to 2')
print(disjktra(graph, 1, 2))

print('path from 1 to 10')
print(disjktra(graph, 1, 10))

print('path from 3 to 9')
print(disjktra(graph, 3, 9))

print('path from 1 to 8')
print(disjktra(graph, 1, 8))

print('path from 8 to 1')
print(disjktra(graph, 8, 1))
