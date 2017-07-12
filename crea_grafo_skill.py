from igraph import *

vlist = range(10)
elist= [(1,5),(1,6),(1,7),(1,8),(1,4),(2,5),(2,7),(2,9),(3,4),(3,6),(3,9),(0,5),(0,6),(0,7),(0,8)]

# g = Graph()
g = Graph(vertex_attrs={"label":vlist}, edges=elist, directed=True)
# g.add_vertices(10)
# g.add_edges(elist)

plot(g)

