import nltk

def txt_to_string(filename):
	file = open(filename, "r")
	return file.read()
	# print file.read()

# txt_to_string("ladygaga.txt")

tokens = nltk.word_tokenize(txt_to_string("ladygaga.txt"))
# print tokens

pos_labels = nltk.pos_tag(tokens)
# print pos_labels

# all_adjectives = []

adjective_counts = {}

for pair in pos_labels:
	if pair[1] == "JJ" or pair[1] == "JJR" or pair[1] == "JJS":
		if pair[0] not in adjective_counts.keys():
			adjective_counts[pair[0]] = 1
		else:
			adjective_counts[pair[0]] += 1
		# all_adjectives.append(pair)

print adjective_counts