import csv
import sys

# parameter 1: topic number
# parameter 2: training file name
# parameter 3: testing file name
# parameter 4: testing file id name
# parameter 5: working files path
# parameter 6: jj file

def main():
    
    topic = sys.argv[1]
    working_files = sys.argv[5]
    file_name = sys.argv[6]
    file = open(file_name, "r")   
    my_judgements = file.readlines()
    file.close()
    
    Dict = {}    
    
    for line in my_judgements:
        temp = line.split(",")
        name = temp[0]
        rel = temp[1]
        Dict[name] = rel[0]
         
    file = open("svm.fil", "r")   
    svm = file.readlines()
    file.close()
    
    training_file_name = sys.argv[2]
    training_file = open(training_file_name, "w")
    
    synthetic_file_name = working_files + "/svm.topic_" + topic + ".fil"
    synthetic_file = open(synthetic_file_name, "r")
    line = synthetic_file.readline()
    synthetic_file.close()
    svm.append(line)
    
    testing_file_name = sys.argv[3]
    testing_file = open(testing_file_name, "w")
    testing_file_ids_name = sys.argv[4]
    testing_file_ids = open(testing_file_ids_name, "w")
    for line in svm:
        temp = line.split(" ", 1)
        name = temp[0]
        feature_vector = temp[1]
        
        if name in Dict:        
            rel = 1
            if str(Dict[name]) == str(0):
                rel = -1
            training_file.write(str(rel) + " " + feature_vector)
        else:
            testing_file.write("-1 " + feature_vector)
            testing_file_ids.write(name + "\n")
        
    training_file.close()
    testing_file.close()
    testing_file_ids.close()
    
main()
