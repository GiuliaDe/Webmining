import csv
from collections import defaultdict

jobs_list = defaultdict(list)

with open('grafo_bipartito.csv','r') as f:

    reader = csv.reader(f, delimiter=',', quotechar='|')
    for r in reader:
        jobs_list[r[0]].append(r[1])


#print jobs_list

totaldic = defaultdict()

skills = jobs_list.keys()

for s1 in skills:
    jobs1 = set(jobs_list[s1])
    s1dic = defaultdict(int)
    total = 0
    for s2 in skills:
        if s1 != s2:
            jobs2 = set(jobs_list[s2])
            common = len(jobs1.intersection(jobs2))
            if common > 0:
                s1dic[s2] = common
                total += common
    for k, v in s1dic.iteritems():
        s1dic[k] = 1.0 *v/total
    print s1dic
    totaldic[s1] = s1dic


with open('cover_graph.csv', 'w') as f:
    file_writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    for k, v in totaldic.iteritems():
        for k1, v1 in v.iteritems():
            row = [k,k1,v1]

            file_writer.writerow(row)
