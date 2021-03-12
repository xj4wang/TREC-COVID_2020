import csv
import sys

# parameter 1: runid (xj4wang_runX)
# parameter 2: number of topics (round3 = 40)
# parameter 3: topic names (e.g. run2_results)

def main():
    
    doc_name = sys.argv[3]
    write_file = open(doc_name, "w")   
    
    runtag = sys.argv[1]
    n = int(sys.argv[2])
    n = n+1
    
    
    for i in range(1, n):
        read_file_name = (doc_name + "_" + str(i))
        read_file = open(read_file_name, "r")   
        lines = read_file.readlines()
        read_file.close()
        
        rank = 1
        score = 1000
        for docid in lines:
            ## topicid Q0 docid rank score run-tag ##
            write_file.write(str(i) + " Q0 " + docid.rstrip() + " " + str(rank) + " " + str(score) + " " + runtag + "\n")
            rank = rank+1
            score = score-1   
    
    write_file.close()
    
main()
