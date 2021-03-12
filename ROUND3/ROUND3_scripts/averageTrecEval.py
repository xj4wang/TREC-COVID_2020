# parameter 1: document to read (col 1 = label, col 2 = included-topics, col 3 = score)
# NOTE: need to append iteration of k at the end
# parameter 2: k = number of partitions

import sys

def main():

    read_file_name = sys.argv[1] # getting rid of the ending to replace with iteration
    k = int(sys.argv[2])
    Dict = {}
    
    for i in range(1, k+1):
        read_file = open(read_file_name+"_"+str(i), "r")
        read_file.readline() # get rid of first line with has the run id (xj4wang)
        lines = read_file.readlines()
        read_file.close()

        for line in lines:
            temp = line.split()
            label = temp[0]
            score = float(temp[2].rstrip())
                
            if (i == 1):
                Dict[label] = score
            else:
                Dict[label] = Dict[label] + score
    
    for key in Dict:
        print(key + " " + str(round(Dict[key]/float(k),4)))
        
main()
