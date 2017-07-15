from igraph import *

g = Graph.Read_GML("grafo_gml_type.ncol")

g.vs["weight"] = True

gs = Graph()
gs.vs["weight"] = True

summary(g)

for v in g.vs:
    if v["types"] == "skill":
        gs.add_vertex(v)
        gs.vs[v] = len(neighbors())
print (g.vs)

summary(gs)

#plot(g)

