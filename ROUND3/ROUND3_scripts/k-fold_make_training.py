import csv
import sys

# parameter 1: k
# parameter 2: working files path

def main():
    
    k = int(sys.argv[1])
    working_files = sys.argv[2]
    
    # create dictionary for docids and their feature representations
    file = open("svm.fil", "r")   
    svm = file.readlines()
    file.close()
    Dict_features = {}
    for line in svm:
        temp = line.split(" ", 1)
        docid = temp[0]
        feature = temp[1]
        Dict_features[docid] = feature
        
    # create list of dictionary for docids and their rel judgements (list size = # of topics)
    num_of_topics = 30
    list_of_Dict_judgements = []
    
    for i in range(0, num_of_topics+1): # position 0 isn't actually used, it's just a place holder
        list_of_Dict_judgements.append({})
    
    file = open("qrels-rnd1.txt", "r")   
    qrels = file.readlines()
    file.close()
    
    for line in qrels:
        temp = line.split(" ")
        topic = int(temp[0])
        docid = temp[3]
        judgement = temp[4].rstrip('\n')      
        list_of_Dict_judgements[topic][docid] = judgement
        
    # create training files    
    for topic in range(1, num_of_topics+1):
        for i in range(1, k+1):
            file = open(working_files+"/group_"+str(i), "r")   
            docids = file.readlines()
            file.close()
            
            file = open(working_files+"/train_file_"+str(topic)+"_"+str(i), "w")
            for docid in docids:
                docid = docid.rstrip('\n')
                rel = "0"
                if docid in list_of_Dict_judgements[topic]:
                    rel = list_of_Dict_judgements[topic][docid]
                if (rel == "0"):
                    rel = "-1"
                else:
                    rel = "1"
                file.write(rel + " " + Dict_features[docid])
            file.close()
            
    
main()

