import nltk
from operator import itemgetter
import time
import csv
import sys
reload(sys)

sys.setdefaultencoding("ISO-8859-1")

start_time = time.time()

def txt_to_string(filename):
	file = open(filename, "rb")
	return file.read()
	# print file.read()

all_words = ''

### UNCOMMENT below for NBA files
filenames = txt_to_string("data/NBAfilenames.txt").split()
for name in filenames:
	data_name = "data/NBA_txt_Files/" + name
	all_words += txt_to_string(data_name)

# print all_words.len()
### UNCOMMENT below for WNBA files
# all_words += txt_to_string("data/WNBA_Main.txt")

### UNCOMMENT below for WTA files
# filenames = txt_to_string("data/WTAfilenames.txt").split()
# for name in filenames:
# 	data_name = "data/WTA_txt_Files/" + name
# 	all_words += txt_to_string(data_name)

### UNCOMMENT below for ATP files
# filenames = txt_to_string("data/ATPfilenames.txt").split()
# for name in filenames:
# 	data_name = "data/ATP_txt_Files/" + name
# 	all_words += txt_to_string(data_name)

tokens = nltk.word_tokenize(all_words)
# print tokens
# count = 0
# for word in tokens:
# 	count += 1
# print count

all_word_counts = {}

for word in tokens:
	if word not in all_word_counts.keys():
		all_word_counts[word] = 1
	else:
		all_word_counts[word] += 1

print sorted(all_word_counts.items(), key = itemgetter(1))

myFile = open('NBA_all_counts.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(all_word_counts.items())
     
print("Writing all counts complete")

pos_labels = nltk.pos_tag(tokens)
# print pos_labels

descriptive_counts = {}

for pair in pos_labels:
	if pair[1] == "JJ" or pair[1] == "JJR" or pair[1] == "JJS" or pair[1] == "RB" or pair[1] == "RBR" or pair[1] == "RBS": #refer to pos_dictionar.txt for meanings of different tags
		if pair[0] not in adjective_counts.keys():
			descriptive_counts[pair[0]] = 1
		else:
			descriptive_counts[pair[0]] += 1

print sorted(descriptive_counts.items(), key=itemgetter(1)) #sort by adjective count in ascending order

myFile = open('NBA_descriptive_counts.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(descriptive_counts.items())
     
print("Writing descriptive counts complete")

print("--- %s seconds ---" % (time.time() - start_time))