from igraph import *

g = Graph.Read_GML("grafo_gml.ncol")

g.vs["weight"] = True

gs = Graph()

print (g.vs)

plot(g)

