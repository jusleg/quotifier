# Import some goodies
import sys, json,os

#Import Authors, Quotes, and File Extensions
with open('db.json') as json_data:
    db = json.load(json_data)
    json_data.close()
smajson = db['fileext']

# Write to file
def write_file(stringy_string,namy_name):
    os.remove(namy_name)
    text_file = open(namy_name, "w")
    text_file.write(stringy_string)
    text_file.close()

# MaGiC
def boringify(filename):
	full_file = ""
	for line in open(filename):		
		if (line[0] != smajson[filename[filename.index('.')+1:]]):
			full_file = full_file + line
	write_file(full_file,filename)

#Run the script on the output file
if (len(sys.argv) > 1):
    boringify(sys.argv[1])
