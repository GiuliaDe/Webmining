import csv
from collections import defaultdict
import operator


skill_dic = defaultdict()

with open('cover_graph.csv','r') as f:

    reader = csv.reader(f, delimiter=';', quotechar='"')
    for r in reader:
        # print (r)
        if r[0].lower() not in skill_dic:
            skill_dic[r[0].lower()]={}
        skill_dic[r[0].lower()].update({r[1].lower(): float(r[2])})


# requested_skill = "AutoCAD"
#
# connected_skill = skill_dic[requested_skill]
# print (connected_skill)
#
# print (max(connected_skill.iteritems(), key=operator.itemgetter(1))[0])
# print (sorted(connected_skill.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])

print("#############")
print("Welcome to the DTV skill recommendation system")
# print("Benvenuto al sistema di raccomandazione di competenze DTV")
print("############# \n")
print("You can enter a skill you are interested in and we will suggest you other skills you should be interested in to succesfully find a job")
# print("Inserendo una competenza digitale di interesse verranno consigliate ")
# print ("Write the skill for which you want to find the 5 most similar")
print ("Write 'x' to stop the program \n")
skillInput = raw_input("Enter the skill: ").lower().strip()

while skillInput != "x":
    if skillInput in skill_dic:
        connected_skill = skill_dic[skillInput]
        output = sorted(connected_skill.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]
        print("\n")
        i = 1
        for el in output:
            skill = " "+el[0]
            print(str(i) + skill)
            # print(connected_skill)
            i += 1
        print("\n")
        skillInput = raw_input("Enter the skill: ").lower().strip()
    else:
        print ("The skill you requested isn't in our list, please try again")
        skillInput = raw_input("Enter the skill: ")
        print("\n")

print("That's all folks!")
print("Thank you for using the DTV skill finder")



