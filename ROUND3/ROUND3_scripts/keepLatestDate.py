import csv
import sys
import datetime

# parameter 1: read document name
# parameter 2: write document name

def main():
    doc_name = sys.argv[1]
    reader = csv.reader(open(doc_name, "r"))
    content = []
        
    for row in reader:
        for col in row:
            content.append(col)
    
    num_of_fields = 19
    num_of_lines = int(len(content)/num_of_fields)
    
    d_max = datetime.datetime(1500, 1, 1)
    index_max = -1
    for i in range(0,num_of_lines):
        temp = content[9+(i*num_of_fields)].split("-")
        
        if (len(temp) == 1):
            d_temp = datetime.datetime(int(temp[0]), 1, 1)
        elif (len(temp) > 1):
            d_temp = datetime.datetime(int(temp[0]), int(temp[1]), int(temp[2]))
        else:
            d_temp = datetime.datetime(1600, 1, 1)
        
        if (d_temp > d_max):
            index_max = i
            d_max = d_temp
    
    # Save the max dated line as the file
    file = open(doc_name, "r")
    lines = file.readlines()
    file.close()
    
    write_name = sys.argv[2]
    print(write_name)
    if (index_max < 0):
        print("ERROR!!!")
    file = open(write_name, "w")
    file.write(lines[index_max])    
    file.close()    

main()