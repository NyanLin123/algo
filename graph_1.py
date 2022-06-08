from curses import newpad
from turtle import st


class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def __str__(self):
        return self.src.getSrc()+' -------> '+self.dest.getDest()


class Graph(object):
    # create new dictionary
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicated Node")
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSrc()
        dest = edge.getDest()
        if not(src in self.edges and dest in self.edges):
            raise ValueError("Don't see")
        self.edges[src].append(dest)

    def getNode(self, name):
        for node in self.edges:
            if node == name:
                return node
            else:
                raise NameError("Name Error")

    def getChildren(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.eges

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src + ' -----> ' + dest + '\n'
        return result


def cityGraph(g):
    for city in ("maw", "yan", "mu", "than", "pyin", "nay", "man"):
        g.addNode(city)
    g.addEdge(Edge("maw", "man"))
    g.addEdge(Edge("maw", "mu"))
    g.addEdge(Edge("maw", "pyin"))
    g.addEdge(Edge("nay", "maw"))
    g.addEdge(Edge("mu", "pyin"))
    g.addEdge(Edge("than", "man"))
    g.addEdge(Edge("than", "nay"))
    g.addEdge(Edge("than", "yan"))
    g.addEdge(Edge("than", "pyin"))
    return g


def printPath(path):
    result = path[0]
    for i in path[1:]:
        result = result+'->'+i
    return result


def dfs(graph, start, end, path, shortest, toPrint):
    path = path + [start]
    if toPrint:
        print("Current DFS path:", printPath(path))
    if start == end:
        return path
    for node in graph.getChildren(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = dfs(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
            elif toPrint:
                print("Expressed path")
    return shortest


g = cityGraph(Graph())

def bfs(graph, start, end, toPrint):
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.getChildren(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath +[nextNode]
                pathQueue.append(newPath)
    return None

print("Depth First Search")
dfs(g, 'maw', 'pyin', [], None, toPrint=True)
print('------------')
print("Breath First Search")
bfs(g,'maw','pyin', toPrint=True)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Distance of vertex from source")
        for key, value in dist.items():
            print(' '+key, ' :   ', value)

    def bellmanFord(self, src):
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for temp in range(self.V-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    print("Graph contains negative cycle")

            return self.print_solution(dist)


g = Graph(5)
lst = ["A", "B", "C", "D", "E"]
for i in lst:
    g.addNode(i)

g.add_edge("A", "C", 6)
g.add_edge("A", "D", 5)
g.add_edge("B", "C", 1)
g.add_edge("A", "B", 2)
g.add_edge("C", "E", 2)

g.bellmanFord("E")
