import csv
from collections import defaultdict
import operator


skill_dic = defaultdict()

with open('cover_graph.csv','r') as f:

    reader = csv.reader(f, delimiter=';', quotechar='"')
    for r in reader:
        if r[0] not in skill_dic:
            skill_dic[r[0]]={}
        skill_dic[r[0]].update({r[1]: float(r[2])})


requested_skill = "AutoCAD"

connected_skill = skill_dic[requested_skill]

print connected_skill


print max(connected_skill.iteritems(), key=operator.itemgetter(1))[0]


