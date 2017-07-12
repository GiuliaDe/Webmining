from collections import defaultdict
import dbdatahandler as ddh
from igraph import *

db, cursor = ddh.open_connection()


#una serie di nodi sono le skill

#altra serie di nodi sono gli annunci di lavoro

nodes = defaultdict(int)

i=0

select_skills = "SELECT distinct(skill) FROM Jobs.indeed_skills join lavori_all on lavori_all.jobkey= indeed_skills.jobkey where lavori_all.used_for_analysis=1;"

result = cursor.execute(select_skills)
res = cursor.fetchall()

valid_skills = []

for r in res:
    valid_skills.append(r[0])
    nodes[r[0]]=i
    i+=1

print valid_skills

select_jobkey = "SELECT distinct(indeed_skills.jobkey) FROM Jobs.indeed_skills join lavori_all on lavori_all.jobkey= indeed_skills.jobkey where lavori_all.used_for_analysis=1;"

result = cursor.execute(select_jobkey)
res = cursor.fetchall()

valid_jobkeys = []

for r in res:
    valid_jobkeys.append(r[0])
    nodes[r[0]]=i
    i+=1


g=Graph()
g.add_vertices(i)

vertex_names = valid_skills.append(valid_jobkeys)

#g.vs["names"] = vertex_names

#print valid_jobkeys

select_jk_skill = "select jobkey from indeed_skills where skill = %s;"

for s in valid_skills:
    #s=valid_skills[0]
    print s
    result = cursor.execute(select_jk_skill,(s,))
    res = cursor.fetchall()
    for r in res:
        if r[0] in valid_jobkeys:
            node1 = nodes[s]
            node2 = nodes[r[0]]
            g.add_edge(node1,node2)

g.save("grafo_gml.ncol", format="gml")


#save(g,'/home/giulia/git_projects/JobAnalyser/Webmining/bigraph.txt')