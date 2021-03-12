import xml.etree.ElementTree as ET
import sys

# parameter 1: topic document
# parameter 2: starter file name (without topic number)
# parameter 3: name for file with list of starter file names

def main():
    doc_name = sys.argv[1]
    
    tree = ET.parse(doc_name)
    root = tree.getroot()
    
    savefile_name = sys.argv[2]
    starter_names_file = sys.argv[3]
    
    names_file = open(starter_names_file, "a+")  

    for child in root: #topic
        topic = child.get('number')
        temp = savefile_name + str(topic) # synthetic file to start query with (has rel=1 since it does not answer the question), not that it matters in the end
        names_file.write(temp + "\n")
        
        query = child.find('query').text
        question = child.find('question').text
        narrative = child.find('narrative').text
        
        write_file = open(temp, "w")    
        #write_file.write(query)        
        write_file.write(query + "\n" + question + "\n" + narrative)
        write_file.close()
    
    names_file.close()
    
main()