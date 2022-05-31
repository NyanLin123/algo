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
        if not( src in self.edges and dest in self.edges):
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
                result = result+ src +' -----> '+ dest + '\n'
        return result



def cityGraph(g):
    for city in ("maw","yan","mu","than","pyin","nay","man"):
        g.addNode(city)
    g.addEdge(Edge("maw","man"))
    g.addEdge(Edge("maw","mu"))
    g.addEdge(Edge("maw","pyin"))
    g.addEdge(Edge("nay","maw"))
    g.addEdge(Edge("mu","pyin"))
    g.addEdge(Edge("than","man"))
    g.addEdge(Edge("than","nay"))
    g.addEdge(Edge("than","yan"))
    g.addEdge(Edge("than","pyin"))
    result = g.getChildren("maw")

    return result
    
print(cityGraph(Graph()))