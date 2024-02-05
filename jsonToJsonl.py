#https://stackoverflow.com/questions/62091789/list-of-json-files-into-jsonl-file-using-python
import os, json
import pandas as pd

directory = '/Path/To/Your/Json/Directory'  #Specify your json directory path here

json_list=[]    #Initiate a new blank list for storing json data in list format
for dirpath, subdirs, files in os.walk(directory):
    print(dirpath)
    print(filename)
    print(file)
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(dirpath, file)) as json_file: 
                data = json.load(json_file) 
                json_list.append(data)

#Now, output the list of json data into a single jsonl file
with open('output.jsonl', 'w') as outfile:
    for entry in json_list:
        json.dump(entry, outfile)
        outfile.write('\n')
