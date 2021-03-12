import csv
import sys

# parameter 1: qrel file
# parameter 2: final write file
# parameter 3: final read file

def main():
    
    qrel_file_name = sys.argv[1]
    final_write_file_name = sys.argv[2]
    final_read_file_name = sys.argv[3]

    file = open(qrel_file_name, "r")   
    qrel_lines = file.readlines()
    file.close()
    
    file = open(final_read_file_name, "r")   
    final_read_lines = file.readlines()
    file.close()
    
    file_write = open(final_write_file_name, "w")   
    for line in final_read_lines:
        if line not in qrel_lines:
            file_write.write(line)
    file_write.close()       
    
main()
