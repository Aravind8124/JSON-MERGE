import json
import glob
# the max number of file to be merged
x=input("enter the max")
#path ,name of the file
 path = "input-json/"
basename = "data"
dict = {}
dict["strikers"] = []
length = 100
files_name = glob.glob(path+basename+"*.json")
# reads individual files and stores its content in a list variable
json_list = []
counter = 0
for f in files_name:
    fp = open(f,'r')
    json_list.append(fp.read())
    fp.close()
for content in json_list:
    counter += 1
    temp = json.loads(content)
    temp = temp["strikers"]
    for element in temp:
        dict["strikers"].append(element)
    if counter == x:
        break
# for i in json_list:
#     dict["strikers"].append(i)

with open("merged_file.json", "wb") as fp:
    fp.write(str(dict))