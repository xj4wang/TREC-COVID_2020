import csv
import sys

# parameter 1: testing file name (write file)
# parameter 2: testing file id name (read file)

def main():
        
    Dict = {}
    file = open("svm.fil", "r")   
    svm = file.readlines()
    file.close()
    for line in svm:
        temp = line.split(" ", 1)
        name = temp[0]
        feature_vector = temp[1]
        Dict[name] = feature_vector
    
    testing_file_name = sys.argv[1]
    testing_file = open(testing_file_name, "w")
    
    testing_file_ids_name = sys.argv[2]
    file = open(testing_file_ids_name, "r")
    testing_file_ids = file.readlines()
    file.close()
    
    for line in testing_file_ids:
        testing_file.write("-1 " + Dict[line.rstrip('\n')])
        
    testing_file.close()
    
main()
