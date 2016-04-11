# forming a large review document with all the review concatenated into one line
review = ''	
unig_list = []
bigr_list = []

# making a large review text
with open("new_data.txt", "r") as fin:
	review = ''		
	for line in fin:
		review += line[1:].rstrip()	

# making a unigram set
ug = set(review.split())
# separation of unigram with count > 1
for key in ug:
	if review.count(key) > 1:
		# print str(key)+"\r" 
		unig_list.append(key)

# tokenising and making of all bigram combinations 
input_list = review.split()
for i in range(len(input_list)-1):
    bigr_list.append((input_list[i], input_list[i+1]))

# making a bigram set and separation of bigram with count > 1
bg = set(bigr_list)
bigr_list = []
for key in bg:
	substr = str(key[0])+" "+str(key[1])
	if review.count(substr) > 1:
		bigr_list.append(substr)


# print unig_list
unig_list.sort()
bigr_list.sort()
with open("unigram.txt", "w") as fd:
	for i in unig_list:
		fd.write(str(i))
		fd.write("\n")

with open("bigram.txt", "w") as fd:
	for i in bigr_list:
		fd.write(i)
		fd.write("\n")

print "ugram length: ", len(unig_list)
print "bigram length: ", len(bigr_list)
print "unique ug created earlier:", len(ug)
print "unique bg created earlier:", len(bg)
