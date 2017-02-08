# Import some goodies
import sys, json, random, io,os

# Genereate a random number between 5 and 15
def random_modulo():
    return random.randint(5,15)

# Genereate a random quote - by a random author
def gen_quote():
    random_author = random.randint(0,len(author)-1)
    random_quote = random.randint(0,len(bajson_quotes)-1)
    return bajson_quotes[random_quote] + " - " + author[random_author]

# Write to file
def write_file(stringy_string,namy_name):
	#removes file path from namy_name
    os.remove(namy_name)
    text_file = open(namy_name, "w")
    text_file.write(stringy_string)
    text_file.close()

# MaGiC
def do_the_whole_shabang(filename):
    counter = 0
    modulo = random_modulo()
    full_file = ""
    for line in open(filename):
        counter += 1
        full_file = full_file + line
        if (counter % modulo == 0):
            full_file = full_file + smajson[filename[filename.index('.')+1:]] + " " + gen_quote() + "\n"
    write_file(full_file,filename)

#Import Authors, Quotes, and File Extensions
with open('db.json') as json_data:
    db = json.load(json_data)
    json_data.close()

author = db['authors']
bajson_quotes = db['quotes']
smajson = db['fileext']

#Run the script on the output file
if (len(sys.argv) > 1):
    do_the_whole_shabang(sys.argv[1])