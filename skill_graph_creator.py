from igraph import *

g = Graph.Read_GML("")

g.vs["weight"] = True