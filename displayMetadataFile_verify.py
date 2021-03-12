import csv
import sys
import subprocess as sp
import re

# parameter 1: $starter_topic
# parameter 2: $topic 
# parameter 3: $directory

def main(doc_name, topic, path):
    print(path + "/" + doc_name)
    reader = csv.reader(open(path + "/" + doc_name, "r"))
    content = []
    
    savefile_name = "WORKINGFILES/verify_topic_" + str(topic)
    
    for row in reader:
        for col in row:
            content.append(col)
            
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("CURRENT TOPIC: " + str(topic))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Publish Time: " + content[9]) #publish time
    print("Authors: " + content[10]) #authors
    print("Journal: " + content[11]) #journal
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Title: " + content[3]) #title
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Abstract: " + content[8]) #abstract
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    value = input("Please enter your relevancy judgement {0,1,2}:\n")
    savefile_value = doc_name + "," + value
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# STUFF STARTS HERE #    
top10_rel = sys.argv[1]
topic = sys.argv[2]
path = sys.argv[3]


file = open(top10_rel, "r")
lines = file.readlines()
file.close()
count = 1
total = len(lines)
for line in lines:
    tmp = sp.call('clear',shell=True)
    print(str(count) + "/" + str(total))
    main(line.rstrip('\n'), topic, path)
    count = count+1
