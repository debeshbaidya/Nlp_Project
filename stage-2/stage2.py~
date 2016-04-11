import re

stop_word_file = open('stopwords.txt', 'r')
dataset_file = open('data.txt', 'r')
new_dataset_file = open('new_data.txt', 'w')

stop_words = stop_word_file.readlines()
for i in range(len(stop_words)):
	stop_words[i] = re.sub('\r\n', '', stop_words[i])
	
i = 0

line = dataset_file.readline()

while line:
	line = line.lower()
	review = line[0]
	new_line = re.sub('\'', '', line)	
	new_line = re.sub('[_+-=~`?.,!@#$%^&*(){}\[\]:;\/|<>"\']', ' ', new_line)		
	new_line = re.sub(r' ([a-z0-9])*([0-9])([a-z0-9])', ' ', new_line)
	new_line = re.sub(r'\b[a-zA-Z]{1,2}\b', '', new_line)	

	for stop_word in stop_words:
		new_line = re.sub(' ' + stop_word + ' ', ' ', new_line)
	
	
	new_line = re.sub(r'[\s]+', ' ', new_line)
	new_dataset_file.write(review + ' ' + new_line + '\n')

	line = dataset_file.readline()
	
dataset_file.close()
new_dataset_file.close()
