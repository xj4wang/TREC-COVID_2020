import csv
import sys
import subprocess as sp
import re

# parameter 1: $starter_topic
# parameter 2: $topic 
# parameter 3: $directory
# parameter 4: $relevant_words_file

def highlight_green(display_string, words_to_highlight):
    display_string_WORKING = display_string    
    
    for word in words_to_highlight:
        length = len(word)
        locations = [m.start() for m in re.finditer(word, display_string_WORKING, re.IGNORECASE)]
        offset = 0
        for i in locations:
            cur_offset = i + offset
            highlighted_word = '\x1b[6;30;42m' + display_string_WORKING[cur_offset:cur_offset+length] + '\x1b[0m' # actual substring is used to help detect errors in offsets
            display_string_WORKING = display_string_WORKING[:cur_offset] + highlighted_word + display_string_WORKING[cur_offset+length:]
            offset = offset + len(highlighted_word) - length
    
    return display_string_WORKING

def main(doc_name, topic, path, words_to_highlight):
    print(path + "/" + doc_name)
    reader = csv.reader(open(path + "/" + doc_name, "r"))
    content = []
    
    savefile_name = "WORKINGFILES/jj_topic_" + str(topic)
    
    for row in reader:
        for col in row:
            content.append(col)
            
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("CURRENT TOPIC: " + str(topic))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Publish Time: " + highlight_green(content[9], words_to_highlight)) #publish time
    print("Authors: " + highlight_green(content[10], words_to_highlight)) #authors
    print("Journal: " + highlight_green(content[11], words_to_highlight)) #journal
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Title: " + highlight_green(content[3], words_to_highlight)) #title
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Abstract: " + highlight_green(content[8], words_to_highlight)) #abstract
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    value = input("Please enter your relevancy judgement {0,1,2}:\n")
    savefile_value = doc_name + "," + value
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
    write_file = open(savefile_name, "a+")    
    write_file.write(savefile_value + "\n")
    write_file.close()
    print("The following judgement has been saved to " + savefile_name + ":")
    print(savefile_value)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# STUFF STARTS HERE #    
top10_rel = sys.argv[1]
topic = sys.argv[2]
path = sys.argv[3]

######################################
## GETTING HIGHLIGHTING STUFF start ##
######################################
readfile_name = sys.argv[4]
read_file = open(readfile_name, "r")
lines = read_file.readlines()    
read_file.close()

words_to_highlight = [] # array of lists of words to highlight

# each line contains exactly all string to highlight for each document
for line in lines:
    words = line.rstrip('\n') # get rid of trailing new-line character
    words = words.split(",")
    words_to_highlight.append(words)
        
####################################
## GETTING HIGHLIGHTING STUFF end ##
####################################

file = open(top10_rel, "r")
lines = file.readlines()
file.close()
count = 1
total = len(lines)
for line in lines:
    tmp = sp.call('clear',shell=True)
    print(str(count) + "/" + str(total))
    main(line.rstrip('\n'), topic, path, words_to_highlight[count-1])
    count = count+1

# Print stopping condition
savefile_name = "WORKINGFILES/jj_topic_" + str(topic)
file = open(savefile_name, "r") 
lines = file.readlines()
file.close()
n=0 #non-rel
m=0 #rel
for line in lines:
    rel = line.split(",")[1].rstrip('\n')
    if str(rel) == str("0"):
        n = n+1
    else:
        m = m+1
a = 0.5 # non-rel per rel to review, 0.5 by paper
b = 20 # fixed overhead, 1000 by paper
temp = a*m+b
print("NOT-REL: " + str(n) + " to REL:" + str(m))
print(str(n) + " > " + str(temp) + " <- stop when true")
