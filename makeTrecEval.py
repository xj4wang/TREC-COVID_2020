# parameter 1: write file name (append only)
# parameter 2: document to read (col 1 = score, col 2 = docid)
# parameter 3: current topic number 
# parameter 4: i = number of partition currently on

import sys

def main():

    write_file_name = sys.argv[1]
    read_file_name = sys.argv[2]
    topic = sys.argv[3]
    i = int(sys.argv[4])
    
    read_file = open(read_file_name, "r")
    lines = read_file.readlines()
    read_file.close()
    
    write_file = open(write_file_name, "a")
    
    runtag = "xj4wang"
    
    query_id = str(topic) + "_" + str(i)
    rank = 1
    for line in lines:
        temp = line.split(" ")
        score = temp[0]
        docid = temp[1].rstrip()
        
        ## topicid Q0 docid rank score run-tag ##
        write_file.write(topic + " Q0 " + docid + " " + str(rank) + " " + score + " " + runtag + "\n")
        rank = rank+1 
    write_file.close()
    
main()
