#   Erich Eden
#   SY301
#   Dr. Mayberry
#   graph.py

class Graph:
    def __init__(self, dotfile):
        self.vertices = []
        with open(dotfile, "r") as graph:
            for line in graph:
                parsed = line.split(" ")
                print(parsed)

                if parsed[0] == "}" or parsed[0] == "}\n":
                    break
                elif parsed[0] == "graph":
                    self.graphName = parsed[1]
                    #print(self.graphName)
                else:
                    vertex1 = parsed[3].strip() #depending on your sample dot file, these indexes may be wrong. Mine parsed my 'tab' as 3 empty strings. Idk why.
                    vertex2 = parsed[5].strip().rstrip(";")
                    vert1check = False
                    vert2check = False
                    for i in range(len(self.vertices)):
                        if self.vertices[i].key == vertex1: #vertex already in vertex list  vertices
                            vert1check = True
                            v1index = i
                            vertex1 = self.vertices[i] #change the variable vertex1 from a string to the vertex w that string as its key
                        if self.vertices[i].key == vertex2: #vertex already in vertex list  vertices
                            vert2check = True
                            v2index = i
                            vertex2 = self.vertices[i]
                    if not vert1check:
                        #make a vertex vertex1 and get its index in the graph
                        vertex1 = Vertex(vertex1, [])
                        self.vertices.append(vertex1)
                        for i in range(len(self.vertices)):
                            if self.vertices[i].key == vertex1.key:
                                v1index = i

                    if not vert2check:
                        #make a vertex vertex2 and get its index in the graph
                        vertex2 = Vertex(vertex2, [])
                        self.vertices.append(vertex2)
                        for i in range(len(self.vertices)):
                            if self.vertices[i].key == vertex2.key:
                                v2index = i


                    #make sure vertex1 is in vertex2's adjacencyList and vice versa
                    if not self.isAdjacent(vertex1, vertex2):
                        self.vertices[v1index].adjacencyList.append(vertex2)
                        self.vertices[v2index].adjacencyList.append(vertex1)




    def isAdjacent(self, vertexA, vertexB):
        for i in range(len(self.vertices)):
            if self.vertices[i].key == vertexA:
                for j in range(len(self.vertices[i].adjacencyList)):
                    if self.vertices[i].adjacencyList[j].key == vertexB:
                        return True
        return False

    def returnAdjacent(self, vertex):
        for i in range(len(self.vertices)):
            if self.vertices[i].key == vertex:
                adjV = []
                for j in range(len(self.vertices[i].adjacencyList)):
                    adjV.append(self.vertices[i].adjacencyList[j].key)

                return adjV

        return 1
    def __str__(self):
        edgeList = []
        for i in range(len(self.vertices)):
            part1 = self.vertices[i].key
            for j in range(len(self.vertices[i].adjacencyList)):
                part2 = self.vertices[i].adjacencyList[j].key

                reverse = part2 + " -- " + part1
                entry = part1 + " -- " + part2
                if reverse not in edgeList and entry not in edgeList:
                # check to see if entry's reverse is in edgeList. If not, add it.

                    edgeList.append(entry)
        return edgeList

class Vertex:
    def __init__(self, vertex, adjacencyList):
        self.key = vertex
        self.adjacencyList = adjacencyList
    def addAdjacent(self, newNeighbor):
        self.adjacencyList.append(newNeighbor)
