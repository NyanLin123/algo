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
        return self.src.getSrc()+'---->'+self.dest.getDest()

class graph(object):
    def __init__(self):
        self.edges = {}
    
    def addNode(self, node):
        if node in self.edge:
            raise ValueError("Duplicated Node")
        else:
            self.edges[node]=[]

    def addEdge(self, edge):
        src = edge.getSrc()
        dest = edge.getDest()
        if not(src in self.edges and dest in self.edges):
            raise ValueError("Don't see Node")
        else:
            self.edges[src].append(dest)

    def getChildren(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges