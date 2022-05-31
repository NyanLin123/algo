class node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSrc(self):
        return self.src
    
    def getDest(self):
        return self.dest
    
    def __str__(self):
        return self.getSrc()+' ----> '+ self.getDest()

class graph(object):
    def __init__(self):
        self.edges = {}
    
    def addNode(self, node):
        if node in self.edges:
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

    def getNode(self,name):
        for n in self.edges:
            if n == name:
                return n
            else:
                NameError(name)

    def getChildren(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src + '----->'+dest+'\n'
        return result[:-1]
        
class Graph(graph):
    def addEdge(self, edge):
        graph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        graph.addEdge(self, rev)


def cityGraph(graphType):
    for node in ('Maw','Than','Mu','Yan','Sag','Man'):
        graphType.addNode(node)
    graphType.addEdge(edge(graphType.getNode('Maw'), graphType.getNode('Yan')))
    graphType.addEdge(edge(graphType.getNode('Than'), graphType.getNode('Sag')))
    graphType.addEdge(edge(graphType.getNode('Man'), graphType.getNode('Maw')))
    graphType.addEdge(edge(graphType.getNode('Mu'), graphType.getNode('Sag')))
    graphType.addEdge(edge(graphType.getNode('Maw'), graphType.getNode('Yan')))
    return graphType

print(cityGraph(graph()))